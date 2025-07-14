from fastapi import FastAPI

from routes.bogie_checksheet import router as bogie_form_router  # ✅ Make sure this file exists

app = FastAPI(
    title="Bogie Checksheet API",
    version="1.0.0",
    description="API for submitting bogie inspection checksheet data"
)

app.include_router(bogie_form_router, prefix="/api/forms", tags=["Bogie Checksheet"])
