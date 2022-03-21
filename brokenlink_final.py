
from requests_ntlm import HttpNtlmAuth
from urllib.parse import urlsplit
import requests
from bs4 import BeautifulSoup
import pandas as pd
import validators
import logging
logging.basicConfig(level=logging.DEBUG)


def SharePointCrawler(url, usr, pwd, out_path):
    # trys to validate base url from main URL passed to this function. eg https://www.example.com from https://www.example.com/xyz/blabla
    base_url = "{0.scheme}://{0.netloc}/".format(urlsplit(url))[:-1]
    # Authenticate and pass your credentials for GET method
    content = requests.get(url, auth=HttpNtlmAuth(usr, pwd))
    response_code = str(content.status_code)
    data = content.text
    # BeautifulSoup will scrape information from web page(s)
    soup = BeautifulSoup(data, 'html.parser')
    LinksListRaw = []
    '''
    At this stage we will try to find all the URLs from above web scrape and validate correct URL to move to next stage of validation.
    LinksListRaw will contain the URL and its URL text in form of list of lists. For this action, we have used Validators package
    '''
    for link in soup.find_all('a'):

        valid = validators.url(f"{link.get('href')}")

        if valid == True:

            LinksListRaw.append([f"{link.get('href')}", link.text.strip()])

        elif f"{link.get('href')}".startswith('/'):

            fixed_url = ("{}{}".format(base_url, f"{link.get('href')}"))

            LinksListRaw.append([fixed_url, link.text.strip()])

        elif "/mylink/" in f"{link.get('href')}":

            LinksListRaw.append([f"{link.get('href')}", link.text.strip()])

        else:

            logging.error(f" Invalid URL: {link.get('href')}")

    '''
    From set method, we are filtering unique URLs to avoid repetitive validation
    '''
    link_set = set(tuple(x) for x in LinksListRaw)
    UniqueLinkList = [list(x) for x in link_set]
    brokenlinklist = []
    list_length = len(UniqueLinkList)
    count = 0

    '''
    Below method will further refine valid URLs and remove all the URLs which do not redirect.
    '''
    for url in UniqueLinkList:
        count = count + 1
        try:

            logging.debug("Testing if URL '{}' is valid URL".format(url))
            if (not url[0].endswith(".png")) and (not url[0].endswith(".jpg")) and (not url[0].endswith(".pdf")) and (not url[0].endswith(".xlsx")) and (not url[0].endswith(".xls")):
                if url[0].endswith(".comNone"):

                    correct_url = url[0].replace(".comNone", ".com")
                    content = requests.get(
                        correct_url, auth=HttpNtlmAuth(usr, pwd))

                    if content.status_code == 404 or content.status_code == 401:
                        brokenlinklist.append(
                            [correct_url, url[1], f"Status Code: {str(response_code)}"])

                elif url[1].endswith(".com#"):
                    correct_url2 = url[1].replace(".com#", ".com")
                    content = requests.get(
                        correct_url2, auth=HttpNtlmAuth(usr, pwd))

                    if content.status_code == 404 or content.status_code == 401:
                        brokenlinklist.append(
                            [correct_url2, url[1], f"Status Code: {str(response_code)}"])

                else:
                    content = requests.get(url[0], auth=HttpNtlmAuth(usr, pwd))

                    if content.status_code == 404 or content.status_code == 401:
                        brokenlinklist.append(
                            [url[0], url[1], f"Status Code: {str(response_code)}"])

        except Exception as ex:
            logging.error("Cannot pase URL {}: {}".format(url[0], ex))

        logging.debug("{} URL verified out of {}.".format(count, list_length))

    '''
    Finally, putting everything in a .csv file using pandas
    '''
    dataframeFinal = pd.DataFrame(brokenlinklist, columns=[
                                  "URL", "URL Header", "Status"])  # Creating a table of link source URL, Broken link and its header
    dataframeFinal = dataframeFinal.drop_duplicates(
        subset=['URL'], keep='last')
    return dataframeFinal.to_csv(out_path, header=True, index=False)
