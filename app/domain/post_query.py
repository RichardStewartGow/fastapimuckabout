from pydantic import BaseModel

class PostQuery(BaseModel):
    query: str
    qtype: str
    payload: list = []