from flask import Blueprint, render_template
from app.models import Producto

routes = Blueprint('routes', __name__)  # Definimos el Blueprint

@routes.route('/')
def index():
    productos = Producto.query.all()  # Obtener todos los productos de la base de datos
    return render_template('index.html', productos=productos)
