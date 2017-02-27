# -*- coding: utf-8 -*-


import xlwt
import uuid
from django.conf import settings


class WriteXLS(object):
    """docstring for WriteXLS"""

    def __init__(self, name, data, title):
        self.name = name
        self.data = data
        self.title = title
        # self._write_table(self.data, self.title)

    def write_table(self):
        try:
            wb = xlwt.Workbook()
            ws = wb.add_sheet('Sheet Phone')
            j = 0
            for elem in self.title:
                ws.write(0, j, elem)
                j += 1
            i = 1
            for obj in self.data:
                obj = str(obj).split(',')
                j = 0
                for elem in obj:
                    if elem == 'None':
                        elem = ' '
                    ws.write(i, j, elem.decode('utf-8'))
                    j += 1
                i += 1
            uuid_name = str(uuid.uuid1())
            path_to_file = ''.join([settings.MEDIA_ROOT,
                                   "backup_xls/", self.name, "-", uuid_name, ".xls"])
            wb.save(path_to_file)
            path_to_download_file = ''.join([settings.MEDIA_URL,
                                            "backup_xls/", self.name, "-", uuid_name, ".xls"])
            return path_to_download_file
        except:
            return None
