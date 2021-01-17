import http.client

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
import json


@api_view(['GET'])
def get_todo(request):
    conn = http.client.HTTPSConnection("jsonplaceholder.typicode.com")

    conn.request("GET", "/todos")

    res = conn.getresponse()
    data = res.read()

    my_json = json.loads(data.decode("utf-8"))

    start = int(request.GET.get('start_index', 0))
    end = int(request.GET.get('end_index', 16))

    if start >= end:
        return HttpResponse('Invalid parameters!', status=400)

    titles = []

    for i in range(start, end):
        titles.append(my_json[i]['title'])

    return HttpResponse(json.dumps(titles), content_type="application/json")
