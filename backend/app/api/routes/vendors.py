from fastapi import APIRouter, HTTPException, status

from app.schemas.vendor import Vendor, VendorCreate, VendorUpdate
from app.services.inventory import create_item, delete_item, get_item, list_items, update_item


router = APIRouter(prefix="/vendors", tags=["Vendors"])



@router.get("/", response_model=list[Vendor])
def list_vendors():
    return list_items("vendors")


@router.get("/{vendor_id}", response_model=Vendor)
def get_vendor(vendor_id: str):
    vendor = get_item("vendors", vendor_id)
    if not vendor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found")
    return vendor


@router.post("/", response_model=Vendor, status_code=status.HTTP_201_CREATED)
def create_vendor(payload: VendorCreate):
    return create_item("vendors", payload.model_dump())


@router.patch("/{vendor_id}", response_model=Vendor)
def update_vendor(vendor_id: str, payload: VendorUpdate):
    updated_vendor = update_item(
        "vendors",
        vendor_id,
        payload.model_dump(exclude_unset=True),
    )
    if not updated_vendor:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found")
    return updated_vendor


@router.delete("/{vendor_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_vendor(vendor_id: str):
    if not delete_item("vendors", vendor_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Vendor not found")