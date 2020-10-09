# from django.shortcuts import HttpResponse
from django.http import JsonResponse
import json
from django.forms.models import model_to_dict
from . models import motor

def index(request):
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
    data = motor.objects.all()

    simpan = []
    for x in data:
        simpan.append({
            'merek': x.merek,
            'kecepatan': x.kecepatan,
        })

    return JsonResponse({
        'data': simpan
    }, safe=False)

def create(request):
    if request.method == 'POST':
        data_byte = request.body
        data_string = str(data_byte, 'utf-8')
        data = json.loads(data_string)

        Motor = motor.objects.create(merek=data['merek'], kecepatan=data['kecepatan'])
        return JsonResponse({
            'data': model_to_dict(Motor),
        })

def detail(request, id):
    if request.method == 'GET':
        Motor = motor.objects.filter(pk=id).first()
        return JsonResponse({
            'data': model_to_dict(Motor),
        })
def delete(request, id):
    if request.method == 'DELETE':
        Motor = motor.objects.filter(pk=id).delete()
        return JsonResponse({
            'msg': 'data has been delete'
        })

def update(request, id):
    if request.method == 'PUT':
        data_byte = request.body
        data_string = str(data_byte, 'utf-8')
        data = json.loads(data_string)

        Motor = motor.objects.filter(pk=id).update(merek=data['merek'], kecepatan=data['kecepatan'])
        Motor = motor.objects.filter(pk=id).first()

        return JsonResponse({
            'data': model_to_dict(Motor),
        })