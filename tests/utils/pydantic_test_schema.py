from pydantic import BaseModel, Field

class TestSchema(BaseModel):
    name: str = Field(...)
    id: int = Field(...)
    cellphone: str = Field(...)