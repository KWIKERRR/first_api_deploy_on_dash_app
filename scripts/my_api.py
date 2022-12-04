import requests

class Movie :
    '''
    Contains all the informations we want to keep about the movie in a Movie object

    Params :
    id : Movie's id in the imdb apis
    title : Movie's title
    image : Movie's main image
    description : Movie's description
    rate : Movie's imdb rate 
    '''
    def __init__(self, content) -> None:
        self.id = content.get('id')
        self.title = content.get('title')
        self.image = content.get('image')
        self.description = content.get('description')
        self.rate = 0
    
    def _update_rate_(self, rate) :
        '''
        Set the Movie's rate

        Params :
        rate : Movie's rate
        '''
        self.rate = rate

class SearchMovie :
    '''
    Object contains the content of the request to the SearchMovie imbd api.
    This api gives all movie's information retrieved by imdb that correspond to the search name.

    Params :
    url : Url to request to the SearchMovie imdb api (constructed with api's base url + the imdb key + the searched name)
    content : Request's return
    '''
    _base_url = 'https://imdb-api.com/en/API/SearchMovie/'
    def __init__(self, key, name) -> None:
        self.url = self._base_url + key + name
        self.content = requests.get(self.url).json()

    def _get_content_(self, i) :
        '''
        Gives the ith movie's content in the request's return

        Params :
        i : the ith movie 
        '''
        return self.content.get('results')[i]

class SearchRate :
    '''
    Object contains the content of the request to the Ratings imbd api.
    This api gives the movie's rate give by differents organism.

    Params : 
    url : Url to request to the SearchMovie imdb api (constructed with api's base url + the imdb key + the searched name)
    content : Request's return
    '''
    _base_url = 'https://imdb-api.com/en/API/Ratings/'
    def __init__(self, key, id) -> None:
        self.url = self._base_url + key + id
        self.content = requests.get(self.url).json()

    def _get_content_(self) :
        '''
        Gives the movie's imdb rate
        '''
        return self.content.get('imDb')

class RequestMovie :
    '''
    Our api constructed with two imdb api (SearchMovie and Ratings).
    Gives the first movie's informations and rate in the imdb dataset.

    Params :
    key : imdb account's key
    '''
    def __init__(self, key) -> None:
        self.key = key + '/'

    def get_movie(self, name) :
        '''
        Returns movie's informations and rate. 
        Only the first movie founds in the imdb dataset is retrieved.

        Input :
        name : Movie's name

        Output :
        movie : Movie's object with the movie's informations and rate
        '''
        content = SearchMovie(self.key, name)._get_content_(0)
        movie = Movie(content)
        rate = SearchRate(self.key, movie.id)._get_content_()
        movie._update_rate_(rate)
        return movie
    