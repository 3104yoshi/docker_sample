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
  
  ENV DB_HOST="192.168.2.201" \
    DB_PORT="3306" \
    DB_USER="myapp" \
    DB_PASSWD="ZbGc7#adG87GBfVC" \
    DB_DATABASE="sample"

 * 参考
  - https://docs.docker.jp/engine/reference/builder.html
  - https://www.tohoho-web.com/docker/dockerfile.html