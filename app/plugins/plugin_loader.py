from TestPlugin import TestPlugin


def load_plugins(config, scheduler):
    for plugin_name in config:
        try:
            plugin_config = config[plugin_name]
            plugin = _load_plugin_type(plugin_config)
            schedule_config = plugin_config['schedule']
            schedule_type = schedule_config['type']
            if schedule_type == 'cron':
                scheduler.add_job(plugin.run, 'cron', id=plugin_name,
                                  second=schedule_config.get('second', '*'),
                                  minute=schedule_config.get('minute', '*'),
                                  hour=schedule_config.get('hour', '*'),
                                  day_of_week=schedule_config.get('day_of_week', '*'),
                                  week=schedule_config.get('week', '*'),
                                  day=schedule_config.get('day', '*'),
                                  month=schedule_config.get('month', '*'),
                                  year=schedule_config.get('year', '*'),
                                  start_date=schedule_config.get('start_date', None),
                                  end_date=schedule_config.get('end_date', None))
            elif schedule_type == 'interval':
                scheduler.add_job(plugin.run, 'interval', id=plugin_name,
                                  seconds=schedule_config.get('seconds', 0),
                                  minutes=schedule_config.get('minutes', 0),
                                  hours=schedule_config.get('hours', 0),
                                  days=schedule_config.get('days', 0),
                                  weeks=schedule_config.get('weeks', 0),
                                  start_date=schedule_config.get('start_date', None),
                                  end_date=schedule_config.get('end_date', None))
            else:
                raise Exception("Unknown schedule type: %s" % schedule_type)
        except Exception, e:
            print "Could not load plugin: %s" % plugin_name
            print e


def _load_plugin_type(config):
    type_name = config['plugin_type']
    if type_name == 'TestPlugin':
        return TestPlugin(config)
    else:
        raise Exception("Unknown plugin type: %s" % type_name)
