from drf_pydantic import BaseModel

from . import Message


class Update(BaseModel):
    update_id: int
    message: Message | None
