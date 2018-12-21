from math import log10, cos, pow, radians, pi
from scipy import constants


def fspl(freq_MHz=None, dist_km=None):
    """

    :rtype: path loss as positive value in dB
    """
    if (freq_MHz == 0.0) or (dist_km == 0.0):
        return 0.0
    else:
        return 32.44+(20*log10(freq_MHz))+(20*log10(dist_km))


def cross_pol_gain(angle_mismatch_d):
    return pow(cos(radians(angle_mismatch_d)), 2)


def ratio2dB(ratio):
    return 10*log10(ratio)


def dB2ratio(dB):
    return pow(10, dB/10)


def wavelength2freq(lam, vel_prop=1):
    return constants.c*vel_prop/lam


def freq2wavelength(f, vel_prop=1):
    return constants.c*vel_prop/f


class LinkCalc:
    freq_MHz = None
    dist_km = None
    tx_ant_gain = None
    rx_ant_gain = None
    radio = None

    def __init__(self, freq_MHz, dist_km, tx_ant_gain, rx_ant_gain, radio):
        self.freq_MHz = freq_MHz
        self.dist_km = dist_km
        self.tx_ant_gain = tx_ant_gain
        self.rx_ant_gain = rx_ant_gain
        self.radio = radio

    def margin(self, dist_km=None):
        if dist_km is None:
            dist_km = self.dist_km
        eirp = self.radio.tx_power+self.tx_ant_gain
        pg = -1*fspl(self.freq_MHz, dist_km)
        return eirp + pg + self.rx_ant_gain - self.radio.rx_sens

    def distance(self, margin_dB=3):
        acceptable_pl = self.radio.tx_power + self.tx_ant_gain + self.rx_ant_gain - self.radio.rx_sens - margin_dB
        dist_m = 10 ** ((acceptable_pl + 20 * log10(300000000 / (4 * pi * self.freq_MHz * 1000000))) / 20)
        return dist_m/1000.0


class Radio:
    rx_sens = None
    tx_power = None

    def __init__(self, rx_sens, tx_power):
        self.rx_sens = rx_sens
        self.tx_power = tx_power


class Antenna:
    def gain(self, freq):
        pass
