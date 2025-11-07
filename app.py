from flask import Flask, request, jsonify, render_template
import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

app = Flask(__name__)

# 載入模型
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)
X = df.drop('medv', axis=1)
y = df['medv']
scaler = StandardScaler().fit(X)
model = LinearRegression().fit(scaler.transform(X), y)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/predict', methods=['POST'])
def predict():
    data = [float(x) for x in request.form.values()]
    features = pd.DataFrame([data], columns=X.columns)
    features_scaled = scaler.transform(features)
    prediction = model.predict(features_scaled)[0]
    return render_template('index.html', prediction_text=f'預測房價: {prediction:.2f} 千美元')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
