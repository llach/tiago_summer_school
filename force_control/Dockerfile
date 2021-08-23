FROM python:3.9.6

RUN apt-get update -y
RUN apt install libgl1-mesa-glx -y

RUN git clone https://github.com/llach/tiago_rl /tiago_rl
WORKDIR /tiago_rl

RUN pip install -r requirements.txt
RUN pip install .

WORKDIR /
CMD ["python", "main.py"]