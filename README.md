#### Prueba técnica quick

- clonar el repositorio -> https://github.com/Danielmc09/pruebaquick.git
- crear un entorno virtual  -> virtualenv name_env
- activar entorno virtual 
- instalar librerias  ->  (env) pip install -r requirements.txt 
- ejecutar el proyecto 
- Crear migraciones manage.py makemigrations - manage.py migrate
- crear un usuario en el endpoint -> http://127.0.0.1:8000/clientes/user/

- Puertos a utilizar que no deben estar ocupados o con los servicios locales apagados:
  - Django: 8000

- Endpoints:

|Path|Verb
|----|----
|http://127.0.0.1:8000/clientes/user/|POST
|http://127.0.0.1:8000/login/|POST
|http://127.0.0.1:8000/clientes/clients/|POST
|http://127.0.0.1:8000/clientes/clients/:id|PUT
|http://127.0.0.1:8000/clientes/clients/:id|DELETE
|http://127.0.0.1:8000/productos/products/|POST
|http://127.0.0.1:8000/productos/products/:id|PUT
|http://127.0.0.1:8000/productos/products/:id|DELETE
|http://127.0.0.1:8000/ventas/bills/|POST
|http://127.0.0.1:8000/ventas/bills/:id|PUT
|http://127.0.0.1:8000/ventas/bills/:id|DELETE
|http://127.0.0.1:8000/export/
|http://127.0.0.1:8000/upload/

- el archivo de prueba para el endpoint upload se encuentra en la dirección quick/app/clients/file_csv/ el nombre del archivo es clients.csv

Autor: Angel Daniel Menideta Castillo © 2021
