# -*- coding: utf-8 -*-

import MySQLdb
from datetime import datetime
from django.utils import timezone
from posting.work_table import ConnectDatabases


class Active(ConnectDatabases):
    def __init__(self):
        super(Active, self).__init__()

        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword,
                                 host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            query = "SELECT value FROM Options where name='franchiseActiveTo';"
            c.execute(query)
            self.result = c.fetchone()[0]
        except:
            pass
        finally:
            c.close()
            db.close()

    def franshises(self):
        active_date = datetime.strptime(self.result, "%Y-%m-%d")
        if active_date < timezone.now():
            return False
        return True
