stacionamientoPy_230758
EstacionamientoPy es una API backend ligera y eficiente diseñada para la gestión integral de sistemas de autolavado. Construida sobre FastAPI, prioriza el alto rendimiento y la facilidad de despliegue.

🌟 Características Principales
API REST Moderna: Desarrollada con FastAPI para aprovechar el tipado de Python y la validación automática de datos.

Documentación Autogenerada: Acceso inmediato a Swagger UI (/docs) y ReDoc (/redoc).

Persistencia Robusta: Integración con bases de datos relacionales (MySQL/MariaDB) mediante SQLAlchemy (ORM).

Configuración Segura: Gestión de variables de entorno mediante archivos .env.

🛠️ Requisitos del Sistema
Python: 3.10 o superior.

Base de Datos: Instancia de MySQL o MariaDB activa.

Dependencias: fastapi, uvicorn, sqlalchemy, pymysql, python-dotenv.

🚀 Instalación y Configuración (Windows)
1. Preparación del Entorno
Abrir una terminal en la raíz del proyecto y ejecutar:

# Crear el entorno virtual
python -m venv entorno

# Activar el entorno
entorno\Scripts\activate

2. Gestión de Dependencias
Instalar los paquetes necesarios:

pip install -r requirements.txt

3. Configuración de Variables de Entorno
Crear un archivo .env en la raíz con la siguiente variable:

DATABASE_URL=mysql+pymysql://root:1234@localhost/autolavadobackend230758

🖥️ Ejecución de la API
Para iniciar el servidor en modo desarrollo:

uvicorn main:app --reload

Punto de acceso API	http://127.0.0.1:8000
Documentación Swagger	http://127.0.0.1:8000/docs