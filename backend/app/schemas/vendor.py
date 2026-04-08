from typing import Optional

from pydantic import BaseModel, Field


class VendorBase(BaseModel):
    name: str = Field(..., min_length=1)

    contactPerson: str = Field(..., min_length=1)

    phone: str = Field(..., min_length=1)

    email: str = Field(..., min_length=1)


class VendorCreate(VendorBase):
    pass


class VendorUpdate(BaseModel):
    name: Optional[str] = None
    contactPerson: Optional[str] = None
    phone: Optional[str] = None
    email: Optional[str] = None


class Vendor(VendorBase):
    id: str