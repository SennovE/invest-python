import logging
import sys
from pathlib import Path

import iprotopy.service_generator

from scripts.generate_models.service_method_generator_extention import (
    ServiceMethodGeneratorExtended,
)

iprotopy.service_generator.ServiceMethodGenerator = ServiceMethodGeneratorExtended

from iprotopy import PackageGenerator, protos_generator
from iprotopy.message_class_generator import MessageClassGenerator
from iprotopy.one_of_generator import OneOfGenerator
from iprotopy.type_mapper import TypeMapper

from scripts.generate_models.message_class_field_generator import (
    ExtendedClassFieldGenerator,
)

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


def add_fields_helpers(origin_field_generator):
    def init(self, *args, **kwargs):
        origin_field_generator(self, *args, **kwargs)
        self._class_field_generator = ExtendedClassFieldGenerator(
            self._importer, self._type_mapper
        )
        self._one_of_generator = OneOfGenerator(self._class_field_generator)

    return init


def run_executable(original_run):
    def run(cmd, *a, **kw):
        if isinstance(cmd, (list, tuple)) and cmd and cmd[0] == "python":
            cmd = [sys.executable] + list(cmd[1:])
        return original_run(cmd, *a, **kw)

    return run


if __name__ == "__main__":
    protos_generator.subprocess.run = run_executable(protos_generator.subprocess.run)
    TypeMapper.__init__ = extended_types(TypeMapper.__init__)
    MessageClassGenerator.__init__ = add_fields_helpers(MessageClassGenerator.__init__)

    generator = PackageGenerator()
    base_dir = Path().absolute()

    generator.generate_sources(
        proto_dir=base_dir / "protos",
        out_dir=base_dir,
    )
