This is a simple URL shortener in Python, where only admin can shorten URLs.

It can be used as a catch-all "last stop before 404" proxy on `/`.

To install:

* `cp config-example.py config.py`
* `python mkpass.py >> config.py` (prompts for password twice)
* Edit `config.py` to your taste
* [optional] create `templaties/404.html` (note, it's a partial template. See `templates/404-example.py`).
  If you use this as a catch-all, this will become your site's 404 page.

To run:

`python twisted_server.py`
