from __future__ import absolute_import
from celery import Celery

goblin_slayer = Celery( 'goblin_task',
                        broker='amqp://goblin:asdf@fumika/goblin_vhost',
                        backend='rpc://', include=[ 'goblin.task' ] )
