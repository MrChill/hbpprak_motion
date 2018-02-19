
@nrp.MapSpikeSource("input_neuron", nrp.brain.neurons[0], nrp.dc_source)
@nrp.MapRobotSubscriber('model_states', Topic('/gazebo/model_states', gazebo_msgs.msg.ModelStates))
@nrp.Robot2Neuron()
def set_neuron_rate(t, input_neuron, model_states):
    states = model_states.value
    try:
        if t > 1.3:
            input_neuron.voltage = 10
            clientLogger.info("Neuron Input potential: {}".format(input_neuron.voltage))
    except ValueError:
        input_neuron.voltage = 0.0
