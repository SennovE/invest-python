import logging
import re
import sys
from ast import Call, Constant, Expr, Load, Name, alias
from pathlib import Path

from iprotopy import PackageGenerator, protos_generator
from iprotopy.imports import ImportFrom
from iprotopy.service_method_generator import (
    BaseServiceMethodGenerator,
    ServiceMethodUnaryUnaryFunctionGenerator,
)
from iprotopy.type_mapper import TypeMapper

logging.basicConfig(level=logging.DEBUG)


def extended_types(origin_mapper):
    def init(self):
        origin_mapper(self)
        self._standard_types_mapping.update(
            {
                "string": "str",
                "bytes": "bytes",
                "bool": "bool",
                "double": "float",
                "float": "float",
                "int32": "int",
                "sint32": "int",
                "sfixed32": "int",
                "uint32": "int",
                "fixed32": "int",
                "int64": "int",
                "sint64": "int",
                "sfixed64": "int",
                "uint64": "int",
                "fixed64": "int",
            }
        )

    return init


def service_func_names_to_snake_case(origin_creater):
    def create(self, method):
        func_def = origin_creater(self, method)
        func_def.name = (
            re.sub(r"(?<!^)(?=[A-Z])", "_", method.name).replace("-", "_").lower()
        )
        return func_def

    return create


def add_logging_to_imports(origin_importer):
    def add_imports(self):
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
        return origin_importer(self)

    return add_imports


def add_logging_to_service_funcs(original_get_func_body):
    def get_function_body(self, method):
        body = original_get_func_body(self, method)
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

    return get_function_body


def run_executable(original_run):
    def run(cmd, *a, **kw):
        if isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "python":
            cmd = [sys.executable] + list(cmd[1:])
        return original_run(cmd, *a, **kw)

    return run


if __name__ == "__main__":
    protos_generator.subprocess.run = run_executable(protos_generator.subprocess.run)
    TypeMapper.__init__ = extended_types(TypeMapper.__init__)
    BaseServiceMethodGenerator.create = service_func_names_to_snake_case(
        BaseServiceMethodGenerator.create
    )
    BaseServiceMethodGenerator._add_function_body_imports = add_logging_to_imports(
        BaseServiceMethodGenerator._add_function_body_imports
    )
    ServiceMethodUnaryUnaryFunctionGenerator._get_function_body = (
        add_logging_to_service_funcs(
            ServiceMethodUnaryUnaryFunctionGenerator._get_function_body
        )
    )

    generator = PackageGenerator()
    base_dir = Path().absolute()

    generator.generate_sources(
        proto_dir=base_dir / "protos",
        out_dir=base_dir,
    )
