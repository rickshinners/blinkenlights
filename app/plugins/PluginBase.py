class PluginBase(object):
    def __init__(self, set_pixel):
        print "PluginBase.__init__()"
        self.set_pixel = set_pixel

    def run(self):
        print "PluginBase.run()"

    def set_led(self, strip_name, index, r, g, b):
        print "PluginBase.set_led(strip_name=%s, index=%s, rgb=(%s,%s,%s))" % (strip_name, index, r, g, b)
        self.set_pixel(strip_name, index, r, g, b)
