
class MojioAddOn(object):

    __name__ = ''

    def __init__(self, resource):

        self.resource = resource


class AccessAddOn(MojioAddOn):

    __name__ = 'access'

    def get(self, id):
        return self.resource._request(id, self.__name__)


class StoreAddOn(MojioAddOn):
    
    __name__ = 'store'
    
    def get(self, id, key):
        return self._request(id, self.__name__, key)

    def list(self, id):
        return self.resource._request(id, self.__name__)


class EventsAddOn(MojioAddOn):
    
    __name__ = 'events'

    def list(self, id):
        return self.resource._request(id, self.__name__)


class ImageAddOn(MojioAddOn):

    __name__ = 'image'

    def get(self, id):
        return self.resource._request(id, self.__name__)



class TripsAddOn(MojioAddOn):

    __name__ = 'trips'

    def list(self, id):
        return self.resource._request(id, self.__name__)


class OwnerAddOn(MojioAddOn):

    __name__ = 'owner'

    def get(self, id):
        return self.resource._request(id, self.__name__)


class UsersAddOn(MojioAddOn):

    __name__ = 'users'

    def list(self, id):
        return self.resource._request(id, self.__name__)


class ViewerAddOn(MojioAddOn):

    __name__ = 'viewer'

    def delete(self, id):
        pass

    def create(self, id):
        pass


class MojiosAddOn(MojioAddOn):

    __name__ = 'mojios'
    def list(self, id):
        return self.resource._request(id, self.__name__)


class VehiclesAddOn(MojioAddOn):

    __name__ = 'vehicles'

    def list(self, id):
        return self.resource._request(id, self.__name__)


