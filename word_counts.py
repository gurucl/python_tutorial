



file_content = open('/Users/gurumurthy.cl/Documents/python_tutorial/resources/text.txt', 'r')
lines = file_content.readlines()

for line in lines:
    print(line.split(' ')[0].lower().replace(',',''))
