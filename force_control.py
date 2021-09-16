import numpy as np

from tiago_rl.envs import GripperTactileEnv
from tiago_rl.misc import LoadCellVisualiser

# Environment setup
# ----------------------------

show_gui = True
force_type = 'raw'
target_forces = np.array(2*[0.2])


env = GripperTactileEnv(show_gui=show_gui, 
                        force_type=force_type, 
                        target_forces=target_forces)

# Visualisation setup
# ----------------------------

vis = None
if show_gui:
    vis = LoadCellVisualiser(env)

# Control Loop
# ----------------------------

env.reset()
for i in range(300):
    # TODO do force control
    new_state = env.create_desired_state({
        'gripper_right_finger_joint': -0.2,
        'gripper_left_finger_joint': -0.2,
    })

    obs, reward, done, info = env.step(new_state)

    # extract information from observations.
    # see GripperTactileEnv._get_obs() for reference.
    f = obs[-2:]

    if vis:
        vis.update_plot(is_success=info['is_success'], reward=reward)
    