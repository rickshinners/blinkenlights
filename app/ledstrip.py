
class IndicatorStrip:
    bibliopixel = None
    length = 0
    is_reversed = False

    def __init__(self, bibliopixel, length, is_reversed = False):
        self.bibliopixel = bibliopixel
        self.length = length
        self.is_reversed = is_reversed
        self.bibliopixel.all_off()
        self.bibliopixel.update()

    def length(self):
        return self.length

    def set(self, index, r, g, b):
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
