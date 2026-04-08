from typing import Optional

from pydantic import BaseModel, Field


class WarehouseBase(BaseModel):
    name: str = Field(..., min_length=1)

    location: str = Field(..., min_length=1)

    capacity: int = Field(..., ge=0)

    currentUsage: int = Field(..., ge=0)


class WarehouseCreate(WarehouseBase):
    pass


class WarehouseUpdate(BaseModel):
    name: Optional[str] = None
    location: Optional[str] = None
    capacity: Optional[int] = Field(default=None, ge=0)
    currentUsage: Optional[int] = Field(default=None, ge=0)


class Warehouse(WarehouseBase):
    id: str