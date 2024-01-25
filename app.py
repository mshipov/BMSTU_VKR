# import flask
from flask import Flask, render_template, request
from keras import models
import numpy as np

# from tensorflow.keras import Sequential
# from tensorflow.keras.layers import Dense, Dropout
# from tensorflow.keras.optimizers import Adam
# from keras.callbacks import EarlyStopping
# import numpy as np

app = Flask(__name__)
model = models.load_model("C:/Users/Public/Documents/my_model")
@app.route('/', methods=['get', 'post'])
def main():
    message = ''
    if request.method == 'POST':
        param = []
        for i in range(1, 13):
            param.append(float(request.form.get(str(i))))
        param = np.array(param)
        pred = model.predict(param)
        message = f'Соотношение матрица-накопитель для переданных параметров {pred}'
    return render_template('main.html', result=message)

if __name__ == '__main__':
    app.run(debug=True)