from flask import Flask, request, jsonify
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split

app = Flask(__name__)

# === 模型訓練階段 ===
url = "https://raw.githubusercontent.com/selva86/datasets/master/BostonHousing.csv"
df = pd.read_csv(url)

X = df.drop('medv', axis=1)
y = df['medv']

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

model = LinearRegression()
model.fit(X_scaled, y)


@app.route('/')
def home():
    return "🏠 Boston Housing Price API is running!"


@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    df_input = pd.DataFrame([data])
    df_scaled = scaler.transform(df_input)
    prediction = model.predict(df_scaled)[0]
    return jsonify({'predicted_price': round(prediction, 2)})


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
