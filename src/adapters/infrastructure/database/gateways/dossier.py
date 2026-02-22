from typing import List
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import text

from src.application.interfaces import DossierReader, DossierSaver
from src.domain.dossier import Dossier


class DossierGateway(
    DossierReader,
    DossierSaver,
):
    def __init__(self, session: AsyncSession):
        self._session = session

    async def read_by_uuid(self, uuid: str) -> Dossier | None:
        query = text("SELECT * FROM dossiers WHERE uuid = :uuid")
        result = await self._session.execute(
            statement=query,
            params={"uuid": uuid},
        )
        row = result.fetchone()
        if not row:
            return None
        return Dossier(
            uuid=row.uuid,
            first_name=row.first_name,
            middle_name=row.middle_name,
            last_name=row.last_name,
            photo_url=row.photo_url,
            phone_number=row.phone_number,
            description=row.description,
        )

    async def save(self, dossier: Dossier) -> None:
        query = text(
            "INSERT INTO dossiers (uuid, first_name, middle_name, last_name, photo_url, phone_number, description) VALUES (:uuid, :first_name, :middle_name, :last_name, :photo_url, :phone_number, :description)"
        )
        await self._session.execute(
            statement=query,
            params={
                "uuid": dossier.uuid,
                "first_name": dossier.first_name,
                "middle_name": dossier.middle_name,
                "last_name": dossier.last_name,
                "photo_url": dossier.photo_url,
                "phone_number": dossier.phone_number,
                "description": dossier.description,
            },
        )

    async def get_all(self) -> List[Dossier] | List:
        query = text("SELECT * FROM dossiers")
        result = await self._session.execute(query)
        rows = result.fetchall()
        return [
            Dossier(
                uuid=row.uuid,
                first_name=row.first_name,
                middle_name=row.middle_name,
                last_name=row.last_name,
                photo_url=row.photo_url,
                phone_number=row.phone_number,
                description=row.description,
            )
            for row in rows
        ]
