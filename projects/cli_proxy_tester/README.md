# mini-projects-python - cli based proxy tester (#77)

*Author:* Ingo Kleiber (ingo@kleiber.me)

This mini project is a proxy tester based on `requests`. It utilized `pandas` for handling csv files and
`click` for the CLI.

## Usage

This script tests proxies by querying (GET request) a testing website that returns the IP of the client. If the returned IP matches the IP of the proxy, we consider the proxy to be good.

### Testing Single Proxies

`python cli.py single http://1.1.1.1`

This will test the HTTP proxy 1.1.1.1 against the default testing website [iptest.ingokleiber.de](http://iptest.ingokleiber.de).
You can run your own testing service using the PHP script in `/ipinfo`. This service should be offered both via HTTP and HTTPs.

`python cli.py single http://1.1.1.1 --iptest iptest.yourdomain.com`

### (Re)Testing a CSV File

`python cli.py csv-file proxies.csv`

This will (re)test all proxies in the given file.

### Adding and Testing Proxies From a Text File

`python cli.py add-from-txt-file proxy_candidates.txt`

This will add and test each proxy (one per line) in `proxy_candidates.txt`.
