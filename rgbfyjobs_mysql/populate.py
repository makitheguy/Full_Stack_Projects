import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','rgbfyjobs_mysql.settings')

import django
django.setup()

from testapp.models import noida
# from faker import Faker
from faker import Faker
from random import *
fake = Faker()

def phonenumbergen():
    di = randint(7,9)
    num = ''+str(di)
    for i in range(9):
        num =num+str(randint(0,9))
    return int(num)


def populate(n):
    for i in range(n):
        fdate = fake.date()
        fcompany = fake.company()
        ftitle = fake.random_element(elements=('Project Manager', 'Software engineer', 'Team Lead'))
        feligibility = fake.random_element(elements=('B.tech', 'M.Tech', 'MCA','Phd'))
        faddress = fake.address()
        femail = fake.email()
        fphonenumber = phonenumbergen()
        noida_records = noida.objects.get_or_create(date=fdate,company = fcompany,title =ftitle,
                                                    eligibility=feligibility,address = faddress,
                                                    email=femail,phonenumber = fphonenumber)

populate(25)
