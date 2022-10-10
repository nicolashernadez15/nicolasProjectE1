from django.shortcuts import render

# Create your views here.

def index (request):
    data ={
        "nombre": 'Nicolas',
        "apellido": 'Hernandez Verdugo',
        "profesion": 'estudiante',
        "edad": '23 Años',
        "img": '/static/foto.jpg',
        }

    return render (request, 'index.html',data)
    

def projecto1(request):
    data = {
        "img":'/static/web.jpg',
        "proyecto":'Desarrollo de pagina web',
        "detalle": 'Desarrollo de un pagina web con el objetivo de resolver una problematica',
        "cliente": 'Dueno de empresa comercial "jat',
        "año": 2022,
        "Tipo":'Proyecto privado',
        "Clasificaion":'publicidad',
        "Financiamiento": 200.000,
        "link": 'https://www.youtube.com'
        

    }
    return render (request, 'projectos.html',data ) 

def projecto2(request):
    data = {
        "img":'/static/sofware.png',
        "proyecto":'Desarrollo de software',
        "detalle": 'Desarrollo de software con el objetivo de resolver una problematica',
        "cliente": 'Dueno de empresa comercial privada',
        "año": 2015,
        "Tipo":'Proyecto privado',
        "Clasificaion":'ventas',
        "Financiamiento": 300.000,
        "link": 'https://www.youtube.com'


    }
    return render (request, 'projectos.html',data ) 


def projecto3(request):
    data = {
        "img":'/static/app.png',
        "proyecto":'Desarrollo de APP',
        "detalle": 'Desarrollo de una APP con el objetivo de realizar reservas de horas',
        "cliente": 'Dueno de empresa comercial "TATA"',
        "año": 2022,
        "Tipo":'Proyecto privado',
        "Clasificaion":'publicidad',
        "Financiamiento": 200.000,
        "link": 'https://www.youtube.com'


    }
    return render (request, 'projectos.html',data) 