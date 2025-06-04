# PG2_Practica3

# Api Alimentos 

Esta API pública proporciona un conjunto de herramientas robustas para la gestión y consulta de datos relacionados con **alimentos, su composición nutricional, y sistemas de clasificación**. Está diseñada para ser una fuente centralizada de información sobre nutrición, ideal para ser integrada en aplicaciones móviles, web o de análisis de datos que requieran acceso a:

* **Detalles de Alimentos:** Información específica sobre una amplia variedad de alimentos, incluyendo su origen (procesado/no procesado), descripción y clasificación.
* **Composición Nutricional:** Datos precisos sobre la cantidad de diversos nutrientes (macronutrientes y micronutrientes) presentes en los alimentos, especificados por diferentes unidades de medida y cantidades de referencia.
* **Clasificaciones Estándar:** Gestión de unidades de medida (gramos, mililitros, calorías, etc.) y la organización de alimentos en grupos alimenticios (frutas, proteínas, vegetales, etc.) para facilitar la búsqueda y el análisis.

El principal objetivo de esta API es ofrecer una base de datos nutricional estructurada y de fácil acceso, que pueda ser utilizada para:
* Desarrollo de aplicaciones de seguimiento dietético y planificación de comidas.
* Creación de herramientas de análisis nutricional para profesionales de la salud.
* Población de catálogos de alimentos en plataformas de comercio electrónico o restaurantes.
* Proyectos de investigación y educación sobre hábitos alimenticios.

# Diagrama de modelos 
Aca nuestro objetivo es hacer un diagrama de entidad relacion, para eso necesitamos sacar las entidades, atributos y relaciones de nuestra Api, para eso antes tenemos que creear nuestro enterno virtual y activarlo

# Crear entorno virtual
```bash
python -m venv env
```
# Activar entorno

```bash
.\env\Scripts\activate
```

Despues creamos el archivo requirements.txt

# Dentro el archivo

```python
django == 5.2
django-extensions == 4.1
djangorestframework == 3.16.0
 ```

# Crea proecto Django

```bash
django-admin startproject apisenderismo
```

# Iniciamos la app

```bash
python manage.py startapp ruta
```

y con esto ya se nos habran creado varios archivos dentro de el nomber de apisenderismo y ruta, dentro del archivo ruta, buscamos un archivo .py que diga models y dentro de ahi ponemos las entidades de nuestra Api junto con sus atributos y relaciones

# Ejemplo del archivo models
```python
class Alimento(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Alimento")
    descripcion_breve = models.TextField(blank=True, null=True, verbose_name="Descripción Breve")
    imagen_url = models.URLField(blank=True, null=True, verbose_name="URL de Imagen")
    es_procesado = models.BooleanField(default=False, verbose_name="Es Procesado")
    fuente_datos = models.CharField(max_length=100, verbose_name="Fuente de Datos")
    fecha_ultima_actualizacion = models.DateField(default=timezone.now, verbose_name="Fecha Última Actualización")
    grupo = models.ForeignKey(
        GrupoAlimenticio,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='alimentos', 
        verbose_name="Grupo Alimenticio"
    )

class Nutriente(models.Model):
    nombre = models.CharField(max_length=100, unique=True, verbose_name="Nombre del Nutriente")
    descripcion = models.TextField(blank=True, null=True, verbose_name="Descripción")
    es_macro = models.BooleanField(default=False, verbose_name="Es Macronutriente")
    unidad_medida_estandar = models.ForeignKey(
        UnidadDeMedida,
        on_delete=models.PROTECT,
        related_name='nutrientes_con_unidad_estandar', 
        verbose_name="Unidad de Medida Estándar"
    )
```

Despues de haber hecho nos valos al archivo que creamos con el nombre de nuestra Apin en este caso apisenderismo y dentro de ahi buscamos el archivo .py llamados setting y ademas de eso agregaremos una apartado llamado graph_models: 

# Installed Apps
```python 
    'django_extensions',
    'rest_framework',
    'rest_framework.authtoken',
    'ruta',
De momento usaremos dos de estas extensiones que estamos agregando y mas tarde usaremos los otros dos
```

Agregamos debajo de installed apps:

# GRAPH_MODELS
```python
GRAPH_MODELS = {
    'app_labels': ['ruta'],
}
```

Despues de esto ya lo tendriamos listo todo pero antes tenemos que instalar algunas dependencias para que pueda graficar el diagrama 

# INSTALAT DEPENDENCIAS
```bash
pip install pydotplus
pip install django_extensions 
pip install graphviz
```

# Ejecutar el comando para el grafico
```bash
python manage.py graph_models ruta -o diagrama.png
```


# Referencia de Endpoints de la API de Alimentos

Esta documentación detalla los endpoints RESTful disponibles en la API de Alimentos, incluyendo los métodos HTTP, parámetros de consulta (filtros) y la estructura básica del cuerpo de las solicitudes y respuestas.

**Base URL de la API:** `http://127.0.0.1:8000/api/v1/`

---

## 1. Recurso: Unidades de Medida

