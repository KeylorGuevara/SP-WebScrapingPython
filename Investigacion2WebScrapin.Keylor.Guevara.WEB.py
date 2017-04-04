from urllib import  *
from urllib2 import *
import pymysql
from bs4 import BeautifulSoup
import re
import json
from urllib import  *
import html5lib
import lxml
from pymysql import *
import sys
#Librerias que son necesarias

#Coneccion con la base de datos MySQL
#con esta try except estamos realizando la coneccion con una base de datos local, en este caso mySQL
"""
try:
    conn = pymysql.connect(
        host = '127.0.0.1',
        user = 'root',
        password = None,
        db = 'scraping',
        charset = 'utf8'
    )
except Exception as e:
    sys.exit("No pude conectarme a la BD")
"""

#Scraping de los datos

html = urlopen("http://site.ebrary.com/lib/colecciones/search.action?p00=amor")#link de la pagina de la que tomaremos los datos
bsObj = BeautifulSoup(html,"lxml") #objeto de la clase bs4
content= bsObj.find("div",{"class":"book_item"}).get_text()#definimos que vamos a tomar
n=1

for child in bsObj.findAll("div",{"class":"book_item"}):#para poder tomar la imagen del libro
    for imagen in bsObj.find_all("img", {"alt": "book cover"}):#todos los demas datos
        print (imagen)
        print(child.text)
        print (n, "------------------------------------------------------------------------------------------------")
    n = n + 1