class PluginBase(object):
    def __init__(self):
        print "PluginBase.__init__()"

    def run(self):
        print "PluginBase.run()"

    def set_led(self, strip_name, index, r, g, b):
        print "PluginBase.set_led(strip_name=%s, index=%s, rgb=(%s,%s,%s))" % (strip_name, index, r, g, b)
