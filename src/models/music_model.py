from .db import db
from .abstract_model import AbstractModel


class MusicModel(AbstractModel):
    __collection = db["musics"]

    def __init__(self, data: dict):
        super().__init__(data)
