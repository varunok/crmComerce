# -*- coding: utf-8 -*-


import os
import shutil
import uuid
import MySQLdb
import datetime
from django.conf import settings
from setting_globall.models import Franshise
from facility.models import ImagesFacility
from watermark.wm import AddWatermark
from django.utils import timezone, dateformat
from watermark.models import Watermark
from setting_globall.models import Subscribe


class ConnectDatabases(object):
    """docstring for ConnectDatabases"""
    def __init__(self):
        self.franshise = Franshise.objects.values()
        self.franshise_colaps = self.franshise[0]['franshise'].replace('.', '').replace('-', '')
        if settings.DATABASES_POST['DATABASE']:
            DATABASE = settings.DATABASES_POST['DATABASE']
        else:
            DATABASE = ''.join(['image20_', self.franshise_colaps])
        self.textusername = settings.DATABASES_POST['USER']
        self.textpassword = settings.DATABASES_POST['PASS']
        self.texthostname = settings.DATABASES_POST['HOST']
        self.database = DATABASE


class SavePhoto(ConnectDatabases):
    """docstring for SavePhoto"""
    def __init__(self, objectId, objectCode, districtId):
        super(SavePhoto, self).__init__()
        self.objectId = objectId
        self.objectCode = objectCode
        self.districtId = districtId

        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            self.query = "INSERT INTO Object_Photo_Business (objectId, objectCode, photo, districtId) VALUES (%s, %s, %s, %s)"
            self.values = self._get_images()
            c.executemany(self.query, self.values)
        except:
            pass
        finally:
            c.close()
            db.close()

    def _get_images(self):
        self.abs_path = '/'.join(os.getcwd().split('/')[0:5])
        dir_to_photo = ''.join([self.abs_path, '/', self.franshise[0]['franshise'], '/data/object/live/', str(self.objectId), '/'])
        try:
            os.makedirs(dir_to_photo)
        except:
            try:
                list_file = os.listdir(dir_to_photo)
                for ele in list_file:
                    os.remove(''.join((dir_to_photo, ele)))
            except:
                pass
        self.images_list = []
        images = ImagesFacility.objects.filter(album=str(self.objectCode[1:]))
        for ele in images:
            img_to = self._copy_image(ele.image).split('/')
            img_to = img_to[-2]+'/'+img_to[-1]
            self.images_list.append((self.objectId, self.objectCode, img_to, self.districtId))
        return self.images_list

    def _copy_image(self, img):
        img_from = ''.join([os.getcwd(), '/media/', str(img)])
        img_to = ''.join([self.abs_path, '/', self.franshise[0]['franshise'],
                          '/data/object/live/', str(self.objectId), '/', str(uuid.uuid1()), '.jpg'])
        on_off, create = Watermark.objects.get_or_create(id=1)
        if on_off.on_off:
            AddWatermark(img_from, img_to)
        else:
            shutil.copy2(img_from, img_to)
        return img_to


class District(ConnectDatabases):
    """docstring for GetDistrict"""
    def __init__(self, arg=None):
        super(District, self).__init__()
        self.arg = arg

        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            query = "SELECT * FROM District"
            c.execute(query)
            self.data = c.fetchall()
        except:
            pass
        finally:
            c.close()
            db.close()
        
    def get_district(self):
        return self.data


class SearchData(ConnectDatabases):
    isFind = False
    def __init__(self, data):
        super(SearchData, self).__init__()
        self.code = data
        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            query = "SELECT id FROM Object_Business WHERE code= '%s'" % 'K' + str(self.code)
            c.execute(query)
            self.data = c.fetchall()
            self._isFind()
        except:
            pass
        finally:
            c.close()
            db.close()

    def _isFind(self):
        if self.data:
            self.isFind = True


