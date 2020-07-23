FROM tiangolo/uvicorn-gunicorn:python3.7

RUN mkdir /fastapi

COPY requirements.txt /fastapi

WORKDIR /fastapi

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /fastapi

WORKDIR /fastapi/Gender

EXPOSE 8000

CMD ["uvicorn","main:app","--host","0.0.0.0","--port","8000"]
# CMD uvicorn main:app --host 0.0.0.0 --port $PORT