import re
import typing
from ast import Call, Constant, Expr, FunctionDef, Load, Name

from iprotopy.service_method_generator import (
    ServiceMethodGenerator as DefaultServiceMethodGenerator,
    ServiceMethodStreamStreamFunctionGenerator as DefaultServiceMethodStreamStreamFunctionGenerator,
    ServiceMethodStreamUnaryFunctionGenerator as DefaultServiceMethodStreamUnaryFunctionGenerator,
    ServiceMethodUnaryStreamFunctionGenerator as DefaultServiceMethodUnaryStreamFunctionGenerator,
    ServiceMethodUnaryUnaryFunctionGenerator as DefaultServiceMethodUnaryUnaryFunctionGenerator,
)
from proto_schema_parser.ast import Method

from scripts.generate_models.code_generators.base_generators import (
    BaseServiceMethodGenerator,
    BaseSyncServiceAnyStreamFunctionGenerator,
    BaseSyncServiceAnyUnaryFunctionGenerator,
)


class ServiceMethodUnaryUnaryFunctionGenerator(
    BaseSyncServiceAnyUnaryFunctionGenerator,
    DefaultServiceMethodUnaryUnaryFunctionGenerator,
):
    def _get_function_body(self, method):
        body = super()._get_function_body(method)
        log_request = Expr(
            value=Call(
                func=Name(id="log_request", ctx=Load()),
                args=[
                    Call(
                        func=Name(id="get_tracking_id_from_call", ctx=Load()),
                        args=[Name(id="call", ctx=Load())],
                        keywords=[],
                    ),
                    Constant(value=method.name),
                ],
                keywords=[],
            )
        )
        body.insert(-1, log_request)
        return body


class ServiceMethodStreamUnaryFunctionGenerator(
    BaseSyncServiceAnyUnaryFunctionGenerator,
    DefaultServiceMethodStreamUnaryFunctionGenerator,
):
    ...


class ServiceMethodUnaryStreamFunctionGenerator(
    BaseSyncServiceAnyStreamFunctionGenerator,
    DefaultServiceMethodUnaryStreamFunctionGenerator,
):
    ...


class ServiceMethodStreamStreamFunctionGenerator(
    BaseSyncServiceAnyStreamFunctionGenerator,
    DefaultServiceMethodStreamStreamFunctionGenerator,
):
    ...


class SyncServiceMethodGenerator(DefaultServiceMethodGenerator):
    _method_generators: typing.Dict[
        typing.Tuple[bool, bool], typing.Type[BaseServiceMethodGenerator]
    ] = {
        (False, False): ServiceMethodUnaryUnaryFunctionGenerator,
        (True, False): ServiceMethodStreamUnaryFunctionGenerator,
        (False, True): ServiceMethodUnaryStreamFunctionGenerator,
        (True, True): ServiceMethodStreamStreamFunctionGenerator,
    }

    def process_service_method(self, method: Method) -> FunctionDef:
        func_def = super().process_service_method(method)
        func_def.name = (
            re.sub(r"(?<!^)(?=[A-Z])", "_", method.name).replace("-", "_").lower()
        )  # to snake_case
        return func_def
