import logging


class PluginBase(object):
    def __init__(self, set_pixel):
        self.logger = logging.getLogger(__name__)
        self.set_pixel = set_pixel

    def run(self):
        pass

    def set_led(self, strip_name, index, r, g, b):
        self.logger.debug("set_led(strip_name=%s, index=%s, rgb=(%s,%s,%s))" % (strip_name, index, r, g, b))
        self.set_pixel(strip_name, index, r, g, b)
