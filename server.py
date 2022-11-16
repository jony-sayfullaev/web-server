from flask import Flask, render_template, request, redirect
import csv

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)


# def write_to_file(data):
#     with open('database.txt', mode='a') as data_file:
#         data_file.write(f"{data}\n")

def write_to_csv(data):
    with open("database.csv", newline='', mode='a')as database_csv:
        email = data["email"]
        subject = data["subject"]
        message = data["message"]
        csv_writer = csv.writer(database_csv, delimiter=',')
        csv_writer.writerow(['email', 'subject', 'message'])
        csv_writer.writerow([email, subject, message])


@app.route("/submit_form", methods=['POST', 'GET'])
def submit_form():
    if request.method == "POST":
        try:
            data = request.form.to_dict()
            write_to_csv(data=data)
            return redirect('/thankyou.html')
        except:
            return "did not save to database"
    else:
        return "something went wrong: please try again"


