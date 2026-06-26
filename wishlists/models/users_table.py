from datetime import datetime
from sqlalchemy import (
    Column,
    BigInteger,
    String,
    Text,
    Boolean,
    Numeric,
    TIMESTAMP
)

from database import Base


class User(Base):

    __tablename__ = "users"

    id = Column(
        BigInteger,
        primary_key=True,
        autoincrement=True
    )

    role = Column(
        String(20),
        nullable=False
    )

    full_name = Column(
        String(150),
        nullable=False
    )

    email = Column(
        String(150),
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String(255),
        nullable=False
    )

    phone = Column(
        String(20)
    )

    shop_name = Column(
        String(150)   # FIXED
    )

    shop_description = Column(
        Text
    )

    rating = Column(
        Numeric(2, 1)
    )

    is_active = Column(
        Boolean,
        default=True
    )

    created_at = Column(
        TIMESTAMP,
        default=datetime.utcnow
    )

    updated_at = Column(
        TIMESTAMP,
        default=datetime.utcnow
    )

    deleted_at = Column(
        TIMESTAMP,
        nullable=True
    )




