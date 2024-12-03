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

@app.route('/abecedario')
def abecedario():
    return render_template('abecedario.html')

@app.route('/letra/<letra>')
def mostrar_letra(letra):
    video_url = f'/static/videos/{letra.upper()}.mp4'
    sound_url = f'/static/sounds/{letra.upper()}.mp3'
    
    return render_template(
        'letra.html',
        letra=letra.upper(),
        video_url=video_url,
        sound_url=sound_url
    )

@app.route('/numeros')
def numeros():
    return render_template('numeros.html')

@app.route('/numero/<int:numero>')
def mostrar_numero(numero):
    print(f"Intentando mostrar número: {numero}")
    video_url = f'/static/videos/{numero}-gesture.mp4'
    sound_url = f'/static/sounds/{numero}.mp3'
    
    return render_template(
        'numero.html',
        numero=numero,
        video_url=video_url,
        sound_url=sound_url
    )

@app.route('/pronombres')
def pronombres():
    return render_template('pronombres.html')

@app.route('/pronombre/<pronombre>')
def mostrar_pronombre(pronombre):
    video_url = f'/static/videos/{pronombre.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{pronombre.lower()}.mp3'
    
    return render_template(
        'pronombre.html',
        pronombre=pronombre.lower(),
        video_url=video_url,
        sound_url=sound_url
    )

@app.route('/frutas')
def frutas():
    return render_template('frutas.html')

@app.route('/fruta/<fruta>')
def mostrar_fruta(fruta):
    video_url = f'/static/videos/{fruta.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{fruta.lower()}.mp3'
    
    return render_template(
        'fruta.html',
        fruta=fruta.lower(),
        video_url=video_url,
        sound_url=sound_url
    )


@app.route('/alimentos')
def alimentos():
    return render_template('alimentos.html')

@app.route('/alimento/<alimento>')
def mostrar_alimento(alimento):
    video_url = f'/static/videos/{alimento.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{alimento.lower()}.mp3'
    
    return render_template(
        'alimento.html',
        alimento=alimento.lower(),
        video_url=video_url,
        sound_url=sound_url
    )
@app.route('/colores')
def colores():
    return render_template('colores.html')

@app.route('/color/<color>')
def mostrar_color(color):
    video_url = f'/static/videos/{color.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{color.lower()}.mp3'
    
    return render_template(
        'color.html',
        color=color.lower(),
        video_url=video_url,
        sound_url=sound_url
    )

@app.route('/insectos')
def insectos():
    return render_template('insectos.html')

@app.route('/insecto/<insecto>')
def mostrar_insecto(insecto):
    video_url = f'/static/videos/{insecto.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{insecto.lower()}.mp3'
    
    return render_template(
        'insecto.html',
        insecto=insecto.lower(),
        video_url=video_url,
        sound_url=sound_url
    )
@app.route('/animales')
def animales():
    animales = [
        'caballo', 'chancho', 'conejo', 'gallina', 'gato', 'leon', 'mono', 
        'perro', 'pez', 'pajaro', 'raton', 'tortuga'
    ]
    return render_template('animales.html', animales=animales)

@app.route('/animal/<animal>')
def mostrar_animal(animal):
    video_url = f'/static/videos/{animal.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{animal.lower()}.mp3'
    
    return render_template(
        'animal.html',
        animal=animal.lower(),
        video_url=video_url,
        sound_url=sound_url
    )
@app.route('/vegetales')
def vegetales():
    vegetales = [
        'zanahoria', 'brocoli', 'espinaca', 'acelga', 'cebolla', 'coliflor'
    ]
    return render_template('vegetales.html', vegetales=vegetales)
@app.route('/vegetal/<vegetal>')
def mostrar_vegetal(vegetal):
    video_url = f'/static/videos/{vegetal.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{vegetal.lower()}.mp3'
    
    return render_template(
        'vegetal.html',
        vegetal=vegetal.lower(),
        video_url=video_url,
        sound_url=sound_url
    )

@app.route('/bebidas')
def bebidas():
    bebidas = [
        'agua', 'te', 'cafe', 'gaseosa', 'jugo', 'chocolate_caliente', 'limonada'
    ]
    return render_template('bebidas.html', bebidas=bebidas)

@app.route('/bebida/<bebida>')
def mostrar_bebida(bebida):
    video_url = f'/static/videos/{bebida.lower()}-gesture.mp4'
    sound_url = f'/static/sounds/{bebida.lower()}.mp3'
    
    return render_template(
        'bebida.html',
        bebida=bebida.lower(),
        video_url=video_url,
        sound_url=sound_url
    )




if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5050)
