FROM python:3.9.6

RUN apt-get update -y
RUN apt install libgl1-mesa-glx libx11-xcb1 libxcb-xinerama0 libxcb-icccm4 libxcb-image0 libxcb-keysyms1 libxcb-render-util0 libxcb-shape0 libxcb-xkb-dev libxkbcommon-x11-0 libdbus-1-3  -y

RUN git clone https://github.com/llach/tiago_rl /tiago_rl
WORKDIR /tiago_rl

RUN pip install -r requirements.txt
RUN pip install .

WORKDIR /
CMD ["python", "main.py"]