class InsertData(ConnectDatabases):
    isPost = True

    def __init__(self, data):
        super(InsertData, self).__init__()
        self.data = data
        subscribe, created = Subscribe.objects.get_or_create(id=1)

        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            query = "INSERT INTO Object_Business (code, title, operationType, " \
                    "description, address, type, districtId, floor, square, " \
                    "priceUSD, price, contactPerson, contactPhone, video, panoramaCode," \
                    " rieltorId, updateDate, position, enter)" \
                    "VALUES ('{0}', '{1}', '{2}', '{3}', '{5}', '{6}', '{7}', '{8}', '{9}', '{10}', '{13}', '{14}', '{15}', '{16}', '{17}', '{18}', '{19}', '{20}', '{21}')" \
                .format('K' + str(self.data.id),
                        self._get_title(unicode.encode(unicode(self.data.title), "cp1251")),
                        self._get_operationType(self.data.list_operations.all()),
                        self._get_room('pass'),
                        unicode.encode(unicode(self.data.comment), "cp1251"),
                        unicode.encode(unicode(self.data.street_obj), "cp1251"),
                        self._get_type(self.data.type_facilit_id),
                        self._get_district_id(self.data.district_obj),
                        self._get_floor(self.data.number_of_storeys),
                        self._get_total_area(self.data.footage),
                        self._get_floors_up('pass'),
                        self._get_rooms(self.data.rooms),
                        self._get_price_bay(self.data.price_bay),
                        self._get_price_month(self.data.price_month),
                        self._get_name_owner(unicode.encode(unicode(subscribe.name), "cp1251")),
                        self._get_phone_owner(unicode.encode(unicode(subscribe.phone), "cp1251")),
                        self._youtube_code(self._get_youtube(unicode.encode(unicode(self.data.youtube), "cp1251"))),
                        self._panorama_code(self._get_panorama(unicode.encode(unicode(self.data.panorama), "cp1251"))),
                        self._get_riltorId(),
                        self._updateDate(),
                        self._get_position(self.data.location.id),
                        self._get_enter(self.data.entrance.id))
            c.execute(query)
            id_d = u'K' + str(self.data.id)
            query = "SELECT id FROM Object_Business WHERE code='%s'" % id_d
            c.execute(query)
            self.id_obj = c.fetchone()[0]
            SavePhoto(self.id_obj, id_d, self._get_district_id(self.data.district_obj))
            # c.commit()
        except:
            isPost = False
        finally:
            c.close()
            db.close()

    def _youtube_code(self, code):
        if 'iframe' in code:
            return code
        iframe = '<iframe width="560" height="315" src="https://www.youtube.com/embed/%s" frameborder="0" allowfullscreen></iframe>'
        code = code.split('/')[-1]
        if '=' in code:
            code = code.split('=')[-1]
        code = iframe % code
        if code:
            return code
        else:
            return ''

    def _panorama_code(self, code):
        if 'yandex' in code:
            code = code.replace('690%2C495', '490%2C335')
            return code
        panorama = '<iframe %s width="490" height="335" frameborder="0" style="border:0" allowfullscreen=""></iframe>'
        codes = code.split(' ')
        for src in codes:
            if 'src' in src:
                src = panorama % src
                return src
        return ''

    def _updateDate(self):
        return timezone.now() + datetime.timedelta(days=10)

    def _get_riltorId(self):
        return 0

    def _get_youtube(self, data):
        return self._return_str(data)

    def _get_phone_owner(self, data):
        return self._return_str(data)

    def _get_name_owner(self, data):
        return self._return_str(data)

    def _get_price_month(self, data):
        return self._return_int(data)

    def _get_price_bay(self, data):
        return self._return_int(data)

    def _get_rooms(self, data):
        return self._return_int(data)

    def _get_floors_up(self, data):
        return self._return_int(data)

    def _get_total_area(self, data):
        return self._return_int(data)

    def _get_floor(self, data):
        return self._return_int(data)

    def _get_room(self, data):
        return self._return_int(data)

    def _get_title(self, data):
        return self._return_str(data)

    def _get_panorama(self, data):
        return self._return_str(data)

    def _return_str(self, data):
        if data:
            return data
        else:
            return ' '

    def _return_int(self, data):
        if data:
            return data
        else:
            return 0

    def _get_district_id(self, data):
        list_district = District().get_district()
        for elem in list_district:
            if str(data) in elem:
                return elem[0]
        else:
            return list_district[0][0]

    def _get_enter(self, data):
        if data == 1:
            return 1
        elif data == 2:
            return 3
        elif data == 3:
            return 2
        else:
            return 1

    def _get_position(self, data):
        if data == 1:
            return 1
        elif data == 2:
            return 3
        elif data == 3:
            return 2
        else:
            return 3

    def _get_type(self, data):
        if data == 1:
            return 1
        elif data == 2:
            return 2
        elif data == 5:
            return 3
        elif data == 7:
            return 4
        else:
            return 1

    def _get_operationType(self, data):
        if len(data) == 1:
            data = unicode.encode(unicode(data[0]), "utf8")
            if data == unicode.encode(u'Аренда', "utf8") or data == unicode.encode(u'Посуточна', "utf8"):
                return 1
            elif data == unicode.encode(u'Продажа', "utf8") or data == unicode.encode(u'Обмен', "utf8"):
                return 2
        else:
            return 1

    def _get_operation_list(self):
        operations = ' '
        for elem in self.data.list_operations.all():
            operations += unicode.encode(unicode(elem), "cp1251")
        return operations


class GetShows(ConnectDatabases):
    def __init__(self, data):
            super(GetShows, self).__init__()
            self.code = data

        # try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            # query = '''SELECT views FROM Object_Live WHERE code= "%s"''' % 'O' + str(self.code)
            c.execute("""SELECT views FROM Object_Business WHERE code=%s""", ('K' + unicode(self.code),))
            self.data = c.fetchall()
        # except:
        #     pass
        # finally:
            c.close()
            db.close()

    def data_return(self):
        if self.data:
            return '%s' % self.data[0]
        else:
            return 0


class SetShows(ConnectDatabases):
    """docstring for ClassName"""
    def __init__(self, data, active):
        super(SetShows, self).__init__()
        self.code = data
        self.active = active

        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            query = "UPDATE Object_Business SET active=%s WHERE code='%s'" % (self.active, 'K' + str(self.code))
            c.execute(query)
        except:
            pass
        finally:
            c.close()
            db.close()


class NotPost(ConnectDatabases):
    """docstring for ClassName"""
    def __init__(self, data):
        super(NotPost, self).__init__()
        self.code = data

        try:
            db = MySQLdb.connect(user=self.textusername, passwd=self.textpassword, host=self.texthostname, db=self.database, autocommit=True)
            c = db.cursor()
            query = "DELETE FROM Object_Business WHERE code='%s'" % ('K' + str(self.code))
            c.execute(query)
        except:
            pass
        finally:
            c.close()
            db.close()
