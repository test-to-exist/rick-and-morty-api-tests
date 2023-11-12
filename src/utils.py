import re
import xml.etree.ElementTree as ET
from pathlib import Path


def get_project_root() -> Path:
    return Path(__file__).parent.parent


def split_string_on_uppercase(input_string):
    result = re.findall('[A-Z][^A-Z]*', input_string)
    return result


def transform_report(filename):
    tree = ET.parse(filename)
    root = tree.getroot()

    for testcase in root.iter('testcase'):
        arr = testcase.attrib['name'].split("_")
        arr = arr[1:len(arr)]
        arr[0] = str.upper(arr[0][0]) + arr[0][1:len(arr[0])]
        testcase.attrib['name'] = " ".join(arr)
        testcase.attrib['classname'] = " ".join(split_string_on_uppercase(testcase.attrib['classname'].split(".")[2]))

    for testsuite in root.iter('testsuite'):
        testsuite.attrib['name'] = " ".join(
            split_string_on_uppercase(testsuite.attrib['name'].split(".")[2].split("-")[0]))
        tree.write('TEST-report.xml')
