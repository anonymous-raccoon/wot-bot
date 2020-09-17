
import requests

class WGApplication():
    def __init__(self, id:str):
        self.__id = id


    def make_request(self, url:str, id_required=False, **kwargs):
        """Make a request to a given URL with the given query paremeters

        Arguments:
            url:str     URL to be queries
            kwargs      Query paremeters

        Returns:
            resp        Response JSON
            error       Any errors that occorded
        """
        if kwargs:  # Add query parameters
            if id_required:
                kwargs['application_id'] = self.__id
            url = f"{url}?{'&'.join([ f'{key}={kwargs[key]}' for key in kwargs])}"
        elif id_required:
            url = f"{url}?application_id={self.__id}"

        print(url)

        req = requests.get(url)

        if req.status_code != 200:
            return None, f"Unable to access wargaming API ({req.status_code})"

        return req.json(), None