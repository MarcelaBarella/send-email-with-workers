from bottle import route, run, request
import psycopg2

DSN = 'dbname=email_sender user=postgres host=db'
SQL = 'INSERT INTO emails (subject, message) VALUES (%s, %s)'

def register_message(subject, message):
    conn = psycopg2.connect(DSN)
    cur = conn.cursor()
    cur.execute(SQL, (subject, message))
    conn.commit()
    cur.close()
    conn.close()

    print('Registered Message!')

@route('/', method='POST')
def send():
    subject = request.forms.get('subject')
    message = request.forms.get('message')

    register_message(subject, message)

    return f'Queued message! Subject: {subject}, Message: {message}'

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
