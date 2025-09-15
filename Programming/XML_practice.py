import xml.etree.ElementTree as ET

data = ("""
        <head>
            <title>UserInformation</title>
            <body>
                <user1>
                    <name>David</name>
                    <number>202538928</number>
                    <major>BigDataFinance</major>
                </user1>
                <user2>
                    <name>Jane</name>
                    <number>202539284</number>
                    <major>Business</major>
                </user2>
            </body>
        </head>
        """)

root = ET.fromstring(data)

#print(root.find('body').find('user1').find('name').text) #David
for x in range(2):
    print(root.findtext(f'body/user{x+1}/name')) #David\nJane

for name in root.find('body').find('user1'):
    print(name.tag, '//', name.text)