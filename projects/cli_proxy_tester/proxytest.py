from pathlib import Path
import logging
import requests
from requests.exceptions import ProxyError
import pandas as pd
from json.decoder import JSONDecodeError

logging.basicConfig(level=logging.INFO)


def add_proxies_to_file(csv_path: str, proxies: list):
    '''This function will add one or multiple proxies to the CSV file.'''

    if not csv_path.exists():
        proxies_file: pd.DataFrame = pd.DataFrame(columns=['proxy_type', 'proxy_address', 'proxy_status'])
        logging.info('New CSV file will be created')
    else:
        proxies_file: pd.DataFrame = pd.read_csv(csv_path)
        logging.info('Existing CSV file has been loaded')

    for proxy in proxies:
        if len(proxies_file) == 0:
            # First proxy in the file
            proxies_file = proxies_file.append(proxy, ignore_index=True)
        else:
            if len(proxies_file.loc[ (proxies_file['proxy_type'] == proxy['proxy_type']) & (proxies_file['proxy_address'] == proxy['proxy_address'])]) > 0:
                # Proxy is already in the file
                proxies_file.loc[ (proxies_file['proxy_type'] == proxy['proxy_type']) & (proxies_file['proxy_address'] == proxy['proxy_address']) , ['proxy_status']] = proxy['proxy_status']
            else:
                # Proxy is not yet in the file
                proxies_file = proxies_file.append(proxy, ignore_index=True)

        
    proxies_file = proxies_file.drop_duplicates()
    proxies_file.to_csv(csv_path, index=False)
    logging.info('CSV file has been written')


def test_proxy(proxy_type: str, proxy_address: str, iptest: str):
    '''This function takes a proxy (type, address) and tests it against a given iptest adress.'''

    logging.info(f'Testing proxy: {proxy_address}')

    try:
        proxies = {proxy_type: proxy_address}
        proxy_status: str = ''
        r = requests.get('http://iptest.ingokleiber.de', proxies=proxies)

        try:
            json_response: dict = r.json()
            
            if json_response["ip"] == proxy_address:
                proxy_status = 'Proxy functional'
            else:
                logging.warning(f'Proxy "{proxy_address}" returned {json_response}')
                proxy_status = 'Proxy not functional'
        except JSONDecodeError:
            proxy_status = 'Invalid response'
    except ProxyError:
        proxy_status = 'Proxy error'

    logging.info(f'Proxy {proxy_address}: {proxy_status}')
    return {'proxy_type': proxy_type, 'proxy_address': proxy_address, 'proxy_status': proxy_status}


def test_single_proxy(proxy: str, iptest: str, csv_path: str):
    '''This function tests an individual proxy and adds it to the CSV file.'''
    proxy_type, proxy_address = proxy.split('://')
    result: dict = test_proxy(proxy_type, proxy_address, iptest)

    add_proxies_to_file(Path(csv_path), [result])


def test_file(iptest: str, csv_path: str):
    '''This function (re)tests every proxy in a given CSV file.'''

    csv_path: Path = Path(csv_path)

    if csv_path.exists():
        proxies_file: pd.DataFrame = pd.read_csv(csv_path)
    else:
        raise FileNotFoundError

    proxies: list = []

    for index, proxy in proxies_file.iterrows():
        proxies.append(test_proxy(proxy['proxy_type'], proxy['proxy_address'], iptest))

    add_proxies_to_file(csv_path, proxies)


def add_from_text_file(iptest: str, text_path: str, csv_path: str):
    ''' This function adds a list of proxies from a text file (line by line).'''
    text_path: Path = Path(text_path)

    if text_path.exists():
        proxies: list = text_path.read_text().splitlines()

        for proxy in proxies:
            # We will treat each proxy as a single proxy and leverage the existing function
            test_single_proxy(proxy, iptest, csv_path)
    else:
        raise FileNotFoundError
