from PluginBase import PluginBase


class SingleLedPluginBase(PluginBase):
    def __init__(self, config):
        print "SingleLedPluginBase.__init__()"
        self.strip = config['target_strip']
        self.led = config['led']
        super(SingleLedPluginBase, self).__init__()

    def set_led(self, r, g, b):
        super(SingleLedPluginBase, self).set_led(self.strip, self.led, r, g, b)
