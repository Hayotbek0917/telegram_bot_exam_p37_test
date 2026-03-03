from sqlalchemy import String, Integer
from sqlalchemy.orm import mapped_column, Mapped

from models.base import CreatedBaseModel


class Film(CreatedBaseModel):
    name: Mapped[str] = mapped_column(String(255))
    rating: Mapped[int] = mapped_column(Integer, nullable=True)
    description: Mapped[str] = mapped_column(String, nullable=True)
    release_year: Mapped[int] = mapped_column(Integer, nullable=True)

    def __str__(self):
        return f"{self.name}"

    def __repr__(self):
        return f"{self.name}"
