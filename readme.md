# Red de Clínicas Veterinarias (`ae1bim-oct26-feb27`)

Proyecto desarrollado en Python con **SQLite** y **SQLAlchemy ORM** para gestionar una red de clínicas veterinarias, sus consultorios, los médicos veterinarios asignados y las historias clínicas de las mascotas atendidas.

## Tecnologías utilizadas

* **Python 3**
* **SQLite**
* **SQLAlchemy**

## Modelo de entidades

| Entidad | Tabla | Atributos principales | Relación |
| :--- | :--- | :--- | :--- |
| `Clinica` | `clinica` | `id`, `nombre_comercial`, `direccion`, `veterinario_responsable` | Tiene uno o varios `Consultorio` |
| `Consultorio` | `consultorio` | `id`, `nombre_numero`, `especialidad`, `clinica_id` | Pertenece obligatoriamente a una sola `Clinica`; tiene uno o varios `Veterinario` |
| `Veterinario` | `veterinario` | `id`, `nombres`, `apellidos`, `correo`, `numero_licencia`, `consultorio_id` | Pertenece únicamente a un `Consultorio`; elabora varias `HistoriaClinica` |
| `HistoriaClinica` | `historia_clinica` | `id`, `fecha_atencion`, `diagnostico`, `tratamiento`, `nombre_mascota`, `veterinario_id` | Asociada obligatoriamente al `Veterinario` que la elaboró |

## Estructura de archivos

* `configuracion.py`: define la cadena de conexión a la base de datos SQLite (`clinicas_veterinarias.db`).
* `crear_base_entidades.py`: declara las entidades ORM y crea las tablas en SQLite.
* `poblar_base.py`: inserta datos de ejemplo de clínicas, consultorios, veterinarios e historias clínicas.
* `consulta_all.py`: consulta con `all()` que presenta cada clínica y el número de historias clínicas asociadas.
* `consulta_filter.py`: consulta con `filter()` que filtra consultorios por especialidad (`Cirugía`).
* `consulta_order_by.py`: consulta con `order_by()` que ordena las historias clínicas por fecha de atención descendente.
* `consulta_or.py`: consulta con `or_()` que obtiene consultorios de `Dermatología` o `Cirugía`.
* `consulta_and.py`: consulta con `and_()` que filtra historias clínicas por fecha y diagnóstico.

## Instalación y ejecución local

1. Instalar SQLAlchemy:
   ```bash
   py -m pip install sqlalchemy
   ```
   *(En macOS/Linux o Windows con `python` en el PATH, usa `pip install sqlalchemy`.)*

2. Crear la base de datos y las tablas:
   ```bash
   py crear_base_entidades.py
   ```

3. Poblar la base de datos con los registros iniciales:
   ```bash
   py poblar_base.py
   ```

4. Ejecutar las consultas:
   ```bash
   py consulta_all.py
   py consulta_filter.py
   py consulta_order_by.py
   py consulta_or.py
   py consulta_and.py
   ```
## Fork del repositorio en cuenta de Github
https://github.com/Onlytrashhh/ae1bim-oct26-feb27/tree/main