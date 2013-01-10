#### Development
LOG = True
PORT = 51723
APP_MOUNTPOINT = 'http://localhost:{0}'.format(PORT)
SHORTENER_ROOT = '/'
SHORTENED_ROOT = '/'

#### Deployment behind proxy
# Shortener is mounted on '/shorten'
# Catch-all on '/'  also proxies to the shortener
#LOG = False
#APP_MOUNTPOINT = 'https://example.com'
#SHORTENER_ROOT = '/shorten/'
#SHORTENED_ROOT = '/'

