from goblin.celery import goblin_slayer

import requests
import json

@goblin_slayer.task
def save_newspaper( item ):
    str_item = json.dumps( item )
    response = requests.post( 'http://django/crunchiroll/newspaper/',
                              headers={ 'content-type': 'application/json' },
                              data=str_item )
    return response.status_code == 204
