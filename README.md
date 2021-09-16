<p align="center">
    <h1 align="center">
        NeuTouch Summer School 2021 - TIAGo Tutorials
    </h1>
</p>

- [Force Controller](#force-controller)
  - [Usage with Docker](#usage-with-docker)
  - [Manual Installation](#manual-installation)
- [Force Control with Reinforcement Learning](#force-control-with-reinforcement-learning)
  - [Manual Installation](#manual-installation-1)

# Force Controller

In this first task, the goal is to implement a controller that reaches and maintains a given (but variable) target force.
As the robot is either position or velocity controlled, you need to think about how to transform force deltas into position deltas.
A code skeleton can be found in `force_control.py`, where the TIAGo gripper performs a closing movement.


## Usage with Docker
Using docker was only successfully tested on Linux (Ubuntu 18.04) so far. 
Setting up X-forwarding under macOS can be tricky, so we recommend the manual installation option in that case.


1. Clone the repository and change into the directory:
```
git clone https://github.com/llach/tiago_summer_school && cd tiago_summer_school
```

2. Build the docker container using:
```
docker build -t force_control .
```

3. Run `force_control.py` inside the docker container like so:
```
docker run --device /dev/dri -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix -v $PWD/force_control.py:/main.py force_control
```
The script will launch two different GUIs (a pyBullet visualization and live plots of interesting variables), thus we need to set the `DISPLAY` environment variable, forward `/dev/dri` and forward the X11 socket.

Additionally, we mount `force_control.py` as a volume. This allows us to edit the python file locally and execute it using `docker run` without rebuilding the container again.

In case your IDE does not auto-complete `tiago_rl` related code, you need to install the package manually as well.

## Manual Installation

The manual installation is fairly simple, too. It is recommended to use [pyenv](https://github.com/pyenv/pyenv) and set up an environment using python 3.9.6.

1. Follow install instructions of [tiago_rl](https://github.com/llach/tiago_rl)
2.  Clone the repository and change into the directory:
```
git clone https://github.com/llach/tiago_summer_school && cd tiago_summer_school
```
3. Run the script:
```
python force_control.py
```

# Force Control with Reinforcement Learning

You can also use the TIAGo simulation environments to train reinforcement learning algorithms to perform force control.
We recommend using established and tested RL repositories for this, but you are not constrained to a particular project as the environments follow the widely accepted OpenAI gym conventions.
In this example, we'll use stable-baselines3, but feel free to experiment with other projects as well.

## Manual Installation

1. Follow install instructions of [tiago_rl](https://github.com/llach/tiago_rl)
2. Install `stable-baselines3` 
```
pip install -U stable-baselines3
```
3.  Clone the repository and change into the directory:
```
git clone https://github.com/llach/tiago_summer_school && cd tiago_summer_school
```
4. Run the script
```
python learn_control.py
```