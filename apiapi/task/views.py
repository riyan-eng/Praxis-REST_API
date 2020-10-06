# from django.shortcuts import HttpResponse
from django.http import JsonResponse
from tastypie.resources import ModelResource
from . models import motor

# def index(request):
    # html = "<html><body>It is now</body></html>"
    # return HttpResponse(html)

    # html = [
    #     {
    #         'motor' : 'supra',
    #         'kecepatan' : '125 km/jam'
    #     },
    #     {
    #         'motor' : 'beat',
    #         'kecepatan' : '90 km/jam'
    #     }
    # ]
    # return JsonResponse({'html': html})
    # data = motor.objects.all()

    # simpan = []
    # for x in data:
    #     simpan.append({
    #         'merek': x.merek,
    #         'kecepatan': x.kecepatan,
    #     })

    # return JsonResponse({
    #     'data': simpan
    # }, safe=False)
class NoteResource(ModelResource):
    class Meta:
        queryset = motor.objects.all()
        resource_name = 'motor'
