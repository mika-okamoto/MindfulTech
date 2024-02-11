import requests
res = requests.post("http://127.0.0.1:5000/predict",json={'1': '23', '2': 'male', '3': '26-100', '4': 'always', '5': 'anxiety', '6': 'yes', '7': 'yes', '8': 'no', '9': 'yes', '10': 'maybe', '11': 'somewhat not open', '12': 'rarely'})
print(res.json())

