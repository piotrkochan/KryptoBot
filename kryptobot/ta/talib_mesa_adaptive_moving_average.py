from .generic_indicator import GenericIndicator
from talib import MAMA as indicator


class TalibMesaAdaptiveMovingAverage(GenericIndicator):

    def __init__(self, market, interval, periods, params):
        super().__init__(market, interval, periods, None, None, params)

    def next_calculation(self, candle):
        if self.get_datawindow() is not None:
            self.value = indicator(
                self.talib_data(self.get_close())
            )[-1]
