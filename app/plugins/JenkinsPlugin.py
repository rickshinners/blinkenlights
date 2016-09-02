from SingleLedPluginBase import SingleLedPluginBase
from PluginBase import PluginBase
import json
import requests
import logging


def _get_rgb_from_jenkins_color(jenkins_color):
    jenkins_color = str(jenkins_color).lower()
    if jenkins_color.endswith('_anime'):
        return 0, 0, 128
    if jenkins_color == 'red' or jenkins_color == 'aborted':
        return 255, 0, 0
    if jenkins_color.startswith('yellow'):
        return 64, 64, 0
    if jenkins_color.startswith('blue'):
        return 0, 128, 0
    return 0, 0, 0


def _get_rgb_from_jenkins_building_and_result(building, result):
    if building:
        return 0, 0, 128
    if result == 'SUCCESS':
        return 0, 128, 0
    if result == 'UNSTABLE':
        return 128, 128, 0
    return 255, 0, 0


def _remove_secure_protocol(url):
    if url.index(':') == 5:
        return url[:4] + url[5:]
    return url


def _add_jenkins_api(url):
    return url.rstrip('/') + '/api/json'


class JenkinsPlugin(SingleLedPluginBase):
    def __init__(self, config, set_pixel):
        super(JenkinsPlugin, self).__init__(config, set_pixel)
        self.logger = logging.getLogger(__name__)
        self.url = config['job_url']

    def run(self):
        self.logger.debug("run()")
        jenkins_url = _remove_secure_protocol(_add_jenkins_api(self.url))
        job_data = json.loads(requests.get(jenkins_url).text)
        r, g, b = _get_rgb_from_jenkins_color(job_data['color'])
        self.set_led(r, g, b)


class JenkinsHistoryPlugin(PluginBase):
    def __init__(self, config, set_pixel):
        super(JenkinsHistoryPlugin, self).__init__(set_pixel)
        self.logger = logging.getLogger(__name__)
        self.url = config['job_url']
        self.count = config.get('count', 1)
        self.start_pixel = config['start_pixel']
        self.target_strip = config['target_strip']

    def run(self):
        self.logger.debug("run()")
        jenkins_url = _remove_secure_protocol(_add_jenkins_api(self.url))
        job_data = json.loads(requests.get(jenkins_url).text)
        job_urls = [x['url'] for x in job_data['builds']]
        for i in range(self.count):
            self._set_history_pixel(job_urls[i], self.start_pixel + i)

    def _set_history_pixel(self, url, led):
        jenkins_url = _remove_secure_protocol(_add_jenkins_api(url))
        job_data = json.loads(requests.get(jenkins_url).text)
        r, g, b = _get_rgb_from_jenkins_building_and_result(job_data['building'], job_data['result'])
        self.set_led(self.target_strip, led, r, g, b)