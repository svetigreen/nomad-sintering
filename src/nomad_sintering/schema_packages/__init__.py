from nomad.config.models.plugins import SchemaPackageEntryPoint
from pydantic import Field


class NewSchemaPackageEntryPoint(SchemaPackageEntryPoint):
    parameter: int = Field(0, description='Custom configuration parameter')

    def load(self):
        from nomad_sintering.schema_packages.schema_package import m_package

        return m_package


schema_package_entry_point = NewSchemaPackageEntryPoint(
    name='NewSchemaPackage',
    description='New schema package entry point configuration.',
)

class SinteringEntryPoint(SchemaPackageEntryPoint):

    def load(self):
        from nomad_sintering.schema_packages.sintering import m_package

        return m_package


sintering = SinteringEntryPoint(
    name='Sintering',
    description='Schema package for describing a sintering process.',
)
