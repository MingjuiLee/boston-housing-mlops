import requests

url = "http://localhost:30080/predict"

test_data = [
    {"crim": 0.1, "zn": 18, "indus": 2.3, "chas": 0, "nox": 0.5, "rm": 6, "age": 65,
        "dis": 4.0, "rad": 1, "tax": 300, "ptratio": 15, "b": 390, "lstat": 5},
    {"crim": 0.2, "zn": 0, "indus": 6.9, "chas": 0, "nox": 0.6, "rm": 5.8, "age": 80,
        "dis": 3.5, "rad": 5, "tax": 350, "ptratio": 17, "b": 380, "lstat": 12},
    {"crim": 0.05, "zn": 25, "indus": 3.3, "chas": 1, "nox": 0.4, "rm": 7, "age": 45,
        "dis": 5.0, "rad": 2, "tax": 250, "ptratio": 13, "b": 395, "lstat": 3}
]

for i, item in enumerate(test_data, 1):
    res = requests.post(url, json=item)
    print(f"🏠 測試案例 {i}: {res.json()}")
