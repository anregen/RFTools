from unittest import TestCase
import RFTools


class TestLinkCalc(TestCase):
    tolerance_digits = 3

    def test_margin(self):
        tx_ant_gain = 0
        rx_ant_gain = 0
        tx_power = 0
        distance = 2
        freq = 5000
        sens = -110.44
        lc = RFTools.LinkCalc(freq, distance, tx_ant_gain, rx_ant_gain, tx_power, sens)
        ans = lc.margin()
        expected = -2
        self.assertAlmostEqual(ans, expected, places=self.tolerance_digits)

    def test_distance(self):
        tx_ant_gain = 3
        rx_ant_gain = 3
        tx_power = 2
        distance = 2
        freq = 5000
        sens = -110.44
        lc = RFTools.LinkCalc(freq, distance, tx_ant_gain, rx_ant_gain, tx_power, sens)
        ans = lc.distance(margin_dB=6)
        expected = 2
        self.assertAlmostEqual(ans, expected, places=self.tolerance_digits)
