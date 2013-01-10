import os
from beaker.cache import CacheManager
from beaker.util import parse_cache_config_options

dot = os.path.dirname(__file__)

cache_opts = {
    'cache.type': 'file',
    'cache.data_dir': os.path.join(dot,'url_shortener_data'),
    'cache.lock_dir': os.path.join(dot,'url_shortener_lock'),
}

cache = CacheManager(**parse_cache_config_options(cache_opts))
tcache = cache.get_cache("stuff", type='dbm') #, expire=3600)
