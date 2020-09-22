import urllib

def get_page_data(url):
    page = urllib.request.urlopen(url)
    return page.read()