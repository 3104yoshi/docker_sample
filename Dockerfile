# syntax=docker/dockerfile:1
   
# FROM node:18-alpine
FROM python:3.8
WORKDIR /app
COPY . .
# RUN yarn install --production
RUN pip install --trusted-host pypi.python.org -r requirements.txt
# CMD ["node", "src/index.js"]
CMD ["python", "src/app.py"]
EXPOSE 3000