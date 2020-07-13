import logging
import click

from proxytest import test_single_proxy, test_file, add_from_text_file

@click.group()
def cli():
    pass

@cli.command()
@click.argument('proxy')
@click.option('--iptest', default='http://iptest.ingokleiber.de', help='iptest address')
@click.option('--csv', default='proxies.csv', help='CSV path')
def single(proxy, iptest, csv):
    test_single_proxy(proxy, iptest, csv)

@cli.command()
@click.argument('csv')
@click.option('--iptest', default='http://iptest.ingokleiber.de', help='iptest address')
def csv_file(iptest, csv):
    test_csv_file(iptest, csv)

@cli.command()
@click.argument('txt')
@click.option('--iptest', default='http://iptest.ingokleiber.de', help='iptest address')
@click.option('--csv', default='proxies.csv', help='CSV path')
def add_from_txt_file(iptest, txt, csv):
    add_from_text_file(iptest, txt, csv)


if __name__ == '__main__':
    cli()
