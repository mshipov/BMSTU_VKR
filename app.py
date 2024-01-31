from flask import Flask, render_template, request
from keras import models
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


@app.route('/all_features/', methods=['GET', 'POST'])
def all_features():
    message = ''
    model = models.load_model("../models/all")

    if request.method == 'POST':
        param = []
        for i in range(1, 13):
            x = float(request.form.get(str(i)))
            if i == 10:
                if x == 0.0:
                    angle = ''
                elif x > 45:
                    x = 1
                    angle = '. Значение посчитано для угла 90'
                else:
                    x = 0
                    angle = '. Значение посчитано для угла 0'
            param.append(x)
        param = np.array(param)
        pred = model.predict(param)
        message = f'Соотношение матрица-накопитель для переданных параметров {str(pred)[2:-2]}{angle}'
    return render_template('all_features.html', result=message)

@app.route('/key_features/', methods=['GET', 'POST'])
def key_features():
    message = ''
    model = models.load_model("../models/key")

    if request.method == 'POST':
        param = []
        for i in [5, 8, 9, 1, 11]:
            param.append(float(request.form.get(str(i))))

        param = np.array(param)
        pred = model.predict(param)
        message = f'Соотношение матрица-накопитель для переданных параметров {str(pred)[2:-2]}'
    return render_template('key_features.html', result=message)

# if __name__ == '__main__':
app.run(debug=True)
