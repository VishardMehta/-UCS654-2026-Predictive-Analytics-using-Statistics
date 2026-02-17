from flask import Flask, request, render_template_string
from flask_mail import Mail, Message
from topsis_hitesh_102317248.topsis import topsis
import os

app = Flask(__name__)

app.config["MAIL_SERVER"] = "smtp.gmail.com"
app.config["MAIL_PORT"] = 587
app.config["MAIL_USE_TLS"] = True
app.config["MAIL_USERNAME"] = os.getenv("MAIL_USER")
app.config["MAIL_PASSWORD"] = os.getenv("MAIL_PASS")
mail = Mail(app)

HOME_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>TOPSIS Web Service</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #f3f4f6;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            width: 420px;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
        }
        h2 {
            text-align: center;
            margin-bottom: 20px;
            color: #2563eb;
        }
        input {
            width: 100%;
            padding: 10px;
            margin: 8px 0;
            border: 1px solid #d1d5db;
            border-radius: 6px;
            box-sizing: border-box;
        }
        button {
            width: 100%;
            padding: 10px;
            margin-top: 10px;
            background: #2563eb;
            color: white;
            border: none;
            border-radius: 6px;
            font-size: 16px;
            cursor: pointer;
        }
        button:hover {
            background: #1d4ed8;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>TOPSIS Web Service</h2>
        <form action="/topsis" method="post" enctype="multipart/form-data">
            <input type="file" name="file" required>
            <input type="text" name="weights" placeholder="Weights (e.g. 1,1,1,2,1)" required>
            <input type="text" name="impacts" placeholder="Impacts (e.g. +,+,-,+,+)" required>
            <input type="email" name="email" placeholder="Email address" required>
            <button type="submit">Run TOPSIS</button>
        </form>
    </div>
</body>
</html>
"""

SUCCESS_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Result Sent</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #ecfdf5;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            width: 420px;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
            text-align: center;
        }
        h2 { color: #16a34a; }
        p { color: #374151; }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #2563eb;
            color: white;
            text-decoration: none;
            border-radius: 6px;
        }
        a:hover { background: #1d4ed8; }
    </style>
</head>
<body>
    <div class="card">
        <h2>Result Sent Successfully</h2>
        <p>Your TOPSIS result file has been emailed.</p>
        <a href="/">⬅ Back</a>
    </div>
</body>
</html>
"""

ERROR_HTML = """
<!DOCTYPE html>
<html>
<head>
    <title>Error</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            background: #fef2f2;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            margin: 0;
        }
        .card {
            background: white;
            width: 420px;
            padding: 30px;
            border-radius: 14px;
            box-shadow: 0 6px 18px rgba(0,0,0,0.12);
            text-align: center;
        }
        h2 { color: #dc2626; }
        a {
            display: inline-block;
            margin-top: 20px;
            padding: 10px 20px;
            background: #2563eb;
            color: white;
            text-decoration: none;
            border-radius: 6px;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>Error</h2>
        <p>{{ error }}</p>
        <a href="/">⬅ Back</a>
    </div>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(HOME_HTML)

@app.route("/topsis", methods=["POST"])
def run_topsis():
    try:
        file = request.files["file"]
        weights = request.form["weights"]
        impacts = request.form["impacts"]
        email = request.form["email"]

        input_path = "input.csv"
        output_path = "result.csv"

        file.save(input_path)

        topsis(input_path, weights, impacts, output_path)

        msg = Message(
            subject="TOPSIS Result",
            sender=app.config["MAIL_USERNAME"],
            recipients=[email]
        )

        msg.html = """
        <h2 style='color:#2563eb;'>TOPSIS Result Generated</h2>
        <p>Your TOPSIS analysis has been completed successfully.</p>
        <p>The result file is attached with this email.</p>
        <hr>
        <p style='font-size:12px;color:gray;'>Automated message from TOPSIS Web Service</p>
        """

        with app.open_resource(output_path) as fp:
            msg.attach("result.csv", "text/csv", fp.read())

        mail.send(msg)

        os.remove(input_path)
        os.remove(output_path)

        return render_template_string(SUCCESS_HTML)

    except Exception as e:
        return render_template_string(ERROR_HTML, error=str(e))

if __name__ == "__main__":
    app.run(debug=True)
