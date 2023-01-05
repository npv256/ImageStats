from fastapi import APIRouter
from typing import Optional

router = APIRouter()


@router.get("/groups/{status}", name="images:get_groups")
def get_groups(status: Optional[str] = None):
    pass


@router.get("/stats/", name="images:get_stats")
def get_stats(days: int):
    pass


@router.put("/id={id_}&status={status}", name="images:update_status")
def update_status(id_: str, status: str):
    pass
