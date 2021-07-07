import requests
import urllib3
import json
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
logger = get_logger(LOGGER_NAME)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cpe_requests(config, params):
    resultsPerPage = str(params.get('resultsPerPage'))
    startIndex = str(params.get('startIndex'))
    modStartDate = str(params.get('modStartDate'))
    modEndDate = str(params.get('modEndDate'))
    includeDeprecated = str(params.get('includeDeprecated'))
    keyword = str(params.get('keyword'))
    cpeMatchString = str(params.get('cpeMatchString'))
    addOns = str(params.get('addOns'))

    def build_uri(resultsPerPage: str = '', startIndex: str = '', modStartDate: str = '', modEndDate: str = '', includeDeprecated: str = '', keyword: str = '', cpeMatchString: str = '', addOns: str = ''):
        uri = []
        if resultsPerPage != '':
            resultsPerPage = 'resultsPerPage=' + resultsPerPage
            uri.append(resultsPerPage)
        if startIndex != '':
            startIndex = 'startIndex=' + startIndex
            uri.append(startIndex)
        if modStartDate != '':
            modStartDate = 'modStartDate=' + modStartDate
            uri.append(modStartDate)
        if modEndDate != '':
            modEndDate = 'modEndDate=' + modEndDate
            uri.append(modEndDate)
        if includeDeprecated != '':
            includeDeprecated = 'includeDeprecated=' + includeDeprecated
            uri.append(includeDeprecated)
        if keyword != '':
            keyword = 'keyword=' + keyword
            uri.append(keyword)
        if cpeMatchString != '':
            cpeMatchString = 'cpeMatchString=' + cpeMatchString
            uri.append(cpeMatchString)
        if addOns != '':
            addOns = 'addOns=' + addOns
            uri.append(addOns)

        # if there is a search query
        if len(uri) > 0:
            return '&'.join(uri)

        # else
        return ''

    additional_search_uri = build_uri(resultsPerPage=resultsPerPage,
                                      startIndex=startIndex,
                                      modStartDate=modStartDate,
                                      modEndDate=modEndDate,
                                      includeDeprecated=includeDeprecated,
                                      keyword=keyword,
                                      cpeMatchString=cpeMatchString,
                                      addOns=addOns
                                      )
    res = requests.get(url=('https://services.nvd.nist.gov/rest/json/cpes/1.0?' +
                       additional_search_uri), headers={'ContentType': 'application/json'}, verify=False)

    # debug print
    # print(json.dumps(json.loads(res.text), indent=4))
    return json.loads(res.text)
