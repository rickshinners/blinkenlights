from SingleLedPluginBase import SingleLedPluginBase
import json
import requests


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


def _remove_secure_protocol(url):
    if url.index(':') == 5:
        return url[:4] + url[5:]
    return url


def _add_jenkins_api(url):
    return url.rstrip('/') + '/api/json'


class JenkinsPlugin(SingleLedPluginBase):
    def __init__(self, config, set_pixel):
        print "JenkinsPlugin.__init__()"
        super(JenkinsPlugin, self).__init__(config, set_pixel)
        self.url = config['job_url']

    def run(self):
        print "JenkinsPlugin.run()"
        jenkins_url = _remove_secure_protocol(_add_jenkins_api(self.url))
        job_data = json.loads(requests.get(jenkins_url).text)
        r, g, b = _get_rgb_from_jenkins_color(job_data['color'])
        self.set_led(r, g, b)