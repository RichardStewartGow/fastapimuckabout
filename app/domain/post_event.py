import datetime
from pydantic import BaseModel

"""
Post for event logging, note that only the first dimension is requiured as we should be allowed to record things
atomically happening on one dimension

Likewise we dont allways need species, 2 levels of taxonomy will do at times.

Allow opts for date_created in case you want originn source to define time 

Date negation exists for the negation of event (similar to soft delete but we may want to ask about negated events)
e.g. someone liking and then unliking an event would result in the original event being negated
"""
class PostEvent(BaseModel):
    dim_id_1: int
    dim_type_1: str
    dim_id_2: int | None
    dim_type_2: str | None
    dim_id_3: int | None
    dim_type_3: str | None
    ecategory: str
    etype: str
    especies: str | None
    date_negated: datetime.datetime | None