# ⚾ 숫자 야구 웹 게임 (Number Baseball Web Game)

0부터 9까지의 중복되지 않는 3자리 숫자를 맞추는 클래식 숫자 야구 게임입니다. 
파이썬 **Flask**와 **SQLite**를 이용해 서버와 명예의 전당(랭킹) 시스템을 구축하고, 직관적인 웹 UI를 구현했습니다.

## 🚀 배포 링크 (Live Demo)
👉 **[숫자 야구 게임 플레이하기](https://number-baseball-game-l7zo.onrender.com/)**

## ✨ 주요 기능 (Features)
- **명예의 전당 (글로벌 랭킹):** SQLite 기반의 데이터베이스를 연동하여, 최소 횟수로 정답을 맞춘 Top 5 플레이어의 기록을 실시간으로 보여줍니다.
- **시각적 타격감 (UI/UX):** 정답을 맞췄을 때 화려한 폭죽 파티클(Confetti)이 터지고, 아웃(Out) 시 게임 보드가 흔들리는 애니메이션을 적용해 게임의 재미를 더했습니다.
- **서버/클라이언트 이중 검증:** 중복된 숫자나 문자를 입력하는 등의 비정상적인 접근을 양쪽에서 차단하여 서버의 안정성을 높였습니다.

## 🛠 기술 스택 (Tech Stack)
- **Backend**: Python 3, Flask, SQLite
- **Frontend**: HTML5, CSS3, Vanilla JavaScript
- **Deployment**: Render (Gunicorn)

## 💡 트러블슈팅 및 아키텍처 고민 (Troubleshooting)

**[이슈] 실시간 멀티플레이 도입에 따른 서버 과부하 및 렉 발생**
- **시도:** 유저 간의 실시간 대결을 위해 `Flask-SocketIO`를 활용한 양방향 웹소켓(WebSocket) 통신 모드를 구현 및 배포했습니다.
- **문제 발생:** 무료 클라우드 호스팅(Render Free Tier) 환경에서 메모리 한계로 인해 소켓 연결 유지가 불안정해지고, 게임 진행 시 극심한 지연(Latency)이 발생했습니다.
- **해결 및 롤백(Rollback):** 서비스의 '안정성'과 '쾌적한 사용자 경험(UX)'이 최우선이라고 판단하여, 무거운 소켓 로직을 과감히 덜어내고 기존의 가벼운 단방향 HTTP 기반 + SQLite 랭킹 시스템으로 롤백을 진행했습니다. 이를 통해 서버 응답 속도를 정상화하고 안정적인 서비스를 복구할 수 있었습니다.

## 📁 프로젝트 구조 (Directory Structure)
```text
number-baseball-web/
 ├── app.py                 # 서버 실행, 게임 판정 및 DB 통신 로직
 ├── leaderboard.db         # 명예의 전당 기록을 저장하는 SQLite DB
 ├── requirements.txt       # 배포용 파이썬 패키지 목록
 ├── static/
 │    └── style.css         # UI 디자인 및 흔들림 애니메이션
 └── templates/
      └── index.html        # 웹 페이지 구조 및 클라이언트(JS) 통신
