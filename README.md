# api-20v-flask

# 🌐 Blog App: Flask, Bootstrap, y HTMLX

Este proyecto es una aplicación web de blog simple construida con **Flask**, Jinja2 para la creación de plantillas, **Bootstrap 5** para el diseño moderno y **HTMX** para la interactividad asíncrona (AJAX).

---

## ⚙️ Configuración y Ejecución

Sigue estos pasos para poner en marcha la aplicación.

### 1. Clonar y Configurar el Entorno Virtual

```bash
# 1. Clonar el repositorio

# 2. Crear y activar el entorno virtual
python -m venv venv
# Windows: .\venv\Scripts\activate
# Linux/macOS: source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# Realizar los ajustes requeridos para trabajar con SQLite u otra base de datos.

## IMPORTANTE PARA LA EJECUCION DEL APLICATIVO:
# Asegúrate de que FLASK_APP apunte a tu archivo de inicio en la terminal
# 1. Indica a Flask que tu aplicación está en main.py
export FLASK_APP=main.py

# 2. (Opcional) Activa el modo desarrollo/debug
export FLASK_ENV=development 

# 3. Ejecuta la aplicación
flask run
