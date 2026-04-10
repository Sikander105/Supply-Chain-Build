from datetime import date

from app.db.session import SessionLocal
from app.models.product import Product
from app.models.purchase_order import PurchaseOrder
from app.models.shipment import Shipment
from app.models.vendor import Vendor
from app.models.warehouse import Warehouse


def run() -> None:
    with SessionLocal() as db:
        if db.query(Vendor).count() == 0:
            db.add_all(
                [
                    Vendor(id="v1", name="Acme Supplies", phone="111-1111", email="acme@example.com"),
                    Vendor(id="v2", name="Global Parts", phone="222-2222", email="global@example.com"),
                ]
            )

        if db.query(Warehouse).count() == 0:
            db.add_all(
                [
                    Warehouse(id="w1", name="Main WH", location="Dallas", capacity=1000, current_usage=300),
                    Warehouse(id="w2", name="West WH", location="Phoenix", capacity=800, current_usage=120),
                ]
            )

        if db.query(Product).count() == 0:
            db.add_all(
                [
                    Product(id="p1", name="Bolt", sku="SKU-BOLT-001", category="Hardware", stock=500, price=0.25, reorder_level=100, warehouse_id="w1", status="active"),
                    Product(id="p2", name="Nut", sku="SKU-NUT-001", category="Hardware", stock=400, price=0.20, reorder_level=100, warehouse_id="w2", status="active"),
                ]
            )

        if db.query(PurchaseOrder).count() == 0:
            db.add(
                PurchaseOrder(
                    id="po1",
                    po_number="PO-0001",
                    vendor_id="v1",
                    product_id="p1",
                    quantity=200,
                    status="Active",
                    created_date=date(2026, 4, 1),
                )
            )

        if db.query(Shipment).count() == 0:
            db.add(
                Shipment(
                    id="s1",
                    shipment_number="SHP-0001",
                    product_id="p1",
                    warehouse_id="w1",
                    quantity=150,
                    status="Received",
                    received_date=date(2026, 4, 5),
                )
            )

        db.commit()
        print("Seed complete.")


if __name__ == "__main__":
    run()