# import objects
import xml.etree.ElementTree as ET
import requests

# download file from Microsoft and open it for read
XML_URL = 'https://support.content.office.net/en-us/static/O365IPAddresses.xml'
r = requests.get(XML_URL, allow_redirects=True)
XML_File = open('O365IPAddresses.xml', 'r')

# overwrite old files with files
Parsed_File_URL = open('/Users/christophervandermade/Desktop/MicrosoftXMLFeedParser/Parsed_File_URL.txt', 'w+')
Parsed_File_IPv4 = open('/Users/christophervandermade/Desktop/MicrosoftXMLFeedParser/Parsed_File_IPv4.txt', 'w+')
Parsed_File_IPv6 = open('/Users/christophervandermade/Desktop/MicrosoftXMLFeedParser/Parsed_File_IPv6.txt', 'w+')

# parse XML file
tree = ET.parse(XML_File)
root = tree.getroot()

# initiate lists to be filled with addresses
URL_List = []
IPv4_List = []
IPv6_List = []

#loop through XML file and add addresses to the correct lists
for addresslist in root.iter('addresslist'):
    if(addresslist.get('type') == "URL"):
        for address in addresslist.findall('address'):
            URL_List.append(address.text)
    if(addresslist.get('type') == "IPv4"):
        for address in addresslist.findall('address'):
            IPv4_List.append(address.text)
    if(addresslist.get('type') == "IPv6"):
        for address in addresslist.findall('address'):
            IPv6_List.append(address.text)

#create .txt files to use in firepower
for URL in URL_List:
	Parsed_File_URL.write("%s\n" % URL)
    
for IPv4 in IPv4_List:
	Parsed_File_IPv4.write("%s\n" % IPv4)

for IPv6 in IPv6_List:
	Parsed_File_IPv6.write("%s\n" % IPv6)

# TO DO: upload TXT files to Firepower as objects (either through API, or by hosting online them and use them as Network Object Feed)

#/api/fmc_config/v1/domain/{domain_UUID}/object/networks/{object_UUID}


#close the opened files, end of script
XML_File.close
Parsed_File_URL.close
Parsed_File_IPv4.close
Parsed_File_IPv6.close