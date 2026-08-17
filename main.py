from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Lead(BaseModel):
    name: str
    email: str
    city: str | None = None


@app.get("/")
def read_root():
    return {"status": "service is running"}


@app.post("/validate-lead")
def validate_lead(lead: Lead):
    errors = []

    if lead.name.strip() == "":
        errors.append("name is empty")

    if "@" not in lead.email:
        errors.append("invalid email format")

    if errors:
        return {"valid": False, "errors": errors}

    return {"valid": True, "errors": []}