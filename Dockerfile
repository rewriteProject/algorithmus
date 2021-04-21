FROM python

WORKDIR /app

COPY ./requirements.txt ./requirements.txt

RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 9002

CMD ["python", "src/request_processing.py" ]