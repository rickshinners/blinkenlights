from PluginBase import PluginBase


class TestPlugin(PluginBase):
    def __init__(self, config, set_pixel):
        print "TestPlugin.__init__()"
        self.strip = config['target_strip']
        self.led = config['led']
        super(TestPlugin, self).__init__(set_pixel)

    def run(self):
        print "TestPlugin.run()"
        self.set_led(self.strip, self.led, 128, 196, 212)
