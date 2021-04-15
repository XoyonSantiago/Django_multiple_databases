import json

from django.shortcuts import render, redirect
from .models import Estudiante
from datetime import datetime
from django.db.models import Count, Q


# Create your views here.
def home(request):
    record = []
    D = Estudiante.objects.all().order_by('id_estudiante')
    for i in D:
        i.Universidad = 'Default'
        i.base_datos = 'Default'
        record.append(i)
    D = Estudiante.objects.all().using('universidadumg').order_by('id_estudiante')
    for i in D:
        i.Universidad = 'Mariano Galvez'
        i.base_datos = 'PostgreSQL'
        record.append(i)
    D = Estudiante.objects.all().using('universidadsancarlos').order_by('id_estudiante')
    for i in D:
        i.Universidad = 'San Carlos'
        i.base_datos = 'MySQL'
        record.append(i)
    Universidad = list()
    genero_masculino = list()
    genero_femenino = list()
    # cuent = sum(record.genero == 1 for record in record)
    MySQLGenerM = 0
    PostgreSQLGenerM = 0
    DefaultM = 0
    MySQLGenerF = 0
    PostgreSQLGenerF = 0
    DefaultF = 0
    for a in record:
        if a.Universidad not in Universidad:
            Universidad.append(a.Universidad)
        if a.genero == 1:
            if a.base_datos == 'Default':
                DefaultM += 1
            if a.base_datos == 'PostgreSQL':
                PostgreSQLGenerM += 1
            if a.base_datos == 'MySQL':
                MySQLGenerM += 1
        elif a.genero == 2:
            if a.base_datos == 'Default':
                DefaultF += 1
            if a.base_datos == 'PostgreSQL':
                PostgreSQLGenerF += 1
            if a.base_datos == 'MySQL':
                MySQLGenerF += 1
    genero_masculino.append(DefaultM)
    genero_femenino.append(DefaultF)
    genero_masculino.append(PostgreSQLGenerM)
    genero_femenino.append(PostgreSQLGenerF)
    genero_masculino.append(MySQLGenerM)
    genero_femenino.append(MySQLGenerF)
    return render(request, 'dashboard.html', {'default': record,
                                              'Universidad': json.dumps(Universidad),
                                              'masculino': json.dumps(genero_masculino),
                                              'femenino': json.dumps(genero_femenino)})
    # DefaultEstudiantes = Estudiante.objects.all().order_by('id_estudiante')
    # UMGEstudiantes = Estudiante.objects.all().using('universidadumg').order_by('id_estudiante')
    # SanCarlosEstudiantes = Estudiante.objects.all().using('universidadsancarlos').order_by('id_estudiante')
    # print(UMGEstudiantes)
    # return render(request, 'dashboard.html',
    #             {'default': DefaultEstudiantes, 'umg': UMGEstudiantes, 'sc': SanCarlosEstudiantes})


class CEstudiante:
    def crearEstudiante(request):
        if request.method == "POST":
            nombres = request.POST['nombres']
            apellidos = request.POST['apellidos']
            genero = request.POST['inlineRadioOptions']
            fecha_registro = datetime.today().strftime('%Y-%m-%d')
            # print(genero)
            Nombre_DB = request.POST['basedatos']
            print(Nombre_DB)
            obj = Estudiante.objects.using(Nombre_DB).create(nombre_estudiante=nombres, apellido_estudiante=apellidos,
                                                             fecha_nacimiento=fecha_registro, genero=genero)
            obj.save()
            return redirect(home)
        else:
            return render(request, 'crear-estudiante.html')
