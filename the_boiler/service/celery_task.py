from celery import Celery
from the_boiler.webapp import celery


def make_celery(app):
    # set redis url vars
    app.config['CELERY_BROKER_URL'] = 'redis://localhost:6379/0'
    # 'REDIS_URL', 'redis://localhost:6379/0')
    app.config['CELERY_RESULT_BACKEND'] = app.config['CELERY_BROKER_URL']
    # create context tasks in celery
    celery = Celery(app.import_name, broker=app.config['CELERY_BROKER_URL'])
    celery.conf.update(app.config)
    TaskBase = celery.Task
    class ContextTask(TaskBase):
        abstract = True
        def __call__(self):
            with app.app_context():
                return TaskBase.__call__(self)
    celery.Task = ContextTask
    return celery
