"""
    Function to count peaks in a graph.

    Receives a list with the data from the graph and creates a new one with the moving average of the data, where
    each point represents the average of the 2 previous points, the current one and the 2 following ones.

    The procedure is to go through the moving average list and keep track of the highest point so far,
    once the current point is less than the average of all the data, add one to the answer
    and search the next peak (if any)
"""

def count_peaks(signal):
    smoothed_values = [] 
    for i in range(0,len(signal)):
        average = 0
        for j in range(-2,3):
            average += signal[i+j] if i + j >= 0 and i + j < len(signal) else signal[i]
        smoothed_values.append(average / 5)

    baseline = sum(signal) / len(signal)

    peak_val = None
    peaks_count = 0
    for val in smoothed_values:
        if val > baseline:
            if not peak_val or val > peak_val:
                peak_val = val
        elif val < baseline and peak_val:
            peaks_count += 1
            peak_val = None

    if peak_val:
        peaks_count += 1

    return peaks_count