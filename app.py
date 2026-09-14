from flask import Flask, render_template, request, jsonify, session
import random

app = Flask(__name__)
app.secret_key = "super_secret_key" # 세션 유지를 위한 비밀키 (임의 지정 가능)

def generate_secret():
    """0~9 사이의 중복 없는 3자리 숫자 생성"""
    return random.sample(range(10), 3)

@app.route('/')
def index():
    # 게임 첫 접속 시 정답 초기화
    if 'secret' not in session:
        session['secret'] = generate_secret()
        session['attempts'] = 0
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    data = request.json
    guess_str = data.get('guess', '')

    # 서버 측 유효성 검사
    if len(guess_str) != 3 or not guess_str.isdigit() or len(set(guess_str)) != 3:
        return jsonify({'error': '유효하지 않은 입력입니다.'})

    session['attempts'] += 1
    guess_list = [int(char) for char in guess_str]
    secret = session['secret']

    strikes = sum(1 for i in range(3) if guess_list[i] == secret[i])
    balls = sum(1 for i in range(3) if guess_list[i] in secret) - strikes

    is_homerun = (strikes == 3)
    attempts = session['attempts']

    # 정답을 맞추면 정답을 새로 고침
    if is_homerun:
        session['secret'] = generate_secret()
        session['attempts'] = 0

    return jsonify({
        'strikes': strikes,
        'balls': balls,
        'attempts': attempts,
        'is_homerun': is_homerun,
        'error': None
    })

if __name__ == '__main__':
    app.run(debug=True)