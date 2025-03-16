from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate():
    greutate = ''
    inaltime = ''
    bmi = 0

    if request.method == "POST" and 'greutateutilizator' in request.form:
        greutate = int(request.form.get('greutateutilizator'))
        inaltime = int(request.form.get('inaltimeutilizator'))
        bmi=calculate_bmi(greutate, inaltime)
    return render_template('index.html', greutate=greutate, inaltime=inaltime, bmi=bmi)


def calculate_bmi(greutate, inaltime):
    inaltime = inaltime / 100
    return round(greutate / (inaltime**2), 1)


app.run()
