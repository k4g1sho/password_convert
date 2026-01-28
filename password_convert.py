"""
Reads csv password file from firefox export and
converts it to xml file which you can import in Falkon browser.
Remember to delete the password files when done.
"""
from xml.sax.saxutils import escape

# Change this if passowrd.csv is not in the same directory
CSV_FILE_LOCATION = 'passwords.csv'

with open(file=CSV_FILE_LOCATION, mode='r') as file:
    raw_data = file.readlines()

password_data = ['server', 'username', 'password']

password_entries = ''
for element in range(2, len(raw_data)):
    temp = ""
    count = 0
    for key in password_data:
        # Data is only split by lines, Split it further by comma
        string_ = raw_data[element].split(',')[count]
        # Add key and remove the string ""
        # Escape to escape speacial characters such as "" \ etc into xml
        temp+=f'<{key}>{escape(string_[1:-1])}</{key}>'
        count+=1
        temp_entry = f'<entry>{temp}</entry>'
    password_entries += temp_entry

with open(file='passwords.xml',mode='w') as file:
    file.write(
        f'<passwords version="1.0">{password_entries}</passwords>'
        )

