from flask import Flask, jsonify, request
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('data_lake.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/data', methods=['GET'])
def get_data():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    offset = (page - 1) * per_page

    conn = get_db_connection()
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM data_table LIMIT ? OFFSET ?', (per_page, offset))
    rows = cursor.fetchall()

    data = [dict(row) for row in rows]

    conn.close()
    
    return jsonify({
        'page': page,
        'per_page': per_page,
        'data': data
    })

if __name__ == '__main__':
    app.run(debug=True)
