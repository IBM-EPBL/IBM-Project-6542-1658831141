FROM python:alpine3.7
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
EXPOSE 5003
ENTRYPOINT [ "python" ]
CMD [ "demo.py" ]
