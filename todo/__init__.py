import os 

from flask import Flask

def create_app(): #Esta funcion es necesaria para aplicaciones en Flask
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY= 'mikey', #Llave para las sesiones de la app
        DATABASE_HOST=os.environ.get('FLASK_DATABASE_HOST'),
        DATABASE_PASSWORD=os.environ.get('FLASK_DATABASE_PASSWORD'), 
        DATABASE_USER=os.environ.get('FLASK_DATABASE_USER'), 
        DATABASE=os.environ.get('FLASK_DATABASE')              
    )

    from . import db

    db.init_app(app)

    from . import auth
    app.register_blueprint(auth.bp)
    
    @app.route("/hola") #Ruta de pruebaste
    def hola():
        return "<p>Hola desde Flask</p>"



    #if __name__ == "__main__":
    #    app.run(debug=True)

    return app
