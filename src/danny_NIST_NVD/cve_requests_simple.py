import requests
import urllib3
import json
from connectors.core.connector import get_logger, ConnectorError
from .constants import LOGGER_NAME
logger = get_logger(LOGGER_NAME)

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)


def cve_requests_simple(config, params):
    cveId = str(params.get('cveId'))
    addOns = str(params.get('addOns'))

    if addOns != '':
        cveId = cveId + '?addOns=' + addOns

    res = requests.get(url=('https://services.nvd.nist.gov/rest/json/cve/1.0/' +
                       cveId), headers={'ContentType': 'application/json'}, verify=False)

    return json.loads(res.text)
