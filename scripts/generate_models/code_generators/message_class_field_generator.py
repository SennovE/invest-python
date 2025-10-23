import keyword as default_keyword
from ast import AnnAssign, Call, Constant, Load, Name, Store, Subscript, alias, keyword

from iprotopy.annotation_generator import AnnotationGenerator
from iprotopy.domestic_importer import DomesticImporter
from iprotopy.imports import ImportFrom
from iprotopy.message_class_generator import (
    MessageClassGenerator as DefaultMessageClassGenerator,
)
from iprotopy.one_of_generator import OneOfGenerator
from iprotopy.type_mapper import TypeMapper
from proto_schema_parser import Field, FieldCardinality


class ClassFieldGenerator:
    def __init__(self, importer: DomesticImporter, type_mapper: TypeMapper):
        self._importer = importer
        self._type_mapper = type_mapper
        self._annotation_generator = AnnotationGenerator(importer, type_mapper)

    def process_field(self, field: Field) -> AnnAssign:
        if field.cardinality == FieldCardinality.REPEATED:
            return self._process_repeated_field(field)
        elif field.cardinality == FieldCardinality.OPTIONAL:
            return self._process_single_field(field, is_optional=True)
        else:
            return self._process_single_field(field)

    def _safe_field_name(self, unsafe_field_name: str) -> str:
        if default_keyword.iskeyword(unsafe_field_name):
            return f"{unsafe_field_name}_"
        return unsafe_field_name

    def _construct_field(
        self,
        field: Field,
        annotation: Name | Subscript,
        is_optional: bool = False,
    ) -> AnnAssign:
        safe_field_name = self._safe_field_name(field.name)
        self._importer.add_import(
            ImportFrom(
                module="tinkoff.invest._grpc_helpers",
                names=[
                    alias(name="message_field"),
                ],
                level=0,
            )
        )
        if is_optional:
            self._importer.add_import(
                ImportFrom(module="typing", names=[alias(name="Optional")], level=0)
            )
            annotation = Subscript(
                value=Name(id="Optional", ctx=Load()),
                slice=annotation,
                ctx=Load(),
            )
        return AnnAssign(
            target=Name(id=safe_field_name, ctx=Store()),
            annotation=annotation,
            value=Call(
                func=Name(id="message_field", ctx=Load()),
                args=[Constant(value=field.number)],
                keywords=([keyword("optional", Constant(True))] if is_optional else []),
            ),
            simple=1,
        )

    def _process_repeated_field(self, field: Field):
        self._importer.add_import(
            ImportFrom(module="typing", names=[alias(name="List")], level=0)
        )
        field_type = self._annotation_generator.process_annotation(field.type)
        annotation = Subscript(
            value=Name(id="List", ctx=Load()),
            slice=Name(id=field_type, ctx=Load()),
            ctx=Load(),
        )
        return self._construct_field(field, annotation)

    def _process_single_field(
        self, field: Field, is_optional: bool = False
    ) -> AnnAssign:
        field_type = self._annotation_generator.process_annotation(field.type)
        annotation = Name(id=field_type, ctx=Load())
        return self._construct_field(field, annotation, is_optional)


class MessageClassGenerator(DefaultMessageClassGenerator):
    def __init__(self, importer: DomesticImporter, type_mapper: TypeMapper):
        self._importer = importer
        self._type_mapper = type_mapper
        self._class_field_generator = ClassFieldGenerator(
            self._importer, self._type_mapper
        )
        self._one_of_generator = OneOfGenerator(self._class_field_generator)
