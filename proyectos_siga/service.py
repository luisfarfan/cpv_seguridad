from django.conf import settings
import json
from request

class App1Service(object):
    @staticmethod
    def do_create_person(**params):
        url = '%s/%s' % (settings.HOST_API_APP1, 'service1/person/create')
        response = request.post(url, data=params)

        if response.status = 200:
            return json.loads(response.data)
        
        return False

        # 
            # ok
