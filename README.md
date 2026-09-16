# ⚾ 숫자 야구 웹 게임 (Number Baseball Web Game)

0부터 9까지의 중복되지 않는 3자리 숫자를 맞추는 클래식 숫자 야구 게임입니다. 
파이썬 **Flask**를 이용해 서버(판정 로직)를 구성하고, **HTML/CSS/JS**를 활용해 직관적이고 깔끔한 웹 UI를 구현했습니다.

## 🚀 배포 링크 (Live Demo)
👉 **[숫자 야구 게임 플레이하기](https://number-baseball-game-l7zo.onrender.com)**

## 🎮 게임 규칙
1. 0~9 사이의 서로 다른 3자리 숫자가 랜덤으로 생성됩니다.
2. 플레이어는 3자리 숫자를 입력하여 정답을 추측합니다.
3. 입력한 숫자에 대한 판정 결과가 나옵니다.
   - **Strike (S)**: 숫자와 위치가 모두 맞은 경우
   - **Ball (B)**: 숫자는 맞지만 위치가 틀린 경우
   - **Out**: 일치하는 숫자가 하나도 없는 경우
4. 3 Strike(홈런)를 맞추면 게임에서 승리하며, 몇 번 만에 맞췄는지 알려줍니다!

## ✨ 주요 기능
- **서버 검증 로직**: 부정 입력(중복된 숫자, 문자 입력 등)을 프론트엔드와 백엔드(Flask) 양쪽에서 이중으로 차단합니다.
- **반응형 웹 디자인**: 스마트폰과 PC 어디서든 깔끔하게 보이는 모바일 친화적 UI를 적용했습니다.
- **애니메이션 효과**: 결과가 추가될 때 부드럽게 나타나는 슬라이드 효과와 시각적인 상태 뱃지(S/B/OUT)를 구현했습니다.

## 🛠 기술 스택 (Tech Stack)
- **Backend**: Python 3, Flask
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Render (Gunicorn)

## 📁 프로젝트 구조 (Directory Structure)
```text
number-baseball-web/
 ├── app.py                 # 서버 실행 및 게임 로직 담당
 ├── requirements.txt       # 배포 및 실행에 필요한 파이썬 패키지 목록
 ├── static/
 │    └── style.css         # UI 디자인 및 애니메이션
 └── templates/
      └── index.html        # 웹 페이지 구조 및 클라이언트(JS) 로직
