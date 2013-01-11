#!/usr/bin/env python

import sys
from os import urandom
from twisted.web.server import Site
from twisted.web.resource import Resource,NoResource
from twisted.internet import reactor
from twisted.web.util import redirectTo
from twisted.python import log
from random import sample
from string import digits, ascii_letters
import cgi
import cache
import time
import hmac

from config import *

def short_id(size):
    return urandom(size).encode('base64').translate(None,'/+=\n')

with open('templates/index.html') as fh:
    index_template = fh.read()

with open('templates/shurl_twisted.html') as fh:
    shurl_template = fh.read()

try:
    with open('templates/404.html') as fh:
        ERROR404 = fh.read()
except:
    ERROR404 = """Couldn't find what you were looking for.<br>[<a href="/">Home</a>]"""

class UrlShortener(Resource):  # Resources are what Site knows how to deal with
    isLeaf = True  # Disable child lookup

    def render_GET(self, request):
        url_id = request.path
        for prefix in [SHORTENER_ROOT,SHORTENED_ROOT]:
            if url_id.startswith(prefix):
                url_id = url_id.lstrip(prefix)
        if not url_id:
            #return index_template.format(request.args.get('u',[''])[0],short_id(5),`dir(request)`)
            return index_template.format(request.args.get('u',[''])[0],short_id(RANDOM_BYTES),APP_MOUNTPOINT+SHORTENER_ROOT)
        else:
            if cache.tcache.has_key(url_id):
                return redirectTo(str(cache.tcache.get_value(url_id)), request)
            else:
                return NoResource(ERROR404).render(request)

    def render_POST(self, request):  # Define a handler for POST requests
        password = cgi.escape(request.args["password"][0])
        if hmac.new(PASSWORD_SALT.decode('hex'),password).hexdigest()!=PASSWORD_HASH:
            # Let's not tell abusers what went wrong :)
            return NoResource(ERROR404).render(request)
        full_url = cgi.escape(request.args["full_url"][0])
        short_url = cgi.escape(request.args["short_url"][0])
        if cache.tcache.has_key(short_url):
            # Too lazy, so instead of writing a "shourt-url is taken" template,
            # simply redirect to the existing full_url as indication :)
            # admin can hit back button and choose a different short url
            return redirectTo(str(cache.tcache.get_value(short_url)), request)
        cache.tcache.put(short_url, full_url)
        return shurl_template.format(APP_MOUNTPOINT+SHORTENED_ROOT+short_url)

def run():
    if LOG:
        log.startLogging(sys.stdout)
    reactor.listenTCP(PORT, Site(UrlShortener()))
    reactor.run()

if __name__ == '__main__':
    run()
