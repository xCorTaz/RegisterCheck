import requests
from statheader import head
from Loghead import hea1
from reghead import hea3
from tkinter import *
from tkinter import messagebox
w = Tk()
w.withdraw()
usernamelist = open('userlist.txt', 'r')
while True:
    checklist = usernamelist.readline().split('\n')[0]
    instaurl = f'https://www.instagram.com/{checklist}/'
    rq = requests.get(instaurl, headers=head)
    if rq.status_code == 404:
        req = requests.session()
        instalog = 'https://www.instagram.com/accounts/login/ajax/'
        dat = {
            'username': checklist,
            'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1592912810:ASRQAAWmL/OKiq54WTH/H4ZNuVwjbVBWXL0EgGusm/4DDJwr3bmpOSnAKhyHDk10E1KajZr6VkuJh+WGB/mlp4ap9iZNEHpmIWN1SOYzAiH7WGuZ+YJEjFlaz+/WGsowSvwx9tDYlzG3Ks+/+oxv7MPg',
            'queryParams': '{}',
            'optIntoOneTap': 'false'
        }
        logdata = req.post(instalog, data=dat, headers=hea1).text
        if ('"user": false') in logdata:
            print(f'This Username Is Available >> {checklist}')
            instaurlreg = 'https://www.instagram.com/accounts/web_create_ajax/'
            dat = {
                'email': 'email',
                'enc_password': '#PWD_INSTAGRAM_BROWSER:10:1592913500:ASRQACK/ZZ4ReoM5QAuqMP/JG2F7/yYHrA5nSHM1XwgzzSVF5xhKda1zyIA45J9upY+rQPvBCy/IqOk35BWPz5F7sgZ3XcqpMPQcXzomWy5EoLpV5eSNiXhA8PDEDbZ0iKV0e4SNTjpztgrE7A==',
                'username': checklist,
                'first_name': 'adaasf43asf',
                'month': '3',
                'day': '4',
                'year': '2001',
                'seamless_login_enabled': '1',
                'tos_version': 'row'
            }
            regda = req.post(instaurlreg, data=dat, headers=hea3).text
            if ('"message": "checkpoint_required"') in regda:
                print(f'Done Register With >> {checklist}')
                messagebox.showinfo('Checker', f'Done Register With >> {checklist}')
                break
            else:
                print('IP is banned || email is invalid')
        elif ('"user": true') in logdata:
            print(f'This Username Is Banned >> {checklist}')
    elif rq.status_code == 200:
        print(f'This Username Is Not Available >> {checklist}')
