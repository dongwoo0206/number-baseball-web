from flask import Flask, render_template, request, jsonify, session
import sqlite3
import random

app = Flask(__name__)
app.secret_key = "super_secret_key"

def init_db():
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()
    c.execute('''CREATE TABLE IF NOT EXISTS ranking 
                 (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT, attempts INTEGER)''')
    conn.commit()
    conn.close()

init_db()

def generate_secret():
    return random.sample(range(10), 3)

@app.route('/')
def index():
    if 'secret' not in session:
        session['secret'] = generate_secret()
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess_str = data.get('guess', '')

    if len(guess_str) != 3 or not guess_str.isdigit() or len(set(guess_str)) != 3:
        return jsonify({'error': '유효하지 않은 입력입니다.'})

    session['attempts'] += 1
    guess_list = [int(char) for char in guess_str]
    secret = session['secret']

    strikes = sum(1 for i in range(3) if guess_list[i] == secret[i])
    balls = sum(1 for i in range(3) if guess_list[i] in secret) - strikes
    is_homerun = (strikes == 3)
    attempts = session['attempts']

    if is_homerun:
        session['secret'] = generate_secret()
        session['attempts'] = 0

    return jsonify({'strikes': strikes, 'balls': balls, 'attempts': attempts, 'is_homerun': is_homerun})

@app.route('/save_score', methods=['POST'])
def save_score():
    data = request.json
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()
    c.execute('INSERT INTO ranking (name, attempts) VALUES (?, ?)', (data['name'], data['attempts']))
    conn.commit()
    conn.close()
    return jsonify({'success': True})

@app.route('/get_leaderboard', methods=['GET'])
def get_leaderboard():
    conn = sqlite3.connect('leaderboard.db')
    c = conn.cursor()
    c.execute('SELECT name, attempts FROM ranking ORDER BY attempts ASC LIMIT 5')
    rankings = [{'name': row[0], 'attempts': row[1]} for row in c.fetchall()]
    conn.close()
    return jsonify(rankings)

if __name__ == '__main__':
    app.run(debug=True)