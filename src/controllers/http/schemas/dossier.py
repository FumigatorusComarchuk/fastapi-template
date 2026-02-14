from pydantic import BaseModel


class DossierSchema(BaseModel):
    first_name: str
    middle_name: str
    last_name: str
    photo_url: str
    phone_number: int
    description: str

