Web_app ->folder
app.yaml
main.py
requirements.txt
templates ->folder
index.html


app.yaml
runtime: python39

# GAE looks for an 'app' object in main.py to start the server
entrypoint: gunicorn -b :$PORT main:app

main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    # render_template automatically looks in the /templates folder
    return render_template('index.html', title="Home Page")

if __name__ == '__main__':
    # Local development server
    app.run(host='127.0.0.1', port=8080, debug=True)

reqirements.txt
flask==3.0.0
gunicorn==21.2.0
Index.html

<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{{ title }}</title>
    <style>
        body { font-family: sans-serif; display: flex; justify-content: center; align-items: center; height: 100vh; margin: 0; background-color: #f4f4f9; }
        .card { background: white; padding: 2rem; border-radius: 8px; box-shadow: 0 4px 6px rgba(0,0,0,0.1); text-align: center; }
        h1 { color: #4285F4; }
    </style>
</head>
<body>
    <div class="card">
        <h1>Success!</h1>
        <p>Your Python-powered HTML is running.</p>
    </div>
</body>
</html>
