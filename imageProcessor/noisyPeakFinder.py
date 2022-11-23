"""
    Function to find peaks in a graph.

    Receives a list with the data from the graph and creates a new one with the moving average of the data, where
    each point represents the average of the 2 previous points, the current one and the 2 following ones.

    The procedure is to go through the moving average list and keep track of the highest point so far,
    once the current point is less than the average of all the data, add the index of that point to the
    answer and search the next peak (if any)
"""

def findPeaks(signal):
    smoothed_values = [] # Ar
    for i in range(0,len(signal)):
        average = 0
        for j in range(-2,3):
            average += signal[i+j] if i + j >= 0 and i + j < len(signal) else signal[i]
        smoothed_values.append(average / 5)

    baseline = sum(signal) / len(signal)
    peak_indices = [] 
    peak_index, peak_val = None, None

    for index,val in enumerate(smoothed_values):
        if val > baseline:
            if not peak_val or val > peak_val:
                peak_index,peak_val = index,val
        elif val < baseline and peak_val:
            peak_indices.append(peak_index)
            peak_index,peak_val = None,None

    if peak_index:
        peak_indices.append(peak_index)

    return peak_indices