from sqlalchemy.orm import Session
from fastapi import HTTPException

from fastapi import HTTPException
from sqlalchemy.orm import Session

from models import (
    User,
    Product,
    Wishlist
)

from schemas import (
    WishlistCreate,
    WishlistUpdate
)

def create_wishlist(
        db : Session, 
        wishlist : WishlistCreate
):
    

    user = db.query(User).filter(
        User.id == wishlist.user_id
    ).first()

    if user is None:
        raise HTTPException(
            status_code = 404, 
            detail = "User Not Found!"
        )
    

    product = db.query(Product).filter(
        Product.id == wishlist.product_id
    ).first()

    if product is None:
        raise HTTPException(
            status_code = 404, 
            detail = "Product Not Found!"
        )
    
    existing = (
    db.query(Wishlist)
    .filter(
        Wishlist.user_id == wishlist.user_id,
        Wishlist.product_id == wishlist.product_id
    )
    .first()
)

    if existing :
        raise HTTPException(
            status_code = 409, 
            detail = "Product already exists in the wishlist"
        )


    new_wishlist = Wishlist(
        user_id = wishlist.user_id, 
        product_id = wishlist.product_id
    )

    db.add(new_wishlist)

    db.commit()

    db.refresh(new_wishlist)

    return new_wishlist


def get_all_wishlists(
    db: Session,
    skip: int = 0,
    limit: int = 10
):

    return (
        db.query(Wishlist)
        .order_by(Wishlist.created_at.desc())
        .offset(skip)
        .limit(limit)
        .all()
    )

def get_wishlist_by_id(
        wishlist_id : int, 
        db : Session
):
    
    wishlist = (
        db.query(Wishlist)
        .filter(
            Wishlist.id == wishlist_id
        )
        .first()
    )

    if wishlist is None:
        raise HTTPException(
            status_code = 404, 
            detail = "Wishlist item not found"
        )
    
    return wishlist

def update_wishlist(
        wishlist_id : int, 
        wishlist_data : WishlistUpdate, 
        db : Session
):
    wishlist = (
        db.query(Wishlist)
        .filter(Wishlist.id == wishlist_id)
        .first()
    )

    if wishlist is None:
        raise HTTPException(
            status_code = 404, 
            detail = "Wishlist item not found"
        )
    
    user = (db.query(Wishlist).filter(
        User.id == wishlist_data.user_id
    ).first()
    )

    if user is None:
        raise HTTPException(
            status_code = 404, 
            detail = "User not found!"
        )


    product = (
        db.query(Product)
        .filter(Product.id == wishlist_data.product_id)
        .first()
    )

    if product is None:
        raise HTTPException(
            status_code = 404, 
            detail = "Product not found"
        )
    
    duplicate = (
        db.query(Wishlist)
        .filter(
            Wishlist.user_id == wishlist_data.user_id, 
            Wishlist.product_id == wishlist_data.product_id, 
            Wishlist.id != wishlist_id
        )
        .first()
    )

    if duplicate:
        raise HTTPException(
            status_code = 404, 
            detail = "Wishlist already exists!"
        )
    
    wishlist.user_id = wishlist_data.user_id
    wishlist.product_id = wishlist_data.product_id

    db.commit()
    db.refresh(wishlist)

    return wishlist

def delete_wishlist(
        wishlist_id : int, 
        db : Session
):
    
    wishlist = (
        db.query(Wishlist)
        .filter(Wishlist.id == wishlist_id)
        .first()
    )

    if wishlist is None:
        raise HTTPException(
            status_code = 404, 
            detail = "Wishlist item not found"
        )
    
    db.delete(wishlist)
    db.commit()

    return {
        "message" : "Wishlist item deleted successfully!"
    }
