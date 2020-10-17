import requests
import os
from bs4 import BeautifulSoup, SoupStrainer
# Makes Output Directory if it does not exist
if not os.path.exists(os.path.join(os.getcwd(), 'HackerNews')):
    os.makedirs(os.path.join(os.getcwd(), 'HackerNews'))
'''
@params page_no: The page number of HackerNews to fetch.
Adding only page number in order to add multiprocess support in future.
@params verbose: Adds verbose output to screen instead
of running the program silently.
'''


def fetch(page_no, verbose=False):
    # Should be unreachable, but just in case
    if page_no <= 0:
        raise ValueError('Number of Pages must be greater than zero')
    page_no = min(page_no, 20)
    i = page_no
    if verbose:
        print('Fetching Page {}...'.format(i))
    try:
        res = requests.get('https://news.ycombinator.com/?p=' + str(i))
        only_td = SoupStrainer('td')
        soup = BeautifulSoup(res.content, 'html.parser', parse_only=only_td)
        tdtitle = soup.find_all('td', attrs={'class': 'title'})
        tdmetrics = soup.find_all('td', attrs={'class': 'subtext'})
        with open(os.path.join('HackerNews', 'NewsPage{}.txt'.format(i)), 'w+') as f:
            f.write('-' * 80)
            f.write('\n')
            f.write('Page {}'.format(i))
            tdtitle = soup.find_all('td', attrs={'class': 'title'})
            tdrank = soup.find_all(
                'td',
                attrs={
                    'class': 'title',
                    'align': 'right'})
            tdtitleonly = [t for t in tdtitle if t not in tdrank]
            tdmetrics = soup.find_all('td', attrs={'class': 'subtext'})
            tdt = tdtitleonly
            tdr = tdrank
            tdm = tdmetrics
            num_iter = min(len(tdr), len(tdt))
            for idx in range(num_iter):
                f.write('\n' + '-' * 80 + '\n')
                rank = tdr[idx].find('span', attrs={'class': 'rank'})
                titl = tdt[idx].find('a', attrs={'class': 'storylink'})
                url = titl['href'] if titl and titl['href'].startswith(
                    'https') else 'https://news.ycombinator.com/' + titl['href']
                site = tdt[idx].find('span', attrs={'class': 'sitestr'})
                score = tdm[idx].find('span', attrs={'class': 'score'})
                time = tdm[idx].find('span', attrs={'class': 'age'})
                author = tdm[idx].find('a', attrs={'class': 'hnuser'})
                f.write(
                    '\nArticle Number: ' +
                    rank.text.replace(
                        '.',
                        '') if rank else '\nArticle Number: Could not get article number')
                f.write(
                    '\nArticle Title: ' +
                    titl.text if titl else '\nArticle Title: Could not get article title')
                f.write(
                    '\nSource Website: ' +
                    site.text if site else '\nSource Website: https://news.ycombinator.com')
                f.write(
                    '\nSource URL: ' +
                    url if url else '\nSource URL: No URL found for this article')
                f.write(
                    '\nArticle Author: ' +
                    author.text if author else '\nArticle Author: Could not get article author')
                f.write(
                    '\nArticle Score: ' +
                    score.text if score else '\nArticle Score: Not Scored')
                f.write(
                    '\nPosted: ' +
                    time.text if time else '\nPosted: Could not find when the article was posted')
                f.write('\n' + '-' * 80 + '\n')
    except (requests.ConnectionError, requests.packages.urllib3.exceptions.ConnectionError) as e:
        print('Connection Failed for page {}'.format(i))
    except requests.RequestException as e:
        print("Some ambiguous Request Exception occurred. The exception is " + str(e))


while(True):
    try:
        pages = int(
            input('Enter number of pages that you want the HackerNews for (max 20): '))
        v = input('Want verbose output y/[n] ?')
        verbose = v.lower().startswith('y')
        if pages > 20:
            print('A maximum of only 20 pages can be fetched')
        pages = min(pages, 20)
        for page_no in range(1, pages + 1):
            fetch(page_no, verbose)
        break
    except ValueError:
        print('\nInvalid input, probably not a positive integer\n')
        continue
