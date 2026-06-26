from sqlalchemy import (
    create_engine,
    Column,
    BigInteger,
    TIMESTAMP,
    UniqueConstraint, 
    ForeignKey
)

from sqlalchemy.orm import declarative_base, Session
from urllib.parse import quote_plus
from datetime import datetime
from faker import Faker
import random
from sqlalchemy import Table
from database import Base


class Wishlist(Base):

    __tablename__ = "wishlists"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    user_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    product_id = Column(
        BigInteger,
        ForeignKey("products.id"),
        nullable=False
    )

    created_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.utcnow
    )

    __table_args__ = (
        UniqueConstraint(
            "user_id",
            "product_id",
            name="uq_wishlist_user_product"
        ),
    )


