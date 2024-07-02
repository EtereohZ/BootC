Plataforma de Reservación de Citas Médicas

Objetivos:
-Proveer un sitio web amigable para poder agendar tus citas
-Facilitar la relacion entre usuario y medico tratante
-Entregar herramientas para una facil manera de agendar tus horas

Prerequisitos:
asgiref==3.8.1
Django==4.2
django-active-link==0.2.1
psycopg2==2.9.9
sqlparse==0.5.0
typing_extensions==4.12.2
tzdata==2024.1

Ejecución:
-Ingresa a la carpeta donde se encuentra el venv y ejecuta: source venv/scripts/activate
-Entra a la carpeta "webmedico" y ejecuta: python manage.py runserver
-listooo

Carga la base de datos:
python manage.py loaddata reserva_horas/fixtures/centros_medicos.json
python manage.py loaddata reserva_horas/fixtures/especialistas.json 
python manage.py loaddata reserva_horas/fixtures/contact_requests.json
python manage.py loaddata reserva_horas/fixtures/usuarios.json
python manage.py loaddata reserva_horas/fixtures/agendas.json
python manage.py loaddata reserva_horas/fixtures/citas.json

Credenciales de acceso:
Usuario estandar:
- correo: paciente@mail.com
- contraseña : Abc123##

Administrador
-correo:administrador@mail.com
-contraseña: Abc123#

Los usuarios se encuentran en el archivo "usuarios.json" mencionados en el punto anterior