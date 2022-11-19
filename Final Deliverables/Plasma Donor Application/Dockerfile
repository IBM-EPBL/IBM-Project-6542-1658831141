FROM python:alpine3.10
COPY . /plasma-app
WORKDIR /plasma-app
RUN pip install -r requirements.txt
EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
