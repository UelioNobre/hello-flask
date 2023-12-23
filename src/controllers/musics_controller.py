from bson import ObjectId
from flask import Blueprint

from models.music_model import MusicModel

# Definindo o controller para musicas
musics_controller = Blueprint("musics", __name__)


# ----------
# Funções protegidas
def _get_all_musics():
    musics = MusicModel.find()
    return [music.to_dict() for music in musics]


def _get_music(id: str):
    music = MusicModel.find_one({"_id": ObjectId(id)})
    return music
