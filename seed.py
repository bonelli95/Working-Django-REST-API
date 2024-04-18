import os, django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'setup.settings')
django.setup()

from faker import Faker
import random, datetime
from school.models import  Student, Course, Enrollment

def creating_students(amount_people):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(amount_people):
        name = fake.name()
        pin = "{}{}{}{}".format(random.randrange(10, 99),random.randrange(100, 999),random.randrange(100, 999),random.randrange(0, 9) ) 
        tin = fake.random_number(digits=9)
        date_birth = fake.date_between(start_date='-18y', end_date='today')
        a = Student(name=name,pin=pin, tin=tin, date_birth=date_birth)
        a.save()

def creating_course(amount_course):
    fake = Faker('pt_BR')
    Faker.seed(10)
    for _ in range(amount_course):
        code_course = "{}{}-{}".format(random.choice("ABCDEF"), random.randrange(10, 99),random.randrange(1, 9))
        descs = ['Python Fundamentals', 'Intermediate Python','Advanced Python', 'Python for Data Science', 'Python/React']
        description = random.choice(descs)
        descs.remove(description)
        level = random.choice("BIA")
        c = Course(code_course=code_course,description=description, level=level)
        c.save()


creating_students(200)
creating_course(5)