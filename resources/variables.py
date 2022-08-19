xpath_start = '/html/body/div//*'
csv_name = 'outputs/CSV_xpaths.csv'
json_name = 'outputs/JSON_xpaths.json'
# URL = 'http://www.degalukainos.lt/'
URL = 'https://www.messenger.com/'

login_name_samples = ['email', 'gmail', 'username', 'user-name', 'name', 'user_name', 'phone', 'number', 'phonenumber',
                      'phone_number', 'uname', 'Enter Username', 'Email or phone number', 'paštas', 'el.paštas',
                      'El. pašto adresas arba telefono numeris', 'pastas', 'el.pastas', 'el_pastas', 'numeris',
                      'telefono numeris', 'tel.numeris', 'prisijungimo vardas', 'slapyvardis', 'telefonas', 'mobilusis',
                      'user_id', 'user-id', 'user id', 'user']
login_password_samples = ['pass', 'password', 'Slaptažodis', 'psw', 'Enter your password']

login_name_pass = login_name_samples+login_password_samples
# print(login_name_pass)