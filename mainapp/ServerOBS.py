import json
from obswebsocket import obsws, requests


class ServerOBS:
    ws = None

    @staticmethod
    def connect():
        with open('mainapp/SERVER.json', 'r', encoding='utf-8') as f:
            server_settings = json.load(f)

        host = server_settings['host']
        port = server_settings['port']
        password = server_settings['password']
        ServerOBS.ws = obsws(host=host, port=port, password=password)
        try:
            ServerOBS.ws.connect()
        except Exception:
            raise Exception("Не удалось подключиться к серверу")


    @staticmethod
    def get_scenes():
        try:
            scenes = ServerOBS.ws.call(requests.GetSceneList())
            current_scene = scenes.getCurrentScene()
        except Exception:
            raise Exception("Ошибка")

        other_scenes = []
        for scene in scenes.getScenes():
            if scene['name'] != current_scene:
                other_scenes.append(scene['name'])

        return {'current_scene': current_scene, 'other_scenes': other_scenes}

    @staticmethod
    def switch_scene(name):
        try:
            ServerOBS.ws.call(requests.SetCurrentScene(name))
        except Exception:
            raise Exception("Изменить сцену не вышло")