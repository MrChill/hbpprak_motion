
@nrp.MapSpikeSink("output_neuron", nrp.brain.neurons[1], nrp.leaky_integrator_alpha)
@nrp.Neuron2Robot(Topic('/robot/hollie_real_left_arm_2_joint/cmd_pos', std_msgs.msg.Float64))
# Example TF: get output neuron voltage and actuate the arm with the current simulation time. You could do something with the voltage here and command the robot accordingly.
def swing(t, output_neuron):
    pos = -40
    if current_ball_state.pose.position.y < 2:
        pos = 20
    voltage=output_neuron.voltage
    return std_msgs.msg.Float64(pos)
