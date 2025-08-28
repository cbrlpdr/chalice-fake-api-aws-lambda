from chalice import Chalice

app = Chalice(app_name='pycode-api')


@app.route('/')
def index():
    return {'it': 'works!'}
