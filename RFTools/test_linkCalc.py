from unittest import TestCase
import RFTools


class TestLinkCalc(TestCase):
    tolerance_digits = 3

    def test_margin(self):
        tx_ant_gain = 0
        rx_ant_gain = 0
        tx_power = 0
        sens = -110.44
        radio = RFTools.Radio(sens, tx_power)
        freq = 5000
        dist = 2

        lc = RFTools.LinkCalc(freq, tx_ant_gain, rx_ant_gain, radio)
        ans = lc.margin(dist_km=dist)
        expected = -2
        self.assertAlmostEqual(ans, expected, places=self.tolerance_digits)

    def test_distance(self):
        tx_ant_gain = 3
        rx_ant_gain = 3
        tx_power = 2
        freq = 5000
        sens = -110.44
        radio = RFTools.Radio(sens, tx_power)
        lc = RFTools.LinkCalc(freq, tx_ant_gain, rx_ant_gain, radio)
        ans = lc.distance(margin_dB=6)
        expected = 2
        self.assertAlmostEqual(ans, expected, places=self.tolerance_digits)
