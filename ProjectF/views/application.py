from bottle import Bottle, request, template
from database import create_tables, execute_query

app = Bottle()

@app.route('/')
def index():
    universities = execute_query('SELECT * FROM University')
    return template('index', universities=universities, update_id=None, update_name='', update_location='')

@app.route('/add', method='POST')
def add():
    name = request.forms.get('name')
    location = request.forms.get('location')

    execute_query('INSERT INTO University (name, location) VALUES (?, ?)', (name, location))
    return index()

@app.route('/delete/<university_id>')
def delete(university_id):
    execute_query('DELETE FROM University WHERE id = ?', (university_id,))
    return index()

@app.route('/update/<university_id>')
def update(university_id):
    university = execute_query('SELECT * FROM University WHERE id = ?', (university_id,))
    return template('index', universities=[], update_id=university[0][0], update_name=university[0][1], update_location=university[0][2])

if __name__ == '__main__':
    create_tables()
    app.run(debug=True)
