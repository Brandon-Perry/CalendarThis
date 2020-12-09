from flask import Flask, Blueprint, render_template # Ignore this error
import os
import psycopg2

bp = Blueprint('main', __name__, '/')

CONNECTION_PARAMETERS = {
    "user": os.environ.get("DB_USER"),
    "password": os.environ.get("DB_PASS"),
    "dbname": os.environ.get("DB_NAME"),
    "host": os.environ.get("DB_HOST"),
}


@bp.route('/')
def home():
    with psycopg2.connect(**CONNECTION_PARAMETERS) as conn:
        with conn.cursor() as cursor:
            cursor.execute('''
                SELECT id, name, start_datetime, end_datetime
                FROM appointments
                ORDER BY start_datetime
            ''')
            rows = cursor.fetchall()
    return render_template('main.html', rows=rows)