Representa las unidades de medida utilizadas para los nutrientes y valores.

* **Endpoint:** `/unidades-de-medida/`
* **Campos Relevantes:** `id`, `simbolo`, `nombre_completo`, `tipo_unidad`

### Métodos Disponibles:

* **`GET /`**
    * **Descripción:** Obtener una lista de todas las unidades de medida.
    * **Filtros (Parámetros de Consulta):**
        * `?search=<texto>`: Búsqueda de texto en `nombre_completo`, `simbolo`, `tipo_unidad`.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            { "id": 1, "simbolo": "g", "nombre_completo": "gramos", "tipo_unidad": "peso" }
        ]
        ```

* **`POST /`**
    * **Descripción:** Crear una nueva unidad de medida.
    * **Cuerpo de la Solicitud (JSON):**
        ```json
        {
            "simbolo": "mg",
            "nombre_completo": "miligramos",
            "tipo_unidad": "peso"
        }
        ```
    * **Ejemplo de Respuesta (201 Created):** Objeto creado con su `id`.

* **`GET /{id}/`**
    * **Descripción:** Obtener los detalles de una unidad específica.
    * **Ejemplo:** `GET /api/v1/unidades-de-medida/1/`

* **`PUT /{id}/`**
    * **Descripción:** Actualizar *completamente* una unidad existente (requiere todos los campos).

* **`PATCH /{id}/`**
    * **Descripción:** Actualizar *parcialmente* una unidad existente (solo campos a modificar).

* **`DELETE /{id}/`**
    * **Descripción:** Eliminar una unidad específica.

---

## 2. Recurso: Grupos Alimenticios

Representa las categorías de alimentos (ej., Frutas, Verduras).

* **Endpoint:** `/grupos-alimenticios/`
* **Campos Relevantes:** `id`, `nombre`, `descripcion`

### Métodos Disponibles:

* **`GET /`**
    * **Descripción:** Listar todos los grupos alimenticios.
    * **Filtros (Parámetros de Consulta):**
        * `?search=<texto>`: Búsqueda de texto en `nombre`, `descripcion`.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            { "id": 1, "nombre": "Frutas", "descripcion": "Alimentos dulces y carnosos..." }
        ]
        ```

* **`POST /`**
    * **Descripción:** Crear un nuevo grupo alimenticio.
    * **Cuerpo de la Solicitud (JSON):**
        ```json
        { "nombre": "Verduras", "descripcion": "Plantas o partes de plantas..." }
        ```

* **`GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/`, `DELETE /{id}/`** (para un grupo específico).

---

## 3. Recurso: Alimentos

Representa la información detallada sobre un alimento.

* **Endpoint:** `/alimentos/`
* **Campos Relevantes:** `id`, `nombre`, `descripcion_breve`, `es_procesado`, `fuente_datos`, `grupo` (ID de GrupoAlimenticio)

### Métodos Disponibles:

* **`GET /`**
    * **Descripción:** Listar todos los alimentos.
    * **Filtros (Parámetros de Consulta):**
        * `?search=<texto>`: Búsqueda de texto en `nombre`, `descripcion_breve`, `fuente_datos`.
        * `?es_procesado=true/false`: Filtrar por si es procesado.
        * `?grupo=<id_grupo>`: Filtrar por el ID del grupo alimenticio.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            { "id": 101, "nombre": "Manzana Roja", "es_procesado": false, "grupo": 1 }
        ]
        ```

* **`POST /`**
    * **Descripción:** Crear un nuevo alimento.
    * **Cuerpo de la Solicitud (JSON):**
        ```json
        {
            "nombre": "Pan Integral",
            "descripcion_breve": "Producto horneado...",
            "es_procesado": true,
            "fuente_datos": "Local",
            "grupo": 4
        }
        ```

* **`GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/`, `DELETE /{id}/`** (para un alimento específico).

---

## 4. Recurso: Nutrientes

Representa la información sobre los diferentes nutrientes.

* **Endpoint:** `/nutrientes/`
* **Campos Relevantes:** `id`, `nombre`, `descripcion`, `es_macro`, `unidad_medida_estandar` (ID de UnidadDeMedida)

### Métodos Disponibles:

* **`GET /`**
    * **Descripción:** Listar todos los nutrientes.
    * **Filtros (Parámetros de Consulta):**
        * `?search=<texto>`: Búsqueda de texto en `nombre`, `descripcion`.
        * `?es_macro=true/false`: Filtrar por si es macronutriente.
        * `?unidad_medida_estandar=<id_unidad>`: Filtrar por la unidad de medida estándar.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            { "id": 1, "nombre": "Proteínas", "es_macro": true, "unidad_medida_estandar": 1 }
        ]
        ```

* **`POST /`**
    * **Descripción:** Crear un nuevo nutriente.
    * **Cuerpo de la Solicitud (JSON):**
        ```json
        {
            "nombre": "Vitamina C",
            "descripcion": "Antioxidante.",
            "es_macro": false,
            "unidad_medida_estandar": 3
        }
        ```

* **`GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/`, `DELETE /{id}/`** (para un nutriente específico).

