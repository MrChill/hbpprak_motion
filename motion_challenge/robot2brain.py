@nrp.MapSpikeSource("sensors", nrp.brain.sensors, nrp.dc_source)
@nrp.Robot2Neuron()
def set_neuron_rate(t, sensors):
    try:
        if t > 1.3:
            sensors.voltage = 100
            clientLogger.info("Neuron Input potential: {}".format(sensors.voltage))
    except ValueError:
        sensors.voltage = 0.0
