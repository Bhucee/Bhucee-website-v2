from flask import Flask, render_template

app = Flask(__name__)

JOBS = [{
  'id': 1,
  'title': 'Data Analyst',
  'location': 'Lagos',
  'Salary': 'N 6,500,000'
}, {
  'id': 2,
  'title': 'Business Analyst',
  'location': 'Remote',
  'Salary': 'N 8,500,000'
}, {
  'id': 3,
  'title': 'Back-end Engineer',
  'location': 'Abuja',
  'Salary': 'N 7,500,000'
}, {
  'id': 4,
  'title': 'Front-end Engineer',
  'location': 'Ikeja, LAgos',
  'Salary': 'N 7,500,000'
}]


@app.route("/")
def hello_world():
  return render_template('home.html', jobs=JOBS, company_name='Bhucee Limited')


if __name__ == "__main__":
  app.run(host='0.0.0.0', debug=True)
