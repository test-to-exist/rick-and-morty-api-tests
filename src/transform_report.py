import xml.etree.ElementTree as ET

if __name__ == '__main__':
    tree = ET.parse('TEST-report.xml')
    root = tree.getroot()

    for testcase in root.iter('testcase'):
        arr = testcase.attrib['name'].split("_")
        arr = arr[1:len(arr)]
        arr[0] = str.upper(arr[0][0]) + arr[0][1:len(arr[0])]
        testcase.attrib['name'] = " ".join(arr)
        print(testcase.attrib)
