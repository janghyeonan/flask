from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)


@app.route("/")
def run():
    conn = sqlite3.connect('wanggun.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM general')
    rows = c.fetchall();
    return render_template("index.html", rows=rows)


@app.route('/modi')
def modi():
    id = request.args.get("id")

    conn = sqlite3.connect('wanggun.db')
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    c.execute('SELECT * FROM general where id=' + str(id))
    rows = c.fetchall();

    return render_template('modi.html', rows=rows)


@app.route('/addrec', methods=['POST', 'GET'])
def addrec():
    if request.method == 'POST':
        try:
            war = request.form['war']
            id = request.form['id']

            with sqlite3.connect("wanggun.db") as con:
                cur = con.cursor()

                cur.execute("update general set war=" + str(war) + " where id=" + str(id))

                con.commit()
                msg = "정상적으로 입력되었습니다."
        except:
            con.rollback()
            msg = "입력과정에서 에러가 발생했습니다."

        finally:
            return render_template("result.html", msg=msg)
            con.close()


@app.route('/intro', methods=['POST', 'GET'])
def intro():
    if request.method == 'POST':
        return render_template('step.html')
    return render_template('intro.html')

@app.route('/step', methods=['POST', 'GET'])
def step():
    if request.method == 'POST':
        return render_template('step1.html')
    return render_template('step.html')

@app.route('/step1', methods=['POST', 'GET'])
def step1():
    if request.method == 'POST':
        return render_template('step2.html')
    return render_template('step1.html')

@app.route('/step2', methods=['POST', 'GET'])
def step2():
    if request.method == 'POST':
        return render_template('step3.html')
    return render_template('step2.html')

@app.route('/step3', methods=['POST', 'GET'])
def step3():
    if request.method == 'POST':
        return render_template('step4.html')
    return render_template('step3.html')

@app.route('/step4', methods=['POST', 'GET'])
def step4():
    if request.method == 'POST':
        return render_template('end.html')
    return render_template('step4.html')

@app.route('/end', methods=['POST', 'GET'])
def end():
    if request.method == 'POST':
        return render_template('report.html')
    return render_template('end.html')

@app.route('/report', methods=['POST', 'GET'])
def report():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('report.html')

@app.route('/talk', methods=['POST', 'GET'])
def talk():
    if request.method == 'POST':
        return render_template('talk_result.html')
    return render_template('talk.html')

@app.route('/talk_result', methods=['POST', 'GET'])
def talk_result():
    if request.method == 'POST':
        return render_template('index.html')
    return render_template('talk_result.html')

app.run(host='0.0.0.0', port=8787, debug=True)
