from PluginBase import PluginBase


class SingleLedPluginBase(PluginBase):
    def __init__(self, config, set_pixel):
        print "SingleLedPluginBase.__init__()"
        self.strip = config['target_strip']
        self.led = config['led']
        super(SingleLedPluginBase, self).__init__(set_pixel)

    def set_led(self, r, g, b):
        super(SingleLedPluginBase, self).set_led(self.strip, self.led, r, g, b)
