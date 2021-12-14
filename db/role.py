import sqlalchemy
from .base import metadata

role = sqlalchemy.Table(
    "role",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True, autoincrement=True, unique=True),
    sqlalchemy.Column("name", sqlalchemy.String),
)