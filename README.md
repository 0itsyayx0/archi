## proyecto de Gestión de Celulares
Este proyecto es una base para la gestión de celulares y marcas, implementado siguiendo el patrón arquitectónico por capas. Utiliza Python, Flask como framework web y SQLAlchemy como ORM para la interacción con bases de datos relacionales.

## Descripción General
El sistema permite registrar, consultar, actualizar y eliminar celulares, así como gestionar las marcas asociadas a cada celular. La arquitectura por capas facilita la separación de responsabilidades, mejorando la mantenibilidad, escalabilidad y flexibilidad del código. El uso de un ORM como SQLAlchemy permite desacoplar la lógica de negocio de la base de datos, facilitando la portabilidad y la seguridad.

## Características principales
API RESTful para la gestión de celulares y marcas.
Modelos bien definidos y documentados.

Repositorios para el acceso a datos desacoplados de la lógica de negocio.

Documentación detallada para facilitar la comprensión y extensión del sistema.

## Estructura del Proyecto

models/: Definición de los modelos de datos (Celular, Marca) y documentación asociada.

repositories/: Implementación de la capa de acceso a datos (repositorios) y su documentación.

controllers/: Lógica de los endpoints y controladores de la API.

services/: Lógica de negocio y conexión entre controladores y repositorios.

config/: Configuración de la base de datos y utilidades.

app_factory.py: Archivo principal para iniciar la aplicación Flask.

requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.

## Cómo crear un entorno virtual en Python

El uso de un entorno virtual es fundamental para aislar las dependencias del proyecto y evitar conflictos con otras aplicaciones o proyectos en tu sistema. Un entorno virtual te permite instalar paquetes específicos para este proyecto sin afectar el entorno global de Python.

Pasos para crear y activar un entorno virtual:
Instala virtualenv si no lo tienes:

Código
pip install virtualenv  
Crea el entorno virtual:

Código
python -m venv venv  
Esto creará una carpeta llamada venv en el directorio del proyecto.

Activa el entorno virtual:

En Linux/Mac:

Código
source venv/bin/activate  
En Windows:

Código
venv\Scripts\activate  
Instala las dependencias del proyecto:

Código
pip install -r requirements.txt  
Importancia de usar un entorno virtual
Aislamiento: Evita conflictos entre dependencias de diferentes proyectos.

Reproducibilidad: Permite que otros desarrolladores instalen exactamente las mismas versiones de las librerías.

Facilidad de despliegue: Simplifica la migración y despliegue en diferentes entornos (desarrollo, pruebas, producción).

Limpieza: Mantiene tu instalación global de Python libre de paquetes innecesarios.

## Contribuciones

Si deseas contribuir, por favor sigue las buenas prácticas de documentación y arquitectura ya establecidas en el proyecto. ¡Toda mejora es bienvenida!

## Licencia
Este proyecto es de uso libre para fines educativos y de aprendizaje.