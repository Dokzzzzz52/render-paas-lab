from datetime import datetime
import socket

from flask import Flask, render_template_string


app = Flask(__name__)


PAGE = """
<!doctype html>
<html lang="ru">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>Flask на Render</title>
  <style>
    * { box-sizing: border-box; }
    body {
      min-height: 100vh;
      margin: 0;
      display: grid;
      place-items: center;
      color: #f8fbff;
      font-family: Arial, sans-serif;
      background: linear-gradient(135deg, #102a43, #176b87 55%, #55c1b3);
    }
    main {
      width: min(650px, calc(100% - 32px));
      padding: 42px;
      border: 1px solid rgba(255, 255, 255, .25);
      border-radius: 24px;
      background: rgba(9, 28, 49, .52);
      box-shadow: 0 24px 70px rgba(0, 0, 0, .28);
      backdrop-filter: blur(8px);
      text-align: center;
    }
    h1 { margin: 0 0 14px; font-size: clamp(28px, 6vw, 42px); }
    .lead { margin: 0 0 28px; font-size: 18px; line-height: 1.55; }
    .details { display: grid; gap: 12px; text-align: left; }
    .item { padding: 14px 16px; border-radius: 12px; background: rgba(255, 255, 255, .12); }
    .label { display: block; margin-bottom: 4px; color: #b9f4e9; font-size: 13px; font-weight: bold; text-transform: uppercase; letter-spacing: .06em; }
    code { overflow-wrap: anywhere; font-size: 16px; }
  </style>
</head>
<body>
  <main>
    <h1>Привет! Это мое приложение на PaaS (Render).</h1>
    <p class="lead">Flask-приложение развёрнуто как веб-сервис.</p>
    <section class="details">
      <div class="item"><span class="label">Текущее время сервера</span><code>{{ server_time }}</code></div>
      <div class="item"><span class="label">Имя хоста сервера</span><code>{{ hostname }}</code></div>
    </section>
  </main>
</body>
</html>
"""


@app.get("/")
def index():
    return render_template_string(
        PAGE,
        server_time=datetime.now().strftime("%d.%m.%Y %H:%M:%S"),
        hostname=socket.gethostname(),
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
