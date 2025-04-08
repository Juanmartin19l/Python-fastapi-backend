from pydantic import BaseModel

class UserCreate(BaseModel):
    name: str
    email: str
    age: int

class UserRead(BaseModel):
    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True  # Reemplazando orm_mode por from_attributes para Pydantic V2
