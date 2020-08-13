FROM tiangolo/uvicorn-gunicorn:python3.7

# streamlit-specific commands
RUN mkdir -p /root/.streamlit
RUN bash -c 'echo -e "\
[general]\n\
email = \"\"\n\
" > /root/.streamlit/credentials.toml'
RUN bash -c 'echo -e "\
[server]\n\
enableCORS = false\n\
port = $PORT\n\
" > /root/.streamlit/config.toml'

RUN mkdir /streamlit

COPY requirements.txt /streamlit

WORKDIR /streamlit

RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /streamlit

EXPOSE 8501

# CMD ["streamlit","--server.port","$PORT","run","app.py"]
CMD streamlit run app.py --server.port $PORT
#Run en local docker-compose
#CMD streamlit run app.py --server.port 8501