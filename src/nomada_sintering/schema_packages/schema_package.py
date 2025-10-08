from typing import (
    TYPE_CHECKING,
)

from nomad.config import config
from nomad.datamodel.data import Schema
from nomad.datamodel.metainfo.annotations import ELNAnnotation, ELNComponentEnum
from nomad.metainfo import Package, Quantity

if TYPE_CHECKING:
    from nomad.datamodel.datamodel import (
        EntryArchive,
    )
    from structlog.stdlib import (
        BoundLogger,
    )

m_package = Package(name='sintering')


class NewSchemaPackage(Schema):
    name = Quantity(
        type=str,
        a_eln=ELNAnnotation(component=ELNComponentEnum.StringEditQuantity)
    )
    message = Quantity(type=str)

    def normalize(self, archive: 'EntryArchive', logger: 'BoundLogger') -> None:
        super().normalize(archive, logger)

         # Konfiguration LAZY und mit **Entry-Point-ID** holen:
        cfg = None
        try:
            cfg = config.get_plugin_entry_point(
                'sintering.schema_packages:schema_package_entry_point',  # <- ID, nicht Modulpfad
                raise_not_found=False
            )
        except Exception:
            pass

        if cfg is not None and hasattr(cfg, 'parameter'):
            logger.info('NewSchema.normalize', parameter=cfg.parameter)
        else:
            logger.info('NewSchema.normalize', parameter='(no cfg)')

        self.message = f'Hello {self.name}!'


m_package.__init_metainfo__()
