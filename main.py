from app import app, db
from app.models import Name, Surname, Street, City

@app.shell_context_processor
def make_shell_context():
    return {
        'db': db,
        'Name': Name,
        'Surname': Surname,
        'Street': Street,
        'City': City
    }
