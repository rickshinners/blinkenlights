from PluginBase import PluginBase
import logging


class TestPlugin(PluginBase):
    def __init__(self, config, set_pixel):
        super(TestPlugin, self).__init__(set_pixel)
        self.logger = logging.getLogger(__name__)
        self.logger.debug("__init__()")
        self.strip = config['target_strip']
        self.led = config['led']

    def run(self):
        self.logger.debug("run()")
        self.set_led(self.strip, self.led, 128, 196, 212)
