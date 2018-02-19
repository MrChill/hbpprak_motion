# Imported Python Transfer Function
import numpy as np
@nrp.MapVariable("time_weight", global_key="time_weight", initial_value=1.41, scope=nrp.GLOBAL)
@nrp.MapSpikeSink("motors", nrp.brain.motors, nrp.leaky_integrator_alpha)
@nrp.MapRobotPublisher('arm_pitch', Topic('/robot/hollie_real_left_arm_2_joint/cmd_pos', std_msgs.msg.Float64))
@nrp.Neuron2Robot()
def swing(t, motors, arm_pitch, time_weight):
    clientLogger.info("Motor potential: {}".format(time_weight.value))
    # set arm to initial state
    arm_pitch.send_message(std_msgs.msg.Float64(-1.5))#* motors.voltage
    # activate Arm when ball is in position and move to end state
    if t > time_weight.value: # 1.3
        arm_pitch.send_message(std_msgs.msg.Float64(-0.1))

