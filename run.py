from app import create_app
from livereload import Server

app = create_app()

if __name__ == '__main__':
    server = Server(app.wsgi_app)

    server.watch('app/templates/*.html')
    server.watch('app/*.py')
    server.watch('app/services.py')

    server.serve(port=5001, debug=True)