from pydantic import BaseModel
from typing import Optional



class PaginationSchema(BaseModel):
    current_page : Optional[int] = 1
    per_page : Optional[int] = 0
    total_pages : Optional[int] = 0
    total_records : Optional[int] = 0