---

## 5. Recurso: Valores Nutricionales

Representa la cantidad de un nutriente en un alimento específico con una unidad de medida.

* **Endpoint:** `/valores-nutricionales/`
* **Campos Relevantes:** `id`, `alimento` (ID), `nutriente` (ID), `unidad_medida` (ID), `cantidad`, `referencia_por_cantidad`, `cantidad_referencia`, `porcentaje_vd`

### Métodos Disponibles:

* **`GET /`**
    * **Descripción:** Listar todos los valores nutricionales.
    * **Filtros (Parámetros de Consulta):**
        * `?alimento=<id_alimento>`: Filtrar por ID de alimento.
        * `?nutriente=<id_nutriente>`: Filtrar por ID de nutriente.
        * `?unidad_medida=<id_unidad>`: Filtrar por ID de unidad de medida.
        * `?cantidad=<valor>`, `?cantidad_referencia=<valor>`, `?porcentaje_vd=<valor>`: Filtrar por valores exactos.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            {
                "id": 1,
                "alimento": 101,
                "nutriente": 1,
                "unidad_medida": 1,
                "cantidad": 0.3,
                "referencia_por_cantidad": "100g",
                "cantidad_referencia": 100.0,
                "porcentaje_vd": null
            }
        ]
        ```

* **`POST /`**
    * **Descripción:** Crear un nuevo valor nutricional.
    * **Cuerpo de la Solicitud (JSON):**
        ```json
        {
            "alimento": 101,
            "nutriente": 4,
            "unidad_medida": 3,
            "cantidad": 5.0,
            "referencia_por_cantidad": "100g",
            "cantidad_referencia": 100.0,
            "porcentaje_vd": 8.0
        }
        ```

* **`GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/`, `DELETE /{id}/`** (para un valor nutricional específico).

---
## 🚀 Ejemplo de Caso de Uso del API: Cálculo Nutricional de una Receta Simple

Este ejemplo ilustra cómo un desarrollador podría utilizar la API para gestionar y calcular el contenido nutricional de una receta básica, como una "Ensalada de Pollo y Manzana".

**Objetivo del Caso de Uso:** Determinar la cantidad total de **Proteínas** y **Calorías** en una porción específica de "Ensalada de Pollo y Manzana", asumiendo las siguientes cantidades:
* **Manzana:** 150 gramos
* **Pollo (Pechuga):** 120 gramos

Para lograr esto, necesitamos interactuar con casi todos los endpoints de la API, siguiendo un flujo lógico: primero crear los datos base (unidades, grupos, nutrientes, alimentos) y luego sus valores nutricionales, para finalmente consultarlos.

# Ejemplo de Caso de Uso: Registrar un Nuevo Alimento y sus Nutrientes

Este ejemplo muestra una secuencia común de interacciones con la API para añadir un nuevo alimento y sus datos nutricionales.

**Objetivo:** Añadir "Kiwi Fresco" con su información nutricional.

**Pasos Clave:**

1.  **Preparar Datos de Referencia:**
    * Verificar o crear **Unidades de Medida** (ej., "gramos", "miligramos") usando `GET /api/v1/unidades-de-medida/` y `POST /api/v1/unidades-de-medida/`.
    * Verificar o crear **Grupos Alimenticios** (ej., "Frutas") usando `GET /api/v1/grupos-alimenticios/` y `POST /api/v1/grupos-alimenticios/`.
    * Verificar o crear **Nutrientes** (ej., "Vitamina C", "Fibra") usando `GET /api/v1/nutrientes/` y `POST /api/v1/nutrientes/`.

2.  **Crear el Alimento:**
    * **Endpoint:** `POST /api/v1/alimentos/`
    * **Cuerpo (JSON):**
        ```json
        {
            "nombre": "Kiwi Fresco",
            "descripcion_breve": "...",
            "es_procesado": false,
            "fuente_datos": "...",
            "grupo": <id_grupo_frutas>
        }
        ```
    * **Resultado:** Obtener el `id` del nuevo alimento (ej., `205`).

3.  **Añadir Valores Nutricionales:**
    * **Endpoint:** `POST /api/v1/valores-nutricionales/` (repetir para cada nutriente).
    * **Cuerpo (JSON):**
        ```json
        {
            "alimento": 205, // ID del "Kiwi Fresco"
            "nutriente": <id_vitamina_c>,
            "unidad_medida": <id_miligramos>,
            "cantidad": 92.7,
            "referencia_por_cantidad": "100g",
            "cantidad_referencia": 100.0,
            "porcentaje_vd": 103.0
        }
        ```
    * **Resultado:** Registrar los detalles nutricionales para Vitamina C, Fibra, Azúcares, etc.

4.  **Verificar (Opcional):**
    * **Endpoint:** `GET /api/v1/alimentos/205/`
    * **Resultado:** Confirmar que "Kiwi Fresco" y sus relaciones nutricionales se muestran correctamente. (Nota: La inclusión de los valores nutricionales directamente en la respuesta del alimento depende de la configuración de tus serializers anidados).

---
