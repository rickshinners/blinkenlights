from bibliopixel.drivers.visualizer import DriverVisualizer
from bibliopixel.drivers.dummy_driver import DriverDummy
from bibliopixel.led import LEDStrip
from ledstrip import IndicatorStrip


def create_bibliopixel_strip(config):
    driver_type = config['driver_type']
    if driver_type == 'Dummy':
        driver = DriverDummy(num=config['pixel_count'])
    elif driver_type == 'Visualizer':
        driver = DriverVisualizer(width=config['pixel_count'], height=1, stayTop=config.get('stay_on_top', True))
    else:
        raise 'Unknown driver_type: {0}'.format(driver_type)
    bibliopixel_base_thing = LEDStrip(driver)
    return IndicatorStrip(bibliopixel_base_thing, config['pixel_count'], is_reversed=config.get('is_reversed', False))


def load_strips(config):
    strips = {}
    for strip_config in config:
        strips[strip_config['endpoint']] = create_bibliopixel_strip(strip_config)
    return strips
