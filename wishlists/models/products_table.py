from sqlalchemy import (
    create_engine,
    Column,
    BigInteger,
    String,
    Text,
    Numeric,
    Boolean,
    TIMESTAMP,
    Integer,
    ForeignKey,
    CheckConstraint,
    Index,
    Table,
    text
)


from urllib.parse import quote_plus
from datetime import datetime
from database import Base



class Product(Base):

    __tablename__ = "products"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    name = Column(
        String(150),
        nullable=False
    )

    description = Column(
        Text
    )

    price = Column(
        Numeric(10, 2),
        nullable=False
    )

    stock = Column(
        Integer,
        nullable=False
    )

    rating = Column(
        Numeric(2, 1)
    )

    category_id = Column(
        BigInteger,
        ForeignKey("categories.id"),
        nullable=False
    )

    seller_id = Column(
        BigInteger,
        ForeignKey("users.id"),
        nullable=False
    )

    is_active = Column(
        Boolean,
        nullable=False,
        default=True
    )

    created_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.utcnow
    )

    updated_at = Column(
        TIMESTAMP,
        nullable=False,
        default=datetime.utcnow
    )

    deleted_at = Column(
        TIMESTAMP,
        nullable=True
    )

    __table_args__ = (

        CheckConstraint(
            "price >= 0",
            name="products_price_check"
        ),

        CheckConstraint(
            "stock >= 0",
            name="products_stock_check"
        ),

        CheckConstraint(
            "(rating IS NULL) OR (rating >= 0 AND rating <= 5)",
            name="chk_rating"
        ),

        Index(
            "idx_products_category_id",
            "category_id"
        ),

        Index(
            "idx_products_name",
            "name"
        ),

        Index(
            "idx_products_seller_id",
            "seller_id"
        ),
    )


