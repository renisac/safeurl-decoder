from setuptools import setup, find_packages

setup(
    name='safeurl_decoder',
    version='1.0.0',
    packages=find_packages(),
    url='https://github.com/renisac/safeurl_decoder',
    author='REN-ISAC',
    author_email='soc@ren-isac.netß',
    description='',
    entry_points = {
              'console_scripts': ['safeurl-decode=safeurl_decoder.__init__:main'],
    }
)
