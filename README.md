 * 起動方法
    - docker build -t app .
    - docker run --name ranking_app -d -p 4000:80 app
 * 接続方法
    - http://localhost:4000/

 * FROM
    - 言語、実行環境のほか、OS 等も指定できる。(python, node, ubuntu....)
    - バージョンを指定できる (python:3.8)
 
 * RUN
    - ビルド時に実行するコマンドを指定できる
    - pip install, npm install など

 * CMD
    - docker run 時に実行するコマンドを指定できる
    - CMD ["python", "app.py"]

 * COPY
    - ホストからコンテナイメージにファイルやディレクトリをコピーする

 * WORKDIR
    - RUN, CMD, ENTRYPOINT, COPY, ADD, docker run, exec で実行するコンテナプロセスの実行ディレクトリを指定する

 * EXPOSE
    - 指定したポート番号をコンテナが公開する
    - EXPOSE 80

 * ENV
    - 環境変数を指定する

 * 参考
    - https://docs.docker.jp/engine/reference/builder.html
    - https://www.tohoho-web.com/docker/dockerfile.html