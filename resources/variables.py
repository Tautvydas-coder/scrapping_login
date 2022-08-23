xpath_start = '/html/body//*'
csv_name = 'outputs/CSV_xpaths.csv'
json_name = 'outputs/JSON_xpaths.json'
# URL = 'http://www.degalukainos.lt/'
# URL = 'https://www.messenger.com/'
# URL = 'https://demoqa.com/login/'
# URL = 'https://sso.teachable.com/secure/9521/identity/login/password'
URL = 'https://login.salesforce.com/?startURL=%2Fsetup%2Fsecur%2FRemoteAccessAuthorizationPage.apexp%3Fsource%3DCAAAAYK2gDxgMDAwMDAwMDAwMDAwMDAwAAAA7oMNqZCWZ82wM4tQNKFUckyxRNNHkrl4pKC7dkwLlh5j9v9RcGQNAeiVx8m0s5Rf624vinXkkUTn0Ph9_NnPM-Ws5T69Cc-p6dsji9GWoHQkMmdQ_vPqonFL-i3pD3Ggaw-0pZkK60QmNSsDHeiuYhzxgtmyMLdsrnyoQHYHuKKS9xZ_GMR5s64jg6MosgY8QTrwO1mWeizvHH9Lz7MhQfBBga7fZ-nXVhmJbUt6CWd4DjStgkV-jbH87-fe-DLgPgC-jBOVgvdTn-dGnpYFLZ8Yw74HIA1tVEXaNBPrLKUDQs8V9ijaTfLo5V8ERyNp3AAS5bbSeCbbniat4O7TrN0752gmiEvYVoHfQL4KwuaKd29DXcI-DUc-DiGyaw5Xv1ZUWchRk_4KFZMHplKnDg_F_pT4NFX4Vkzut3ZC7ikDD3l85_PgUwgEH4z0MxJiGshmr2bKWO4j5OqR49D9zuGcFWAvWA6FBsoHoE9FLd4bzd_FYu5WR8mWMbicUdn7MCASBvEqjoQYzafgurM7CY5zKAICHIXmU-x83fY39rzZvTK7cf3gG_p0pyAyill2bmHy41_GmST0XSku6JUmiOKwGMToqkTXELlxuy3JCvYVfkAWSrvI-_xhEuznKmN9JEHx8E4ylhCojV7c_PDFn2_Y8o3qhpxYnebOaJN6sIDvt59vq6kECZNr4JqIAsldACnLLa8VqJOvDrAqoD1jPoG3FC1dg7lDIYUKUH8G3NRdIZ0IQDxBirca1PSESjyJgNz9gqS0pXzLKB5IaobzhWT5eZX3Po2sHGLCiI_rFIFgUKQwPajQUz1WGsILEoiMprXWwPRktne_p-iXhUXna7ZBg2femk62Gv1ooFaCeoWHujWJgpom3n-njfd-T4LljML-LKzf16qlr5zWwxNt-gnrwVjMQ-gI-yCxOlb9yHOiDzRezOUDJtdMrBzCcqiOH6osAvu0ythNZbivcv4CyhGskLVjkbRcq_BhsF7h8dN4No88Zjspwj8F2YmG1Gl4BPDlBLqazVj1tgi_s8MGWMA%253D&sdtd=1'
# URL ='https://www.linkedin.com/login?fromSignIn=true&session_redirect=https%3A%2F%2Fwww.linkedin.com%2Fjobs&trk=guest_homepage-jobseeker_nav-header-signin'
# TODO permesti i kita csv faila, kuri nuskaitytu
login_name_samples = ['email', 'gmail', 'username', 'user-name', 'name', 'user_name', 'phone', 'number', 'phonenumber',
                      'phone_number', 'uname', 'Enter Username', 'Email or phone number', 'paštas', 'el.paštas',
                      'El. pašto adresas arba telefono numeris', 'pastas', 'el.pastas', 'el_pastas', 'numeris',
                      'telefono numeris', 'tel.numeris', 'prisijungimo vardas', 'slapyvardis', 'telefonas', 'mobilusis',
                      'user_id', 'user-id', 'user id', 'user', 'Email address or username', 'login-username',
                      'userName', 'UserName','Email address or username','Username','Email or Phone']
login_password_samples = ['pass', 'password', 'Slaptažodis', 'psw', 'Enter your password', 'login-password','Password']
# /html/body/div[2]/div/div/div[2]/div[2]/div[2]/form/div[2]/div[2]/input
login_name_pass = login_name_samples + login_password_samples
# print(login_name_pass)
