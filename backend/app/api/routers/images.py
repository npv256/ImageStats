from fastapi import APIRouter, HTTPException
from typing import Optional
from app.bl.images.get_groups import get_groups as get_groups_bl
from app.bl.images.get_stats import get_stats as get_stats_bl
from app.bl.images.update_status import update_status as update_status_bl
from app.models.models import StatusType
from starlette.status import HTTP_422_UNPROCESSABLE_ENTITY, HTTP_500_INTERNAL_SERVER_ERROR
from typing import List, Dict
from app.models.models import ImageGroupBase

router = APIRouter()


@router.get("/groups/", name="images:get_groups")
def get_groups(status: Optional[str] = None, page: Optional[int] = 1, page_size: Optional[int] = 10) \
        -> List[ImageGroupBase]:
    if status and status not in [e.value for e in StatusType]:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Incorrect status")

    try:
        return get_groups_bl(status=status, page=page, page_size=page_size)
    except Exception:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Ops.. try later")


@router.get("/stats/", name="images:get_stats")
def get_stats(days: Optional[int] = None) -> Dict:
    try:
        return get_stats_bl(days=days)
    except Exception:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Ops.. try later")


@router.put("/id={id_}&status={status}", name="images:update_status")
def update_status(id_: str, status: str) -> str:
    if not id_ or not status or status not in [e.value for e in StatusType]:
        raise HTTPException(status_code=HTTP_422_UNPROCESSABLE_ENTITY, detail="Incorrect params")

    try:
        return update_status_bl(id_=id_, status=status)
    except Exception:
        raise HTTPException(status_code=HTTP_500_INTERNAL_SERVER_ERROR, detail="Ops.. try later")
