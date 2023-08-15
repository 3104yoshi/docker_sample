# syntax=docker/dockerfile:1
   
# FROM node:18-alpine
FROM node:14.17.6-alpine3.14
RUN yarn install --production
RUN yarn global add @vue/cli

FROM python:3.8
COPY src/ ./src/
RUN pip install Flask
RUN pip install flask_login
# CMD ["node", "src/index.js"]
CMD ["python", "src/backend/appserver.py"]
EXPOSE 5000