from django.http import JsonResponse


def render_json(code, data):
    return JsonResponse({
        'code': code,
        'data': data
    })