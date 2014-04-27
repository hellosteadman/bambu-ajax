from django.contrib.auth.models import User
from django.test import TestCase, RequestFactory
from bambu_ajax.views import endpoint
from bambu_ajax import autodiscover

try:
    import json
except:
    from django.utils import simplejson as json

class AJAXViewTestCase(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username = 'jacob',
            email = 'jacob@_',
            password = 'top_secret'
        )

        autodiscover()

    def test_test_function(self):
        request = self.factory.get(
            '/ajax/endpoint.js?f=bambu_ajax.test.test_function'
        )

        request.user = self.user
        response = endpoint(request)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.content)
        self.assertTrue(data)
