from ..core.database import Base

from typing import List
from datetime import datetime

from sqlalchemy import func
from sqlalchemy import ForeignKey, String, Table, Column
from sqlalchemy.orm import Mapped, relationship, mapped_column


cart_association_table = Table(
    "cart",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("board_id", ForeignKey("board_games.id", ondelete="CASCADE"), primary_key=True)
)

wishlist_association_table = Table(
    "wishlist",
    Base.metadata,
    Column("user_id", ForeignKey("users.id", ondelete="CASCADE"), primary_key=True),
    Column("board_game_id",
    ForeignKey("board_games.id", ondelete="CASCADE"), primary_key=True)
)

class Users(Base):
    __tablename__ = "users"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(30), unique=True)
    email: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str] = mapped_column(String(255))
    created_at: Mapped[datetime] = mapped_column(server_default=func.now())

    cart_games: Mapped[List["BoardGames"]] = relationship(
        secondary=cart_association_table,
        back_populates="in_carts_of_users"
    )

    wishlist_games: Mapped[List["BoardGames"]] = relationship(
        secondary=wishlist_association_table,
        back_populates="in_wishlists_of_users"
    )

class BoardGames(Base):
    __tablename__ = "board_games"

    id: Mapped[str] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(100))
    price: Mapped[float]
    description: Mapped[str] = mapped_column(String(1024))

    in_carts_of_users: Mapped[List["Users"]] = relationship(
        secondary=cart_association_table,
        back_populates="cart_games"
    )

    in_wishlists_of_users: Mapped[List["Users"]] = relationship(
        secondary=wishlist_association_table,
        back_populates="wishlist_games"
    )