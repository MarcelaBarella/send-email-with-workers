from bottle import route, run, request

@route('/', method='POST')
def send():
    subject = request.forms.get('subject')
    message = request.forms.get('message')
    return f'Queued message! Subject: {subject}, Message: {message}'

if __name__ == '__main__':
    run(host='0.0.0.0', port=8080, debug=True)
