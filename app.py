from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/category/<category>')
def category(category):
    return render_template(f'{category}.html')

# Ruta para el abecedario
@app.route('/abecedario')
def abecedario():
    return render_template('abecedario.html')

# Ruta dinámica para cada letra
@app.route('/letra/<letra>')
def mostrar_letra(letra):
    # Ruta para el video y el sonido correspondientes a la letra
    video_url = f'/static/videos/{letra.upper()}.mp4'
    sound_url = f'/static/sounds/{letra.upper()}.mp3'

    return render_template(
        'letra.html',
        letra=letra.upper(),
        video_url=video_url,
        sound_url=sound_url
    )

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
