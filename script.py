from xml.etree import ElementTree as et
import random

doc = et.parse('500RandomResponses.xml')

for partyId in doc.iter('partyId'):
    partyId.text = random.randint(1,11)*5
    print partyId.text

doc.write('result.xml')
