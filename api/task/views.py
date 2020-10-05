# from django.shortcuts import HttpResponse
from django.http import JsonResponse

def print(request):
    # html = "<html><body>It is now</body></html>"
    # return HttpResponse(html)

    html = [
        {
            'motor' : 'supra',
            'kecepatan' : '125 km/jam'
        },
        {
            'motor' : 'beat',
            'kecepatan' : '90 km/jam'
        }
    ]
    return JsonResponse({'html':html})
