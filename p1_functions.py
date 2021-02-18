import math
import numpy as np
from numpy import genfromtxt


def read_co2_2(file_name = "co2_mm_mlo.txt", verbose=False):
    '''
    # from https://www.esrl.noaa.gov/gmd/ccgg/trends/
    # CO2 expressed as a mole fraction in dry air, micromol/mol, abbreviated as ppm
    #
    #  (-99.99 missing data;  -1 no data for #daily means in month)
    #
#            decimal       monthly    de-season  #days  st.dev  unc. of
#             date         average     alized          of days  mon mean
    '''

    data = genfromtxt(file_name, comments='#')

    dates = data[:,2]
    averages = data[:,3]
    if verbose:
        print (dates)
        print(averages)
    return [dates, averages]


def findPeriod(xdata, ydata):
	from scipy.signal import find_peaks

	peaks,_ = find_peaks(ydata)

	i = 0
	P = []
	for i in range(0,len(peaks),2):
		P.append(xdata[i+1] - xdata[i])

	T = np.average(P)

	return T


def indexToFreq(xdata,N):
	f = []
	for x in xdata:
		f.append(x/N)

	return f


def findPeaks(xdata, Ydata, thresh):
	from scipy.signal import find_peaks
	N = len(Ydata)
	peaks,_ = find_peaks(Ydata, threshold=thresh)
	xpeaks = []
	Ypeaks = []
	for p in peaks:
		xpeaks.append(xdata[p])
		Ypeaks.append(Ydata[p])

	return xpeaks, Ypeaks
