FROM python:alpine3.10
COPY . /docker-plasmadonor-app
WORKDIR /docker-plasmadonor-app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "app.py" ]
