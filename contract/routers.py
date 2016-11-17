class DBRouter(object):
    """
    A router to control all database operations on models in
    the POLLS application
    """

    def db_for_read(self, model, **hints):
        """
        Point all operations on polls models to 'mktplc'
        """
        if model._meta.app_label == 'mktplc':
            return 'mktplc_db'
        return None

    def db_for_write(self, model, **hints):
        """
        Point all operations on myapp models to 'other'
        """
        if model._meta.app_label == 'mktplc':
            return 'mktplc_db'
        return None

    def allow_syncdb(self, db, model):
        """
        Make sure the 'myapp2' app only appears on the 'other' db
        """
        if db == 'cms_db':
            return model._meta.app_label == 'mktplc'
        elif model._meta.app_label == 'mktplc':
            return False
        return None
