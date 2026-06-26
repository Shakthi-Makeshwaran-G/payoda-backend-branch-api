from pydantic import BaseModel 
from datetime import datetime 

class WishlistCreate(BaseModel):

    user_id : int
    product_id : int


class WishlistUpdate(BaseModel):

    user_id : int
    product_id : int


class WishlistResponse(BaseModel):

    id : int
    user_id : int
    product_id : int
    created_at : datetime

    class Config:
        from_attributes = True