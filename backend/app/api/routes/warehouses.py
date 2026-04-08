from fastapi import APIRouter, HTTPException, status

from app.schemas.warehouse import Warehouse, WarehouseCreate, WarehouseUpdate
from app.services.inventory import create_item, delete_item, get_item, list_items, update_item


router = APIRouter(prefix="/warehouses", tags=["Warehouses"])



@router.get("/", response_model=list[Warehouse])
def list_warehouses():
    return list_items("warehouses")


@router.get("/{warehouse_id}", response_model=Warehouse)
def get_warehouse(warehouse_id: str):
    warehouse = get_item("warehouses", warehouse_id)
    if not warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")
    return warehouse


@router.post("/", response_model=Warehouse, status_code=status.HTTP_201_CREATED)
def create_warehouse(payload: WarehouseCreate):
    return create_item("warehouses", payload.model_dump())


@router.patch("/{warehouse_id}", response_model=Warehouse)
def update_warehouse(warehouse_id: str, payload: WarehouseUpdate):
    updated_warehouse = update_item(
        "warehouses",
        warehouse_id,
        payload.model_dump(exclude_unset=True),
    )
    if not updated_warehouse:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")
    return updated_warehouse


@router.delete("/{warehouse_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_warehouse(warehouse_id: str):
    if not delete_item("warehouses", warehouse_id):
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Warehouse not found")