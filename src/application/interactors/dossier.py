from src.application.interfaces import DossierReader, DossierSaver, DBSession, UUIDGenerator
from src.application.dto import NewDossierDTO
from src.domain.dossier import Dossier


class GetDossierInteractor:
    def __init__(
        self,
        dossier_gateway: DossierReader,
    ) -> None:
        self._dossier_gateway = dossier_gateway

    async def __call__(self, uuid: str) -> Dossier | None:
        return await self._dossier_gateway.read_by_uuid(uuid)


class NewDossierInteractor:
    def __init__(
        self,
        db_session: DBSession,
        dossier_gateway: DossierSaver,
        uuid_generator: UUIDGenerator,
    ) -> None:
        self._db_session = db_session
        self._dossier_gateway = dossier_gateway
        self._uuid_generator = uuid_generator

    async def __call__(self, dto: NewDossierDTO) -> str:
        uuid = str(self._uuid_generator())
        dossier = Dossier(
            uuid=uuid,
            first_name=dto.first_name,
            middle_name=dto.middle_name,
            last_name=dto.last_name,
            photo_url=dto.photo_url,
            phone_number=dto.phone_number,
            description=dto.description,
        )

        await self._dossier_gateway.save(dossier)
        await self._db_session.commit()
        return uuid

