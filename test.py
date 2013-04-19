from wsgiref.simple_server import make_server
from pyramid.config import Configurator
from pyramid.response import Response

import xkcd

def get_comic_text(request):
    comic = xkcd.getRandomComic()
    text = comic.getAltText()
    return Response(text)

if __name__ == '__main__':
    config = Configurator()
    config.add_route('comic_text', '/comic_text')
    config.add_view(get_comic_text, route_name='comic_text')
    app = config.make_wsgi_app()
    server = make_server('0.0.0.0', 8080, app)
    server.serve_forever()
