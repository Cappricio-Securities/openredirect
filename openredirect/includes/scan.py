#!/usr/bin/env python

"""
 * Open Redirect
 * Open Redirect Bug scanner for WebPentesters and Bugbounty Hunters
 *
 * @Developed By Cappricio Securities <https://cappriciosec.com>
 */
 
"""
from includes import bot
from utils import configure
import requests
from urllib3.exceptions import InsecureRequestWarning
from urllib.parse import quote
from includes import writefile
from utils import const
from urllib.parse import urlparse

headers = {
    "Tool-Name": "openredirect",
    "Developed-by": "cappriciosec.com",
    "Contact-us": "contact@cappriciosec.com"
}

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)


def cvescan(url, output):
    try:
        with requests.Session() as session:
            payreq = session.get(const.Data.payloadurl)
            for endpoint in payreq.text.splitlines():
                encode = quote(endpoint)
                if url.endswith('/'):
                    url = url[:-1]
                fullurl = f'{url}/{endpoint}'
                try:
                    response = session.get(fullurl, verify=False, headers=headers, allow_redirects=False, timeout=5)
                    print(f'Checking ===> {fullurl}')
                    location = response.headers.get('location', None)
                    parsed_url = urlparse(location)
                    domain = parsed_url.netloc
                    domain = domain.decode('utf-8') if isinstance(domain, bytes) else domain
                    if response.status_code >= 300 and domain is not None and 'cappriciosec.com' in domain:
                        outputprint = (
                            f"\n{const.Colors.RED}💸[Vulnerable]{const.Colors.RESET} ======> "
                            f"{const.Colors.BLUE}{url}{const.Colors.RESET} \n"
                            f"{const.Colors.MAGENTA}📸PoC-Url->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}\n\n\n")
                        print(outputprint)
                        if configure.check_id() == "Exist":
                            bot.sendmessage(fullurl)
                        if output is not None:
                            writefile.writedata(
                                output, str(f'{fullurl}\n'))
                except requests.exceptions.RequestException as e:
                    print(
                        f'{const.Colors.MAGENTA}Invalid Domain ->{const.Colors.BLUE}${const.Colors.RESET} {fullurl}: {e}')
    except requests.exceptions.RequestException as e:
        print(f"Check Network Connection: {e}")
