FROM python:3.8-slim
LABEL maintainer="xgsclear7"
ADD . /real-url-api
WORKDIR /real-url-api
RUN pip install -r requirements.txt -i https://pypi.mirrors.ustc.edu.cn/simple/
EXPOSE 7000
CMD ["python", "flask_server.py"]