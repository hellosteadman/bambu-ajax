from bambu_ajax import site
from django.http import HttpResponse, HttpResponseBadRequest
from django.template.response import TemplateResponse

try:
    import json
except:
    from django.utils import simplejson as json

def utility(request):
    return TemplateResponse(
        request,
        'ajax/utils.js',
        {
        },
        content_type = 'text/javascript'
    )

def endpoint(request):
    if not 'f' in request.GET:
        return HttpResponse(
            json.dumps(
                {
                    'error': 'Function name not specified in f argument'
                }
            ),
            content_type = 'application/json'
        )

    kwargs = {}
    callback = None
    for key, value in request.GET.items():
        if key == 'f':
            funchash = value
        elif key == 'callback':
            callback = value
        elif key.startswith('_'):
            continue
        else:
            kwargs[key] = value

    if funchash in site._registry:
        response = site._registry[funchash](request, **kwargs)

        if isinstance(response, HttpResponse):
            return response

        if callback:
            response = '%s(%s)' % (
                callback, json.dumps(response)
            )
        else:
            response = json.dumps(response)

        return HttpResponse(
            response,
            content_type = 'application/json'
        )

    return HttpResponseBadRequest(
        json.dumps(
            {
                'error': 'Function not found'
            }
        ),
        content_type = 'application/json'
    )
