PORT = 51723 # Should be firewalled when deployed
RANDOM_BYTES = 6 # Length of random suggestions would be ~ a third longer than this
#### Development
LOG = True
APP_MOUNTPOINT = 'http://localhost:{0}'.format(PORT)
SHORTENER_ROOT = '/'
SHORTENED_ROOT = '/'

#### Deployment behind proxy
# Shortener is mounted on '/hard-to-guess-url'
# Catch-all on '/'  also proxies to the shortener
#LOG = False
#APP_MOUNTPOINT = 'https://example.com'
#SHORTENER_ROOT = '/hard-to-guess-url/'
#SHORTENED_ROOT = '/'

