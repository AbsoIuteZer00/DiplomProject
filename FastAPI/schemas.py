from pydantic import BaseModel


class CompanyCreate(BaseModel):
    company: str
    name: str
    email: str
    address: str
    phone: str
    description: str


class CompanyUpdate(BaseModel):
    company: str
    name: str
    email: str
    address: str
    phone: str
    description: str
