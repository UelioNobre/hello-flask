from .db import db
from .abstract_model import AbstractModel
import random


class MusicModel(AbstractModel):
    _collection = db["musics"]

    def __init__(self, data: dict):
        super().__init__(data)

    @classmethod
    def get_random(cls):
        data = cls._collection.find()
        if data is None:
            return

        return random.choice(data)

    def to_dict(self):
        return {
            "_id": str(self.data["_id"]),
            "music": self.data["music"],
        }
