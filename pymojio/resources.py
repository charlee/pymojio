import requests
import urllib

from .addons import AccessAddOn, StoreAddOn, EventsAddOn, ImageAddOn, UsersAddOn, ViewerAddOn, TripsAddOn, MojiosAddOn, VehiclesAddOn

class MojioResource(object):

    __name__ = ''

    def __init__(self, mojio):

        self.mojio = mojio


    def _request(self, *args, **kwargs):

        if self.mojio.credentials is None:
            raise NotAuthorized

        path = '/'.join(args)
        url = '%s%s/%s' % (self.mojio.api_base_uri, self.__name__, path)

        method = kwargs.get('method', 'GET')
        params = kwargs.get('params', None)
        data = kwargs.get('data', None)

        headers = { 'MojioAPIToken': self.mojio.access_token }

        print url

        r = requests.request(method, url, params=params, data=data, headers=headers)

        # TODO: raise http error
        return r.json()

    
    def list(self, limit=10, offset=0, sortBy=None, desc=False):
        params = {
            'limit': limit,
            'offset': offset,
        }

        if sortBy:
            params['sortBy'] = sortBy

        if desc:
            params['desc'] = 'true'

        url_params = urllib.urlencode(params)
        
        return self._request(params=url_params)
    

    def get(self, id):
        return self._request(id)



class MojioResourceWithAccessAndStore(MojioResource):

    def __init__(self, mojio):
        
        super(MojioResourceWithAccessAndStore, self).__init__(mojio)

        self.store = StoreAddOn(self)
        self.access = AccessAddOn(self)


class MojioResourceFull(MojioResourceWithAccessAndStore):

    def __init__(self, mojio):
        
        super(MojioResourceFull, self).__init__(mojio)

        self.events = EventsAddOn(self)
        self.image = ImageAddOn(self)
        self.trips = TripsAddOn(self)


class MojioApps(MojioResourceWithAccessAndStore):

    __name__ = 'apps'



class MojioEvents(MojioResourceWithAccessAndStore):

    __name__ = 'events'


class MojioMojios(MojioResourceWithAccessAndStore):

    __name__ = 'mojios'


class MojioObservers(MojioResource):

    __name__ = 'observers'

    def get(self):
        raise NotImplemented


    def int_check_permission(self):
        # TODO
        pass

    def int_create_observer(self):
        # TODO
        pass


class MojioSchema(MojioResource):
    
    __name__ = 'schema'


class MojioTrips(MojioResourceWithAccessAndStore):

    __name__ = 'trips'

    def __init__(self, mojio):
        
        super(MojioTrips, self).__init__(mojio)

        self.events = EventsAddOn(self)


    def merge_trips(self):
        # TODO
        pass

        



class MojioUsers(MojioResourceFull):

    __name__ = 'users'

    def __init__(self, mojio):

        super(MojioUsers, self).__init__(mojio)

        self.mojios = MojiosAddOn(self)
        self.vehicles = VehiclesAddOn(self)
        # TODO


    def me(self):
        return self._request('me')



class MojioVehicles(MojioResourceFull):

    __name__ = 'vehicles'

    def __init__(self, mojio):
        
        super(MojioVehicles, self).__init__(mojio)

        # TODO

        self.users = UsersAddOn(self)
        self.viewer = ViewerAddOn(self)


class MojioVins(MojioResource):

    def list(self):
        raise NotImplemented


    def get_vehicle_services(self):

        # TODO
        pass
