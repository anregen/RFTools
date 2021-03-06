from unittest import TestCase
import RFTools


class TestRFTools(TestCase):
    def test_fspl(self):
        dist_km = 2
        freq_MHz = 5000
        expected = 112.44
        self.assertEqual(RFTools.fspl(freq_MHz, dist_km), expected)

        dist_km = 0
        expected = 0.0
        self.assertEqual(RFTools.fspl(freq_MHz, dist_km), expected)

    def test_fspl_invalid_input(self):
        dist_km = -2
        freq_MHz = 10
        self.assertRaises(ValueError, RFTools.fspl, freq_MHz, dist_km)

        dist_km = 2
        freq_MHz = -5
        self.assertRaises(ValueError, RFTools.fspl, freq_MHz, dist_km)

    def test_loss(self):
        ant_gain = 0
        tx_power = 0
        distance = 2
        freq = 5000
        sens = -110.44
        lc = RFTools.LinkCalc(freq, distance, ant_gain, tx_power, sens)
        ans = lc.margin()
        expected = -2
        self.assertEqual(ans, expected)

    def test_wavelength2freq(self):
        lam = 1     # m
        expected = 299792458.0
        self.assertEqual(RFTools.wavelength2freq(lam), expected)

        vp = 0.5
        expected *= vp
        self.assertEqual(RFTools.wavelength2freq(lam, vp), expected)

    def test_freq2wavelength(self):
        f = 300e6
        expected = 0.9993081933333333
        self.assertEqual(RFTools.freq2wavelength(f), expected)

        vp = 0.5
        expected *= vp
        self.assertEqual(RFTools.freq2wavelength(f, vp), expected)

    def test_cross_pol_gain(self):
        deg = 45
        expected = 0.5
        self.assertAlmostEqual(RFTools.cross_pol_gain(deg), expected)
