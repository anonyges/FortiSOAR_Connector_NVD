import requests
import urllib3
import json
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
logger = get_logger(LOGGER_NAME)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cve_requests(config, params):
    startIndex = str(params.get('startIndex'))
    resultsPerPage = str(params.get('resultsPerPage'))
    pubStartDate = str(params.get('pubStartDate'))
    pubEndDate = str(params.get('pubEndDate'))
    modStartDate = str(params.get('modStartDate'))
    modEndDate = str(params.get('modEndDate'))
    includeMatchStringChange = str(params.get('includeMatchStringChange'))
    keyword = str(params.get('keyword'))
    isExactMatch = str(params.get('isExactMatch'))
    cweId = str(params.get('cweId'))
    cvssV2Severity = str(params.get('cvssV2Severity'))
    cvssV3Severity = str(params.get('cvssV3Severity'))
    cvssV2Metrics = str(params.get('cvssV2Metrics'))
    cvssV3Metrics = str(params.get('cvssV3Metrics'))
    cpeMatchString = str(params.get('cpeMatchString'))
    addOns = str(params.get('addOns'))

    def build_uri(startIndex: str = '', resultsPerPage: str = '', pubStartDate: str = '', pubEndDate: str = '', modStartDate: str = '', modEndDate: str = '', includeMatchStringChange: str = '', keyword: str = '', isExactMatch: str = '', cweId: str = '', cvssV2Severity: str = '', cvssV3Severity: str = '', cvssV2Metrics: str = '', cvssV3Metrics: str = '', cpeMatchString: str = '', addOns: str = ''):
        uri = []

        if startIndex != '':
            startIndex = 'startIndex=' + startIndex
            uri.append(startIndex)
        if resultsPerPage != '':
            resultsPerPage = 'resultsPerPage=' + resultsPerPage
            uri.append(resultsPerPage)
        if pubStartDate != '':
            pubStartDate = 'pubStartDate=' + pubStartDate
            uri.append(pubStartDate)
        if pubEndDate != '':
            pubEndDate = 'pubEndDate=' + pubEndDate
            uri.append(pubEndDate)
        if modStartDate != '':
            modStartDate = 'modStartDate=' + modStartDate
            uri.append(modStartDate)
        if modEndDate != '':
            modEndDate = 'modEndDate=' + modEndDate
            uri.append(modEndDate)
        if includeMatchStringChange != '':
            includeMatchStringChange = 'includeMatchStringChange=' + includeMatchStringChange
            uri.append(includeMatchStringChange)
        if keyword != '':
            keyword = 'keyword=' + keyword
            uri.append(keyword)
        if isExactMatch != '':
            isExactMatch = 'isExactMatch=' + isExactMatch
            uri.append(isExactMatch)
        if cweId != '':
            cweId = 'cweId=' + cweId
            uri.append(cweId)
        if cvssV2Severity != '':
            cvssV2Severity = 'cvssV2Severity=' + cvssV2Severity
            uri.append(cvssV2Severity)
        if cvssV3Severity != '':
            cvssV3Severity = 'cvssV3Severity=' + cvssV3Severity
            uri.append(cvssV3Severity)
        if cvssV2Metrics != '':
            cvssV2Metrics = 'cvssV2Metrics=' + cvssV2Metrics
            uri.append(cvssV2Metrics)
        if cvssV3Metrics != '':
            cvssV3Metrics = 'cvssV3Metrics=' + cvssV3Metrics
            uri.append(cvssV3Metrics)
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

    additional_search_uri = build_uri(startIndex=startIndex,
                                      resultsPerPage=resultsPerPage,
                                      pubStartDate=pubStartDate,
                                      pubEndDate=pubEndDate,
                                      modStartDate=modStartDate,
                                      modEndDate=modEndDate,
                                      includeMatchStringChange=includeMatchStringChange,
                                      keyword=keyword,
                                      isExactMatch=isExactMatch,
                                      cweId=cweId,
                                      cvssV2Severity=cvssV2Severity,
                                      cvssV3Severity=cvssV3Severity,
                                      cvssV2Metrics=cvssV2Metrics,
                                      cvssV3Metrics=cvssV3Metrics,
                                      cpeMatchString=cpeMatchString,
                                      addOns=addOns
                                      )

    res = requests.get(url=('https://services.nvd.nist.gov/rest/json/cves/1.0?' +
                       additional_search_uri), headers={'ContentType': 'application/json'}, verify=False)

    # debug print
    # print(json.dumps(json.loads(res.text), indent=4))

    return json.loads(res.text)
