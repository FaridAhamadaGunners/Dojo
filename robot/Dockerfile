FROM python:3
MAINTAINER xxxxx <xxxxx@gmail.com>
COPY . /robot
WORKDIR /robot
RUN pip install -r requirements.txt
EXPOSE 3333
CMD ["python","src/get_final_position.py"]