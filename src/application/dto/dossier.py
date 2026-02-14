from dataclasses import dataclass


@dataclass(slots=True)
class NewDossierDTO:
    first_name: str
    middle_name: str
    last_name: str
    photo_url: str
    phone_number: int
    description: str

