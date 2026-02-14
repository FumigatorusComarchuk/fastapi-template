from dataclasses import dataclass


@dataclass(slots=True)
class Dossier:
    uuid: str
    first_name: str
    middle_name: str
    last_name: str
    photo_url: str
    phone_number: int
    description: str
