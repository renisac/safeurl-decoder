
# safeurl_decoder
Python SDK for decoding safeurls from Barracuda, Cisco, Proofpoint, Microsoft, etc.

## Install

```
git clone https://github.com/renisac/safeurl_decoder.git

cd safeurl_decoder/

python setup.py install

```

## CLI Usage

```
$ safeurl-decode
usage: safeurl-decode [-h] [--debug] [--url URL]
```

## Python 

```
from safeurl_decoder import SafeURL

r = SafeURL().decode('https://www.google.com')

print(r)

# https://www.google.com

```
