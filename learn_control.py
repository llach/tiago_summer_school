import numpy as np

from gym.wrappers import TimeLimit
from tiago_rl.envs import GripperTactileEnv

# Environment setup
# ----------------------------
"""
the environment for training is created equally to the one in the first task 
in order for them to be comparable.

we only add the TimeLimit wrapper so that the environment emits a done=True
after N steps
"""
POS_CTRL = 'pos'
VEL_CTRL = 'vel'

target_forces = np.array(2*[0.2])

env = GripperTactileEnv(show_gui=False, 
                        target_forces=target_forces,
                        control_mode=VEL_CTRL)
env = TimeLimit(env, max_episode_steps=500)

# RL Training setup
# ----------------------------
"""
here, you are free to use whichever RL algorithm or package you prefer.
in case you don't know where to start, we recommend having a look at the examples from stable-baselines3:
https://stable-baselines3.readthedocs.io/en/master/guide/examples.html

you can find the calculation of different reward types here:
https://github.com/llach/tiago_rl/blob/master/tiago_rl/envs/load_cell_tactile_env.py#L102

generally, this script should:
* create a model (make sure to use an algorithm that can handle continuous actions)
* train the model
* save model weights (usually only when new high-scores are achieved to save disk space)

then, in another script, you can:
* load the weights of the best performing model
* evaluate the model by:
    * watching its behavior in the environment
    * comparing the cumulative reward with that of your hand-written force controller
"""
# TODO create and train model