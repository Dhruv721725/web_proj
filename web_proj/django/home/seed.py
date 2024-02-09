from faker import Faker
fake=Faker()
import random
from home.models import *
def seed_db(n=10)->None:
    try:
        for i in range(n):
            li=Department.objects.all()
            department=random.choice(li)
            id=random.randint(1,999)
            if len(str(id))==1:
                st_id='STU-00'+str(id)
            elif len(str(id))==2:
                st_id='STU-0'+str(id)
            else:
                st_id='STU-'+str(id)
            st_name=fake.name()
            st_email=fake.email()
            st_age=random.randint(18,25)
            st_address=fake.address()

            st_id=StudentId.objects.create(st_id=st_id)
            Student.objects.create(
                department=department,
                st_id=st_id,
                st_name=st_name,
                st_email=st_email,
                st_age=st_age,
                st_address=st_address)
    except Exception as e:
        print(e)
def seed_marks():
    try:
        sts=Student.objects.all()
        for i in sts:
            subs=Sub.objects.all()
            for j in subs:
                marks=random.randint(50,90)
                Sub_marks.objects.create(
                    st_name=i,
                    sub_name=j,
                    marks=marks)
                
    except Exception as e:
        print(e)
