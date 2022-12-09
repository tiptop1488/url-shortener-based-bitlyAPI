import requests
from urllib.parse import urlparse
import os
import argparse
from dotenv import load_dotenv


def shorten_link(token, input_link):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    payload = {
        "long_url": input_link,
    }
    url = 'https://api-ssl.bitly.com/v4/bitlinks'
    response = requests.post(url, headers=headers, json=payload)
    response.raise_for_status()
    description = response.json()
    bitlink = description['link']
    return bitlink


def count_clicks(token, bitlink):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{bitlink}/clicks/summary'
    response = requests.get(url, headers=headers)
    response.raise_for_status()
    description = response.json()
    total_clicks = description['total_clicks']
    return total_clicks


def is_bitlink(token, url):
    headers = {
        'Authorization': f'Bearer {token}',
    }
    url = f'https://api-ssl.bitly.com/v4/bitlinks/{url}'
    response = requests.get(url, headers=headers)
    return response.ok


def main():
    load_dotenv()
    bitly_token = os.environ['BITLY_TOKEN']
    parser = argparse.ArgumentParser()
    parser.add_argument('link')
    args = parser.parse_args()
    input_link = args.link
    url_components = urlparse(input_link)
    modifed_link = f"{url_components.netloc}{url_components.path}"
    try:
        if is_bitlink(bitly_token, modifed_link):
            total_click = count_clicks(bitly_token, modifed_link)
            print(total_click)
        else:
            bitlink = shorten_link(bitly_token, input_link)
            print(bitlink)
    except requests.exceptions.HTTPError:
        print("Вы ввели не правильную ссылку")


if __name__ == "__main__":
    main()
