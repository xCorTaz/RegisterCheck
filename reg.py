import requests
from reghead import hea3
req = requests.session()
instaurlreg = 'https://www.instagram.com/accounts/web_create_ajax/'
dat = {
    'email': 'email',
    'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1592913500:ASRQACK/ZZ4ReoM5QAuqMP/JG2F7/yYHrA5nSHM1XwgzzSVF5xhKda1zyIA45J9upY+rQPvBCy/IqOk35BWPz5F7sgZ3XcqpMPQcXzomWy5EoLpV5eSNiXhA8PDEDbZ0iKV0e4SNTjpztgrE7A==',
    'username': 'dfgdsrfw4eff4sfg',
    'first_name': 'adaasf43asf',
    'month': '3',
    'day': '4',
    'year': '2001',
    'seamless_login_enabled': '1',
    'tos_version': 'row'
}
regda = req.post(instaurlreg, data=dat, headers=hea3).text
print(regda)