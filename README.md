# archi

Proyecto de Gestión de Archivos

Este proyecto es una base para la gestión y control de archivos digitales, implementado siguiendo el patrón arquitectónico por capas. Utiliza Python, Flask como framework web y SQLAlchemy como ORM para la interacción con bases de datos relacionales.

Descripción General

El sistema permite registrar, consultar, actualizar y eliminar archivos dentro de una base de datos, además de almacenar información relacionada como nombre, tipo, tamaño, fecha de carga y usuario responsable.
La arquitectura por capas facilita la separación de responsabilidades, mejorando la mantenibilidad, escalabilidad y seguridad del sistema.

El uso de un ORM como SQLAlchemy permite desacoplar la lógica de negocio de la base de datos, haciendo que la aplicación sea portable, segura y fácil de extender.

Características principales

API RESTful para la gestión completa de archivos.

Modelos bien definidos y documentados para garantizar integridad y claridad.

Repositorios desacoplados de la lógica de negocio, facilitando el mantenimiento.

Controladores organizados que manejan las operaciones CRUD y validaciones.

Documentación clara y completa, pensada para la comprensión y extensión del sistema.

Estructura del Proyecto

models/: Contiene los modelos de datos (File, User, etc.) y sus relaciones.

repositories/: Implementa la capa de acceso a datos (repositorios) encargada de interactuar con la base de datos.

controllers/: Incluye la lógica de los endpoints y controladores de la API.

config/: Configuración de la base de datos y variables del entorno.

requirements.txt: Lista de dependencias necesarias para ejecutar el proyecto.