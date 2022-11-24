import matplotlib.pyplot as plt
import numpy as np
from scipy.signal import find_peaks

def count_peaks(signal):
    min_index = signal.index(min(signal))
    signal = signal[min_index:] + signal[:min_index]
    smoothed_values = []
   
    for i in range(0,len(signal)):
        average = 0
        for j in range(-2,3):
            average += signal[(i+j) % len(signal)]
        smoothed_values.append(average / 5)
    
    peaks, _ = find_peaks(smoothed_values, height=0)
    mean = sum(smoothed_values) / len(smoothed_values)
    peaks = [peak for peak in peaks if smoothed_values[peak] >= (mean * .9)]
    return len(peaks)