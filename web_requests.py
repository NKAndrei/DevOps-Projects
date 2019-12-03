import urllib

def getPageData(url):
    page = urllib.request.urlopen(url)
    return page.read()