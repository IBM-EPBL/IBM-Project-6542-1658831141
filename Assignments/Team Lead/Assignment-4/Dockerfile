FROM python:alpine3.10
COPY . /docker-jobportal-app
WORKDIR /docker-jobportal-app
RUN pip install -r requirements.txt
EXPOSE 5001
ENTRYPOINT [ "python" ]
CMD [ "jobportal.py" ]
