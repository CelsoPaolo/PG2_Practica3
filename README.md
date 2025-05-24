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

## Referencia de Endpoints Públicos

Todos los endpoints base se encuentran bajo el prefijo `/api/`. No se requiere autenticación para acceder a estos endpoints, lo que los hace completamente públicos y facilitando las operaciones CRUD (Crear, Leer, Actualizar, Eliminar).

### 1. Unidades de Medida ( `/api/unidadesdemedida/` )

Gestiona las diferentes unidades de medida utilizadas en la API.

* **`GET /api/unidadesdemedida/`**
    * **Descripción**: Lista todas las unidades de medida.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            {"id": 1, "simbolo": "g", "nombre_completo": "Gramo", "tipo_unidad": "Peso"}
        ]
        ```

* **`POST /api/unidadesdemedida/`**
    * **Descripción**: Crea una nueva unidad de medida.
    * **Argumentos (Body - JSON):**
        ```json
        {"simbolo": "kcal", "nombre_completo": "Kilocaloría", "tipo_unidad": "Energía"}
        ```

* **`GET /api/unidadesdemedida/{id}/`**
    * **Descripción**: Recupera una unidad de medida específica.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        {"id": 1, "simbolo": "g", "nombre_completo": "Gramo", "tipo_unidad": "Peso"}
        ```

* **`PUT /api/unidadesdemedida/{id}/`**
    * **Descripción**: Actualiza completamente una unidad de medida.
    * **Argumentos**: Body (JSON) con todos los campos.

* **`PATCH /api/unidadesdemedida/{id}/`**
    * **Descripción**: Actualiza parcialmente una unidad de medida.
    * **Argumentos**: Body (JSON) con los campos a actualizar.

* **`DELETE /api/unidadesdemedida/{id}/`**
    * **Descripción**: Elimina una unidad de medida. (Respuesta: `204 No Content`)

### 2. Grupos Alimenticios ( `/api/gruposalimenticios/` )

Clasifica los alimentos en grupos nutricionales.

* **`GET /api/gruposalimenticios/`**
    * **Descripción**: Lista todos los grupos alimenticios.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            {"id": 1, "nombre": "Frutas", "descripcion": "Fuentes de vitaminas y fibra."}
        ]
        ```

* **`POST /api/gruposalimenticios/`**
    * **Descripción**: Crea un nuevo grupo alimenticio.
    * **Argumentos (Body - JSON):**
        ```json
        {"nombre": "Vegetales", "descripcion": "Ricos en nutrientes."}
        ```

*(Las operaciones `GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/` y `DELETE /{id}/` funcionan de manera análoga al endpoint de Unidades de Medida.)*

### 3. Alimentos ( `/api/alimentos/` )

Detalles específicos de cada alimento.

* **`GET /api/alimentos/`**
    * **Descripción**: Lista todos los alimentos.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            {"id": 1, "nombre": "Manzana", "grupo": 1, "descripcion_breve": "Fruta común."}
        ]
        ```
* **`POST /api/alimentos/`**
    * **Descripción**: Crea un nuevo alimento.
    * **Argumentos (Body - JSON):**
        ```json
        {"nombre": "Pollo (pechuga)", "grupo": 2, "descripcion_breve": "Proteína magra."}
        ```
*(Las operaciones `GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/` y `DELETE /{id}/` funcionan de manera análoga al endpoint de Unidades de Medida.)*

### 4. Nutrientes ( `/api/nutrientes/` )

Información sobre los diferentes nutrientes.

