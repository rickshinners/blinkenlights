from PluginBase import PluginBase
import logging


class SingleLedPluginBase(PluginBase):
    def __init__(self, config, set_pixel):
        super(SingleLedPluginBase, self).__init__(set_pixel)
        self.logger = logging.getLogger(__name__)
        self.strip = config['target_strip']
        self.led = config['led']


    def set_led(self, r, g, b):
        super(SingleLedPluginBase, self).set_led(self.strip, self.led, r, g, b)
