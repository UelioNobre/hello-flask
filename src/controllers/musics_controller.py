from bson import ObjectId
from flask import Blueprint, jsonify, request

# from .status_http import StatusHttp
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
    # return jsonify(musics_list), StatusHttp.OK
    # Usando a Enum, acontece o seguinte erro:
    """
    Traceback (most recent call last):
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 2213, in __call__
    return self.wsgi_app(environ, start_response)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 2193, in wsgi_app
    response = self.handle_exception(e)
               ^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 2190, in wsgi_app
    response = self.full_dispatch_request()
               ^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 1487, in full_dispatch_request
    return self.finalize_request(rv)
           ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 1506, in finalize_request
    response = self.make_response(rv)
               ^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/flask/app.py", line 1851, in make_response
    rv.status_code = status
  File "/usr/local/lib/python3.12/site-packages/werkzeug/sansio/response.py", line 146, in status_code
    self.status = code  # type: ignore
  File "/usr/local/lib/python3.12/site-packages/werkzeug/sansio/response.py", line 155, in status
    self._status, self._status_code = self._clean_status(value)
                                      ^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/usr/local/lib/python3.12/site-packages/werkzeug/sansio/response.py", line 161, in _clean_status
    value = value.strip()
            ^^^^^^^^^^^^^
AttributeError: 'StatusHttp' object has no attribute 'strip'
    """
    return jsonify(musics_list), 200


@musics_controller.route("/random", methods=["GET"])
def music_random():
    music = MusicModel.get_random()
    if music is None:
        return
    # return jsonify(music.to_dict()), StatusHttp.OK
    # Utilizar Enum causa um erro
    return jsonify(music.to_dict()), 200


@musics_controller.route("/", methods=["POST"])
def music_post():
    new_music = MusicModel(request.json)
    new_music.save()
    # return jsonify(new_music.to_dict()), StatusHttp.CREATED
    # Utilizar Enum causa um erro
    return jsonify(new_music.to_dict()), 201
