from model.movie import MovieModel

class MovieService(object):
    @classmethod
    def get_all_movie(cls):
        return MovieModel.get_all_movie()
