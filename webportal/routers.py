class SysproWebRouter(object):

    def db_for_read(model, **hints):
        if model._meta.app_label == 'syspro_web':
            return 'syspro'
        elif model._meta.app_label == 'orders':
            return 'default'
        return None

    def db_for_write(model, **hints):
        if model._meta.app_label == 'syspro_web':
            return None
        elif model._meta.app_label == 'orders':
            return 'default'
        return None