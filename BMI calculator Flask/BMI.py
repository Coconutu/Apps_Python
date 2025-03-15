from flask import Flask, request, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def calculate():
    greutate = ''
    inaltime = ''
    bmi=0
    inaltimecm=0
    if request.method=="POST" and 'greutateutilizator' in request.form:
        greutate = int(request.form.get('greutateutilizator'))
        inaltimecm = int(request.form.get('inaltimeutilizator'))
        inaltime=inaltimecm/100
        bmi = round(greutate / (inaltime * inaltime),1)
    return render_template('index.html', greutate=greutate, inaltime=inaltime, bmi=bmi)


app.run()
