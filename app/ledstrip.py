
def _parse_ranges(ranges):
    result = set()
    if ranges is None:
        return result
    for part in ranges.split(','):
        x = part.split('-')
        result.update(range(int(x[0]), int(x[-1]) + 1))
    return sorted(result)


class IndicatorStrip:
    bibliopixel = None
    length = 0
    is_reversed = False

    def __init__(self, bibliopixel, length, is_reversed = False, is_disabled = False, disabled_pixels = None):
        self.bibliopixel = bibliopixel
        self.length = length
        self.is_reversed = is_reversed
        self.is_disabled = is_disabled
        self.disabled_pixels = _parse_ranges(disabled_pixels)
        self.bibliopixel.all_off()
        self.bibliopixel.update()

    def length(self):
        return self.length

    def set(self, index, r, g, b):
        if self._is_disabled(index):
            return
        self.bibliopixel.setRGB(self._get_index(index), r, g, b)
        self.bibliopixel.update()

    def get(self, index):
        return self.bibliopixel.get(index)

    def get_config(self, index):
        return {'rgb': self.bibliopixel.get(self._get_index(index))}

    def get_config_all(self):
        pixels = []
        for i in range(self.length):
            pixels.append(self.get_config(i))
        return pixels

    def _get_index(self, index):
        if index > self.length:
            raise IndexError("index out of range")
        if self.is_reversed:
            return self.length - index
        return index

    def _is_disabled(self, index):
        if self.is_disabled:
            return True
        if index in self.disabled_pixels:
            return True
        return False
