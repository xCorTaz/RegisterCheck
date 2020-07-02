import requests
from Loghead import hea1
req = requests.session()
instalog = 'https://www.instagram.com/accounts/login/ajax/'
dat = {
    'username': 'user',
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1592912810:ASRQAAWmL/OKiq54WTH/H4ZNuVwjbVBWXL0EgGusm/4DDJwr3bmpOSnAKhyHDk10E1KajZr6VkuJh+WGB/mlp4ap9iZNEHpmIWN1SOYzAiH7WGuZ+YJEjFlaz+/WGsowSvwx9tDYlzG3Ks+/+oxv7MPg',
    'queryParams': '{}',
    'optIntoOneTap': 'false'
}
logdata = req.post(instalog, data=dat, headers=hea1).text
if ('"user": false') in logdata:
    print('invalid')
elif ('"user": true') in logdata:
    print('valid')
else:
    print('Something went wrong.')