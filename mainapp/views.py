from django.shortcuts import render
from django.views import View

from rest_framework.response import Response
from rest_framework.views import APIView

from .ServerOBS import ServerOBS

# region Views
class MainAppView(View):
    template_name = 'mainapp.html'

    def get(self, request):
        ServerOBS.connect()

        context = {}
        try:
            scenes = ServerOBS.get_scenes()
            context['current_scene'] = scenes['current_scene']
            context['other_scenes'] = scenes['other_scenes']
        except Exception as e:
            context['error'] = str(e)

        return render(request, self.template_name, context=context)

    def post(self, request):
        print(request.data)

        return render(request, self.template_name)
# endregion


# region API
class MainAppAPI(APIView):

    def post(self, request):
        ServerOBS.connect()
        name_scene = request.data['name']
        try:
            ServerOBS.switch_scene(name_scene)
            scenes = ServerOBS.get_scenes()
            return Response({'Response': f'Сцена изменена на {name_scene}', 'scenes': scenes})

        except Exception as e:
            return Response({"Response": str(e)})


    def get(self, request):
        ServerOBS.connect()
        try:
            scenes = ServerOBS.get_scenes()
            return Response(scenes)
        except Exception as e:
            return Response({'Response': str(e)})
# endregion


