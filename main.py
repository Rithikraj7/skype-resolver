import sys
import re
from bs4 import BeautifulSoup
import requests


def get_html_from_url(url, name):
    response = requests.get(url, params={'name': name})
    if response.status_code == 200:
        return response.text
    else:
        return None


def get_reverse_from_resolvethem(name):
    url = 'http://www.resolvethem.com/'
    html = get_html_from_url(url, name)

    if html:
        parser = BeautifulSoup(html, 'html.parser')
        data = parser.find('div', class_='inner')

        if data is not None:
            ip = re.search(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", data.get_text())

            if ip:
                if re.match(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", ip.group(0)):
                    return ip.group(0)

        return False

    return False


# Example usage
name_to_resolve = "name"
reverse_ip = get_reverse_from_resolvethem(name_to_resolve)

if reverse_ip:
    print(f"Reverse IP for {name_to_resolve}: {reverse_ip}")
else:
    print(f"Failed to get reverse IP for {name_to_resolve}")
