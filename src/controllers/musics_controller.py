from bson import ObjectId
from flask import Blueprint, jsonify

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


# ----------
# Rotas HTTp para a nossa API
@musics_controller.route("/", methods=["GET"])
def music_index():
    musics_list = _get_all_musics()
    return jsonify(musics_list)


@musics_controller.route("/random", methods=["GET"])
def music_random():
    music = MusicModel.get_random()
    if music is None:
        return
    return jsonify(music.to_dict()), 200
