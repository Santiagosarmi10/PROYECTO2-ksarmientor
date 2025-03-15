from app import create_app, db
from app.models import Producto, Ingrediente

app = create_app()

with app.app_context():
    # Crear ingredientes
    fresa = Ingrediente("Fresa", 1000, 50, True, 20)
    chocolate = Ingrediente("Chocolate", 1500, 80, True, 15)
    vainilla = Ingrediente("Vainilla", 1200, 60, True, 25)
    almendras = Ingrediente("Almendras", 800, 70, True, 10)
    
    db.session.add_all([fresa, chocolate, vainilla, almendras])
    db.session.commit()

    # Crear productos con 3 ingredientes
    copa_clasica = Producto("Copa Clásica", 5000, "Helado con toppings clásicos.", "https://via.placeholder.com/150", fresa, chocolate, vainilla)
    malteada_vainilla = Producto("Malteada Vainilla", 7000, "Malteada cremosa de vainilla.", "https://via.placeholder.com/150", vainilla, almendras, chocolate)

    db.session.add_all([copa_clasica, malteada_vainilla])
    db.session.commit()

    print("Ingredientes y productos insertados con éxito.")
