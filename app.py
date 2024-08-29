from flask import Flask, render_template, request, jsonify
import pandas as pd

app = Flask(__name__)

# Cargar el archivo CSV con la codificación adecuada
df = pd.read_csv('data/votacion.csv', encoding='ISO-8859-1')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    # Obtener el número de cédula ingresado y eliminar espacios en blanco
    numero_cedula = request.form.get('cedula').strip()
    
    # Convertir la columna de cédulas a cadena para hacer la comparación
    resultado = df[df['Número de Cédula'].astype(str) == numero_cedula].to_dict(orient='records')
    
    if resultado:
        return jsonify({'status': 'success', 'data': resultado})
    else:
        return jsonify({'status': 'not found', 'message': 'No se encontraron datos para el número de cédula ingresado.'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
