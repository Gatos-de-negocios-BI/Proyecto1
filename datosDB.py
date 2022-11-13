import csv
import os
import random
from random import randrange
from datetime import timedelta
from datetime import datetime
import requests
from random import randint

usuarios = []
for n in range(0, 200):
    usuarios.append('usuario'+str(n))
        
def random_date(start, end):
    delta = end - start
    int_delta = (delta.days * 24 * 60 * 60) + delta.seconds
    random_second = randrange(int_delta)
    return start + timedelta(seconds=random_second)

d1 = datetime.strptime('1/1/2010 1:30 PM', '%m/%d/%Y %I:%M %p')
d2 = datetime.strptime('1/1/2022 4:50 AM', '%m/%d/%Y %I:%M %p')

file = open("./data/inserts.sql", "w", encoding="utf-8")
insert="insert into publicacion (text, date, person, classification) values ('{}','{}','{}','{}');"

ruta = "./data/SuicidiosProyecto.csv"
with open(ruta, encoding="utf-8") as File:  

    reader = csv.reader(File)
    id=0
    for row in reader:
        if id == 0:
            id+=1
        else:
            fecha=random_date(d1, d2)
            usuario= random.choice(usuarios)
            texto=row[1].replace('"','').replace("'",'')
            file.write(insert.format(texto,fecha,usuario, row[2]) + os.linesep)

file.close()