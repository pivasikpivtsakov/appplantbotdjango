from pydantic import BaseModel


class User(BaseModel):
    id: int
    is_bot: bool
    first_name: str
    last_name: str | None
    username: str | None
    language_code: str | None
    is_premium: bool | None
    added_to_attachment_menu: bool | None
    can_join_groups: bool | None
    can_read_all_group_messages: bool | None
    supports_inline_queries: bool | None
