from bs4 import BeautifulSoup
import requests


class Proxy:
    def get_proxies(self):
        url = 'https://sslproxies.org/'
        header = {
            'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) \
              AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
        }
        response = requests.get(url, headers=header)
        data = BeautifulSoup(response.content, 'lxml')
        return data

    def save_proxies(self):
        file = open('proxy.txt', 'w')
        session = requests.Session()
        data = self.get_proxies()
        for item in data.select('div.table-responsive.fpl-list>table>tbody>tr'):
            row = item.select('td')
            proxy = '{}:{}'.format(row[0].get_text(), row[1].get_text())
            session.proxies = {'http': proxy, 'https': proxy}
            file.write(proxy + '\n')
        file.close()

    def read_proxies(self):
        proxies = []
        file = open('proxy.txt', 'r')
        proxies = file.read().split('\n')[:-1]
        return proxies

    def health_check(self, proxy):
        session = requests.Session()
        session.proxies = {'http': proxy, 'https': proxy}
        try:
            ip = session.get("http://icanhazip.com", timeout=1.5).text.strip()
            checked = ip == proxy.split(':')[0]
        except:
            checked = False
        return checked