* **`GET /api/nutrientes/`**
    * **Descripción**: Lista todos los nutrientes.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            {"id": 1, "nombre": "Calorías", "es_macro": true, "unidad_medida_estandar": 2}
        ]
        ```

* **`POST /api/nutrientes/`**
    * **Descripción**: Crea un nuevo nutriente.
    * **Argumentos (Body - JSON):**
        ```json
        {"nombre": "Proteína", "es_macro": true, "unidad_medida_estandar": 1}
        ```
*(Las operaciones `GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/` y `DELETE /{id}/` funcionan de manera análoga al endpoint de Unidades de Medida.)*

### 5. Valores Nutricionales ( `/api/valoresnutricionales/` )

Contenido nutricional de los alimentos.

* **`GET /api/valoresnutricionales/`**
    * **Descripción**: Lista todos los valores nutricionales.
    * **Ejemplo de Respuesta (200 OK):**
        ```json
        [
            {"id": 1, "alimento": 1, "nutriente": 1, "unidad_medida": 2, "cantidad": 52.0}
        ]
        ```

* **`POST /api/valoresnutricionales/`**
    * **Descripción**: Crea un nuevo valor nutricional para un alimento.
    * **Argumentos (Body - JSON):**
        ```json
        {"alimento": 2, "nutriente": 1, "unidad_medida": 1, "cantidad": 25.0, "referencia_por_cantidad": "por 100g", "cantidad_referencia": 100.0}
        ```
*(Las operaciones `GET /{id}/`, `PUT /{id}/`, `PATCH /{id}/` y `DELETE /{id}/` funcionan de manera análoga al endpoint de Unidades de Medida.)*

---
## 🚀 Ejemplo de Caso de Uso del API: Cálculo Nutricional de una Receta Simple

Este ejemplo ilustra cómo un desarrollador podría utilizar la API para gestionar y calcular el contenido nutricional de una receta básica, como una "Ensalada de Pollo y Manzana".

**Objetivo del Caso de Uso:** Determinar la cantidad total de **Proteínas** y **Calorías** en una porción específica de "Ensalada de Pollo y Manzana", asumiendo las siguientes cantidades:
* **Manzana:** 150 gramos
* **Pollo (Pechuga):** 120 gramos

Para lograr esto, necesitamos interactuar con casi todos los endpoints de la API, siguiendo un flujo lógico: primero crear los datos base (unidades, grupos, nutrientes, alimentos) y luego sus valores nutricionales, para finalmente consultarlos.

### Flujo de Interacción con los Endpoints:

1.  **Paso 1: Preparar Unidades de Medida Iniciales**
    * **Propósito:** Registrar las unidades que se usarán para nutrientes y cantidades de alimentos.
    * **Endpoints Usados:**
        * **`POST /api/unidadesdemedida/`**:
            * Se usa para crear "Gramo" (ej. ID 1) con body `{"simbolo": "g", "nombre_completo": "Gramo", "tipo_unidad": "Peso"}`.
            * Se usa para crear "Kilocaloría" (ej. ID 2) con body `{"simbolo": "kcal", "nombre_completo": "Kilocaloría", "tipo_unidad": "Energía"}`.

2.  **Paso 2: Definir Grupos Alimenticios**
    * **Propósito:** Clasificar los alimentos que se añadirán.
    * **Endpoints Usados:**
        * **`POST /api/gruposalimenticios/`**:
            * Se usa para crear "Frutas" (ej. ID 1) con body `{"nombre": "Frutas", "descripcion": "Frutas."}`.
            * Se usa para crear "Proteínas" (ej. ID 2) con body `{"nombre": "Proteínas", "descripcion": "Alimentos ricos en proteínas."}`.

3.  **Paso 3: Registrar Nutrientes Clave**
    * **Propósito:** Definir los nutrientes específicos que se rastrearán (Proteínas y Calorías).
    * **Endpoints Usados:**
        * **`POST /api/nutrientes/`**:
            * Se usa para crear "Proteína" (ej. ID 1) con body `{"nombre": "Proteína", "descripcion": "Macronutriente.", "es_macro": true, "unidad_medida_estandar": 1}` (referencia a "Gramo" de Unidades de Medida).
            * Se usa para crear "Calorías" (ej. ID 2) con body `{"nombre": "Calorías", "descripcion": "Unidad de energía.", "es_macro": true, "unidad_medida_estandar": 2}` (referencia a "Kilocaloría" de Unidades de Medida).

4.  **Paso 4: Añadir los Alimentos de la Receta**
    * **Propósito:** Registrar los alimentos principales de la ensalada.
    * **Endpoints Usados:**
        * **`POST /api/alimentos/`**:
            * Se usa para crear "Manzana" (ej. ID 1) con body `{"nombre": "Manzana", "descripcion_breve": "Fruta común.", "es_procesado": false, "fuente_datos": "USDA", "fecha_ultima_actualizacion": "2025-05-24", "grupo": 1}` (referencia a "Frutas").
            * Se usa para crear "Pollo (Pechuga)" (ej. ID 2) con body `{"nombre": "Pollo (Pechuga)", "descripcion_breve": "Pechuga sin piel.", "es_procesado": false, "fuente_datos": "USDA", "fecha_ultima_actualizacion": "2025-05-24", "grupo": 2}` (referencia a "Proteínas").

5.  **Paso 5: Asignar Valores Nutricionales a los Alimentos**
    * **Propósito:** Definir la composición nutricional (proteínas y calorías) por cada 100g de manzana y pollo.
    * **Endpoints Usados:**
        * **`POST /api/valoresnutricionales/`**:
            * **Para Manzana:**
                * Proteínas: Body `{"alimento": 1, "nutriente": 1, "unidad_medida": 1, "cantidad": 0.3, "referencia_por_cantidad": "por 100g", "cantidad_referencia": 100.0, "porcentaje_vd": null}` (0.3g de Proteína por 100g).
                * Calorías: Body `{"alimento": 1, "nutriente": 2, "unidad_medida": 2, "cantidad": 52.0, "referencia_por_cantidad": "por 100g", "cantidad_referencia": 100.0, "porcentaje_vd": null}` (52 kcal por 100g).
            * **Para Pollo:**
                * Proteínas: Body `{"alimento": 2, "nutriente": 1, "unidad_medida": 1, "cantidad": 25.0, "referencia_por_cantidad": "por 100g", "cantidad_referencia": 100.0, "porcentaje_vd": null}` (25g de Proteína por 100g).
                * Calorías: Body `{"alimento": 2, "nutriente": 2, "unidad_medida": 2, "cantidad": 165.0, "referencia_por_cantidad": "por 100g", "cantidad_referencia": 100.0, "porcentaje_vd": null}` (165 kcal por 100g).

6.  **Paso 6: Realizar Consultas para el Cálculo de la Receta**
    * **Propósito:** Obtener los valores nutricionales registrados para cada alimento y calcular el total para las porciones de la receta.
    * **Endpoints Usados:**
        * **`GET /api/valoresnutricionales/?alimento=1`**: Se usa para obtener todos los valores nutricionales de la Manzana (ID 1).
        * **`GET /api/valoresnutricionales/?alimento=2`**: Se usa para obtener todos los valores nutricionales del Pollo (ID 2).

    * **Cálculo (Lógica de la Aplicación Cliente):**
        * **Manzana (150g):**
            * Proteínas: (0.3g / 100g) * 150g = **0.45g**
            * Calorías: (52.0 kcal / 100g) * 150g = **78 kcal**
        * **Pollo (120g):**
            * Proteínas: (25.0g / 100g) * 120g = **30g**
            * Calorías: (165.0 kcal / 100g) * 120g = **198 kcal**

    * **Resultado Total de la Receta:**
        * **Proteínas Totales:** 0.45g (Manzana) + 30g (Pollo) = **30.45g**
        * **Calorías Totales:** 78 kcal (Manzana) + 198 kcal (Pollo) = **276 kcal**

Este caso de uso demuestra cómo, al poblar la base de datos a través de los endpoints `POST` y luego consultarla con `GET` (utilizando la capacidad de filtrado que ofrece DRF), una aplicación externa puede utilizar esta API para construir funcionalidades complejas como calculadoras nutricionales para recetas.

---
