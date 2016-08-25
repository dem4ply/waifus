from __future__ import absolute_import
from celery import Celery

app = Celery( 'goblin_task',
              broker='amqp://goblin:asdf@melchor/goblin_vhost',
              backend='rpc://',
              include=[ 'goblin.task' ] )
