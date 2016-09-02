from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.drivers.dummy_driver import DriverDummy
from bibliopixel.drivers.APA102 import DriverAPA102, ChannelOrder
from bibliopixel.led import LEDStrip
from ledstrip import IndicatorStrip
import logging


def create_bibliopixel_strip(config):
    driver_type = config['driver_type']
    if driver_type == 'Dummy':
        driver = DriverDummy(num=config['pixel_count'])
    elif driver_type == 'Visualizer':
        driver = DriverVisualizer(width=config['pixel_count'], height=1, stayTop=config.get('stay_on_top', True))
    elif driver_type == 'APA102':
        driver = DriverAPA102(config['pixel_count'], c_order=ChannelOrder.GBR, dev='/dev/spidev32766.0')
    else:
        raise 'Unknown driver_type: {0}'.format(driver_type)
    bibliopixel_base_thing = LEDStrip(driver)
    return IndicatorStrip(bibliopixel_base_thing,
                          config['pixel_count'],
                          is_reversed=config.get('is_reversed', False),
                          is_disabled=config.get('is_disabled', False),
                          disabled_pixels=config.get('disabled_pixels', None))


def load_strips(config):
    logger = logging.getLogger(__name__)
    strips = {}
    if config is None or len(config) == 0:
        logger.info("No strips configured")
    else:
        for key in config:
            logger.info("Loading strip: %s" % key)
            strips[key] = create_bibliopixel_strip(config[key])
    return strips
