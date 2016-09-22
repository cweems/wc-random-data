from lxml import etree as et
import random
import time

def strTimeProp(start, end, format, prop):

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))
    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%Y-%m-%dT%H:%M:%S.000Z', prop)

parser = et.XMLParser(remove_blank_text=True)
doc = et.parse('source/500RandomResults.xml', parser)

for searchResult in doc.iter('searchResult'):

    #Set Random Timestamp
    lastUpdatedDate = et.SubElement( searchResult, 'lastUpdatedDate')
    randomTimestamp = randomDate("2010-01-11T16:00:00.000Z", "2016-09-18T16:00:00.000Z", random.random())
    lastUpdatedDate.text = randomTimestamp

    addressUsageType = et.SubElement( searchResult, 'addressUsageType')
    randomAddressType = 100000 + random.randint(1,2)
    addressUsageType.set('code', str(randomAddressType))

doc.write('results/result.xml', pretty_print=True)
