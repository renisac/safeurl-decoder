import logging
from argparse import ArgumentParser
from urllib.parse import urlparse, parse_qs, unquote

LOG_FORMAT = '%(asctime)s - %(levelname)s - %(name)s[%(lineno)s][%(threadName)s] - %(message)s'

loglevel = logging.getLevelName('ERROR')
console = logging.StreamHandler()
logging.getLogger(__name__).setLevel(loglevel)
console.setFormatter(logging.Formatter(LOG_FORMAT))
logging.getLogger(__name__).addHandler(console)

logger = logging.getLogger(__name__)


class SafeURL(object):

    def __init__(self):
        pass

    def _barracuda(self, u):

        q = parse_qs(u.query)

        r = q['a'][0]
        r = unquote(r)

        return r
    
    def _proofpoint(self, u):

        q = parse_qs(u.query)

        r = q['u'][0]
        r = unquote(r.replace('_', '/').replace('-', '%'))

        return r

    def _safelinks(self, u):

        q = parse_qs(u.query)

        r = q['url'][0]
        r = unquote(r)

        return r

    def decode(self, url):

        u = urlparse(url)

        if u.hostname == 'linkprotect.cudasvc.com':
            return self._barracuda(u)
        
        elif u.hostname == 'urldefense.proofpoint.com':
            return self._proofpoint(u)

        elif 'safelinks.protection.outlook.com' in u.hostname:
            return self._safelinks(u)

        else:
            logger.debug('no provider match for host: {}'.format(u.hostname))
            return url


def main():

    p = ArgumentParser()
    p.add_argument('--debug', '-d', help='enable debug logging', action='store_true')
    p.add_argument('--url', '-u', help='url to decode')

    args = p.parse_args()

    if args.debug:
        logger.setLevel('DEBUG')

    if not args.url:
        p.print_usage()
        raise SystemExit

    print(SafeURL().decode(args.url))


if __name__ == "__main__":
    main()
