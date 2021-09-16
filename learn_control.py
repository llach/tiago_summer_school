import numpy as np

from gym.wrappers import TimeLimit
from tiago_rl.envs import GripperTactileEnv

# Environment setup
# ----------------------------

force_type = 'raw'
target_forces = np.array(2*[0.2])

env = GripperTactileEnv(show_gui=False, 
                        force_type=force_type, 
                        target_forces=target_forces)
env = TimeLimit(env, max_episode_steps=300)

# RL Training setup
# ----------------------------

# TODO setup and train model