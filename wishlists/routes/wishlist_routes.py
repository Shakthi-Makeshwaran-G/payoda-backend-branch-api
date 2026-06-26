from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from typing import List
from database import get_db

from controllers import wishlist_controller

from schemas.wishlist_schema import(
    WishlistCreate,
    WishlistUpdate, 
    WishlistResponse
)

router = APIRouter(
    prefix = "/wishlist", 
    tags = ["Wishlist"]
)


@router.post(
    "/",
    response_model = WishlistResponse
)
def create_wishlist(
    wishlist : WishlistCreate, 
    db : Session = Depends(get_db)
):
    return wishlist_controller.create_wishlists(
        db, wishlist
    )


@router.get(
    "/",
    response_model = List[WishlistResponse]
)
def get_all_wishlists(
    db : Session = Depends(get_db), 
    skip : int = 0, 
    limit : int = 10
):
    
    return wishlist_controller.get_all_wishlists(
        db, 
        skip, 
        limit
    )

@router.get(
    "/{wishlist_id}",
    response_model = WishlistResponse
)
def get_wishlist_by_id(
    wishlist_id : int, 
    db : Session = Depends(get_db)
):
    
    return wishlist_controller.get_wishlist_by_id(
        wishlist_id, 
        db
    )


@router.put(
    "/{wishlist_id}",
    response_model = WishlistResponse
)
def update_wishlist(
    wishlist_id : int, 
    wishlist : WishlistUpdate, 
    db : Session = Depends(get_db)
):
    
    return wishlist_controller.update_wishlist(
        wishlist_id, 
        wishlist, 
        db
    )


@router.delete(
    "/{wishlist_id}"
)
def delete_wishlist(
    wishlist_id : int, 
    db : Session = Depends(get_db)
):
    
    return wishlist_controller.delete_wishlist(
        wishlist_id, 
        db
    )


