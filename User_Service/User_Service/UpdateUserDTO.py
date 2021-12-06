from pydantic import BaseModel


class UpdateUserDTO(BaseModel):
    name: str
