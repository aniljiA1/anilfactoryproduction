from fastapi import APIRouter

router = APIRouter(prefix="/workstations", tags=["Workstations"])

@router.get("/")
def list_workstations():
    return {"message": "Workstation metrics can be added similarly"}
