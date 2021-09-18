import numpy as np

from tiago_rl.envs import GripperTactileEnv
from tiago_rl.misc import LoadCellVisualiser

# Environment setup
# ----------------------------

"""
we first create the simulation environment for the TIAGo sensorised gripper.
it can either be position or velocity controller (whichever you prefer).
"""

POS_CTRL = 'pos'
VEL_CTRL = 'vel'

# whether to render the environment or not
show_gui = True

# target force to reach and maintain. your controller should be able to reach different target forces, not just this one
target_forces = np.array(2*[0.2])

env = GripperTactileEnv(show_gui=show_gui, 
                        target_forces=target_forces,
                        control_mode=VEL_CTRL)

# Visualisation setup
# ----------------------------
"""
additionally, you can visualize certain variables from the environment's state such as
current joint positions, velocities, forces (with target force) and more.
"""
vis = None
if show_gui:
    vis = LoadCellVisualiser(env)

# Control Loop
# ----------------------------

rewards = [] # we use the cumulative reward as a performance metric
for i in range(500):
    """
    current_q and current_vel are dicts mapping joint names 
    to the current joint position and velocity, respectively:
    
    as an example, the position dict would look like this for a fully open gripper:
    current_q = {
        'gripper_right_finger_joint': 0.045,
        'gripper_left_finger_joint': 0.045
    }
    """
    current_q, current_vel = env.get_state_dicts()

    """
    to get the current forces, we access the environment's member current_forces
    """
    current_forces = env.current_forces

    """
    as the action for the environment consists of a desired joint state for all joints, we can use
    BulletRobotEnv.create_desired_state() to create one even if we only want to control a subset of joints.
    
    this is not as important for GripperTactileEnv, which only controls the two finger joints, but very
    convenient for environments that simulate the whole robot
    """
    # TODO create desired state such that the target force is reached and maintained
    new_state = env.create_desired_state({
        'gripper_right_finger_joint': -0.2,
        'gripper_left_finger_joint': -0.2,
    })

    """
    next, we hand over the action (desired joint state) to the environment and receive 
    observations, reward, done (bool) and additional info in return
    """
    obs, reward, done, info = env.step(new_state)
    rewards.append(reward) # store scalar reward r(t) in rewards list

    # finally, we update the plot
    if vis:
        vis.update_plot(is_success=info['is_success'], reward=reward)
print(f"final episode reward {np.sum(rewards)}")