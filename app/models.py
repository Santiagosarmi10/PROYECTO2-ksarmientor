from app import db

class Producto(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(100), nullable=False)
    precio = db.Column(db.Float, nullable=False)
    descripcion = db.Column(db.String(255), nullable=True)
    imagen_url = db.Column(db.String(255), nullable=True)  # URL de la imagen

    def __init__(self, nombre, precio, descripcion, imagen_url):
        self.nombre = nombre
        self.precio = precio
        self.descripcion = descripcion
        self.imagen_url = imagen_url
