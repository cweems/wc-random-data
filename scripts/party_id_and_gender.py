from lxml import etree as et
import random

parser = et.XMLParser(remove_blank_text=True)
doc = et.parse('500RandomResponses.xml', parser)

for partyId in doc.iter('partyId'):
    partyId.text = str(random.randint(100000000000000000,999999999999999999))
    print partyId.text

for addressId in doc.iter('addressId'):
    addressId.text = str(random.randint(100000000000000000,999999999999999999))

for searchResult in doc.iter('searchResult'):
    gender = ''
    random_number = random.randint(1,3)
    if random_number == 1:
        gender = 'F'
    if random_number == 2:
        gender = 'O'
    if random_number == 3:
        gender = 'M'

    genderType = et.SubElement(searchResult, 'genderType')
    genderType.set('code', gender)

doc.write('result.xml', pretty_print=True)
