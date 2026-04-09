from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import HTMLResponse

from app.api.routes.health import router as health_router
from app.api.routes.products import router as products_router
from app.api.routes.purchase_orders import router as purchase_orders_router
from app.api.routes.reports import router as reports_router
from app.api.routes.shipments import router as shipments_router
from app.api.routes.vendors import router as vendors_router
from app.api.routes.warehouses import router as warehouses_router


app = FastAPI(
    title="Supply Chain API",
    version="1.0.0",
    redoc_url=None,     # disable default redoc so we can fully customize it
)


app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    return {"message": "Supply Chain API running"}


@app.get("/redoc", include_in_schema=False, response_class=HTMLResponse)
def custom_redoc():
    return HTMLResponse(
        """
        <!doctype html>
        <html>
          <head>
            <title>Supply Chain API Docs</title>
            <meta charset="utf-8" />
            <meta name="viewport" content="width=device-width, initial-scale=1" />
            <style>
              body { margin: 0; background: #f8fafc; }
              .topbar {
                background: linear-gradient(90deg, #0f766e, #2563eb);
                color: white;
                font-family: Inter, Segoe UI, Arial, sans-serif;
                padding: 12px 18px;
                font-weight: 700;
                letter-spacing: 0.2px;
              }
            </style>
          </head>
          <body>
            <div class="topbar">Supply Chain API — Reference</div>
            <div id="redoc"></div>

            <script src="https://cdn.jsdelivr.net/npm/redoc@next/bundles/redoc.standalone.js"></script>
            <script>
              Redoc.init("/openapi.json", {
                hideHostname: true,
                theme: {
                  colors: {
                    primary: { main: "#0f766e" },
                    success: { main: "#16a34a" },
                    warning: { main: "#f59e0b" }
                  },
                  typography: {
                    fontFamily: "Inter, Segoe UI, Arial, sans-serif",
                    headings: { fontFamily: "Inter, Segoe UI, Arial, sans-serif" }
                  }
                }
              }, document.getElementById("redoc"));
            </script>
          </body>
        </html>
        """
    )


app.include_router(health_router, prefix="/api")
app.include_router(products_router, prefix="/api")
app.include_router(vendors_router, prefix="/api")
app.include_router(warehouses_router, prefix="/api")
app.include_router(purchase_orders_router, prefix="/api")
app.include_router(shipments_router, prefix="/api")
app.include_router(reports_router, prefix="/api")