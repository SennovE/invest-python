import re
import typing
from ast import Call, Constant, Expr, Load, Name, alias

from iprotopy.imports import ImportFrom
from iprotopy.service_method_generator import (
    BaseServiceMethodGenerator,
    ServiceMethodGenerator,
    ServiceMethodStreamStreamFunctionGenerator,
    ServiceMethodStreamUnaryFunctionGenerator,
    ServiceMethodUnaryStreamFunctionGenerator,
    ServiceMethodUnaryUnaryFunctionGenerator,
)


class BaseServiceMethodGeneratorExtended(BaseServiceMethodGenerator):
    def create(self, method):
        func_def = super().create(method)
        func_def.name = (
            re.sub(r"(?<!^)(?=[A-Z])", "_", method.name).replace("-", "_").lower()
        )
        func_def.decorator_list = [
            Call(
                func=Name(id="handle_request_error", ctx=Load()),
                args=[Constant(value=method.name)],
                keywords=[],
            )
        ]
        return func_def

    def _add_function_body_imports(self):
        super()._add_function_body_imports()
        self._importer.add_import(
            ImportFrom(
                module="tinkoff.invest.logging",
                names=[
                    alias(name="get_tracking_id_from_call"),
                    alias(name="log_request"),
                ],
                level=0,
            )
        )


class BaseServiceAnyUnaryFunctionGenerator(BaseServiceMethodGeneratorExtended):
    def _add_function_body_imports(self):
        super()._add_function_body_imports()
        self._importer.add_import(
            ImportFrom(
                module="tinkoff.invest._errors",
                names=[
                    alias(name="handle_request_error"),
                ],
                level=0,
            )
        )


class BaseServiceAnyStreamFunctionGenerator(BaseServiceMethodGeneratorExtended):
    def _add_function_body_imports(self):
        super()._add_function_body_imports()
        self._importer.add_import(
            ImportFrom(
                module="tinkoff.invest._errors",
                names=[
                    alias(name="handle_request_error_gen"),
                ],
                level=0,
            )
        )


class ServiceMethodUnaryUnaryFunctionGeneratorExtended(
    BaseServiceAnyUnaryFunctionGenerator,
    ServiceMethodUnaryUnaryFunctionGenerator,
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


class ServiceMethodStreamUnaryFunctionGeneratorExtended(
    BaseServiceAnyUnaryFunctionGenerator,
    ServiceMethodStreamUnaryFunctionGenerator,
):
    ...


class ServiceMethodUnaryStreamFunctionGeneratorExtended(
    BaseServiceAnyStreamFunctionGenerator,
    ServiceMethodUnaryStreamFunctionGenerator,
):
    ...


class ServiceMethodStreamStreamFunctionGeneratorExtended(
    BaseServiceAnyStreamFunctionGenerator,
    ServiceMethodStreamStreamFunctionGenerator,
):
    ...


class ServiceMethodGeneratorExtended(ServiceMethodGenerator):
    _method_generators: typing.Dict[
        typing.Tuple[bool, bool], typing.Type[BaseServiceMethodGenerator]
    ] = {
        (False, False): ServiceMethodUnaryUnaryFunctionGeneratorExtended,
        (True, False): ServiceMethodStreamUnaryFunctionGeneratorExtended,
        (False, True): ServiceMethodUnaryStreamFunctionGeneratorExtended,
        (True, True): ServiceMethodStreamStreamFunctionGeneratorExtended,
    }
