from typing import Annotated
from uuid import UUID

from dishka.integrations.fastapi import DishkaRoute, FromDishka
from fastapi import APIRouter, HTTPException, Path, status

from src.application.dto import NewDossierDTO
from src.application.interactors import GetDossierInteractor, NewDossierInteractor
from src.controllers.http.schemas import DossierSchema


dossier_router = APIRouter(prefix="/dossier", route_class=DishkaRoute)


@dossier_router.get("/{dossier_id:uuid}")
async def get_dossier(
    dossier_id: Annotated[UUID, Path(description="Dossier ID", title="Dossier ID")],
    interactor: FromDishka[GetDossierInteractor],
) -> DossierSchema:
    dossier_dm = await interactor(uuid=str(dossier_id))

    if not dossier_dm:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="Dossier not found"
        )

    return DossierSchema(
        first_name=dossier_dm.first_name,
        middle_name=dossier_dm.middle_name,
        last_name=dossier_dm.last_name,
        photo_url=dossier_dm.photo_url,
        phone_number=dossier_dm.phone_number,
        description=dossier_dm.description,
    )


@dossier_router.post("/")
async def new_dossier(
    first_name: str,
    middle_name: str,
    last_name: str,
    photo_url: str,
    phone_number: int,
    description: str,
    interactor: FromDishka[NewDossierInteractor],
) -> str:
    dto = NewDossierDTO(
        first_name=first_name,
        middle_name=middle_name,
        last_name=last_name,
        photo_url=photo_url,
        phone_number=phone_number,
        description=description,
    )
    uuid = await interactor(dto)
    return uuid

