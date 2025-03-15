class Heladeria:
    """Clase Heladería que maneja la lista de productos e ingredientes"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.ingredientes = []
    
    def cargar_ingredientes_desde_db(self):
        """Carga todos los ingredientes desde la base de datos al modelo"""
        self.ingredientes = Ingrediente.query.all()

    def cargar_productos_desde_db(self):
        """Carga todos los productos desde la base de datos al modelo"""
        self.productos = Producto.query.all()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def listar_productos(self):
        return [p.nombre for p in self.productos]

    def listar_ingredientes(self):
        return [i.nombre for i in self.ingredientes]
class Heladeria:
    """Clase Heladería que maneja la lista de productos e ingredientes"""
    
    def __init__(self, nombre):
        self.nombre = nombre
        self.productos = []
        self.ingredientes = []
    
    def cargar_ingredientes_desde_db(self):
        """Carga todos los ingredientes desde la base de datos al modelo"""
        self.ingredientes = Ingrediente.query.all()

    def cargar_productos_desde_db(self):
        """Carga todos los productos desde la base de datos al modelo"""
        self.productos = Producto.query.all()

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def agregar_ingrediente(self, ingrediente):
        self.ingredientes.append(ingrediente)

    def listar_productos(self):
        return [p.nombre for p in self.productos]

    def listar_ingredientes(self):
        return [i.nombre for i in self.ingredientes]
