import sqlalchemy as sa
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column

from .base import Base


class Dossier(Base):
    __tablename__ = "dossiers"

    uuid: Mapped[str] = mapped_column(
        "uuid",
        sa.Uuid,
        primary_key=True,
    )
    first_name: Mapped[str]
    middle_name: Mapped[str]
    last_name: Mapped[str]
    photo_url: Mapped[str]
    phone_number: Mapped[int] = mapped_column(sa.BigInteger)
    description: Mapped[str]
