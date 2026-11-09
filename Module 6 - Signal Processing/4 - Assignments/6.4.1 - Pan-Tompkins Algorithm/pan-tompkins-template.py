import os

import numpy as np
from ekg_testbench import EKGTestBench
from scipy.signal import butter, filtfilt, find_peaks
from scipy.ndimage import median_filter, percentile_filter

def detect_heartbeats(filepath):
    """
    Perform analysis to detect location of heartbeats
    :param filepath: A valid path to a CSV file of heart beats
    :return: signal: a signal that will be plotted
    beats: the indices of detected heartbeats
    """
    if filepath == '':
        return list()

    # import the CSV file using numpy
    path = filepath
    fs = 360
    # load data in matrix from CSV file; skip first two rows
    ## your code here
    data = np.loadtxt(path, delimiter=',', skiprows=2)

    # save each vector as own variable
    ## your code here
    times = data[:, 0]
    channel_1 = data[:, 1]
    channel_2 = data[:, 2] if data.shape[1] > 2 else None

    # identify one column to process. Call that column signal

    signal = channel_1 ## your code here

    # pass data through LOW PASS FILTER (OPTIONAL)
    ## your code here
    nyq = fs / 2
    
    # pass data through HIGH PASS FILTER (OPTIONAL) to create BAND PASS result
    ## your code here
    b, a = butter(2, [5 / nyq, 15 / nyq], btype='band')
    signal = filtfilt(b, a, signal)

    # pass data through differentiator
    ## your code here
    signal = np.diff(signal, prepend=signal[0])

    # pass data through square function
    ## your code here
    signal = signal ** 2

    # pass through moving average window
    ## your code here
    window = int(0.15 * fs)
    signal = np.convolve(signal, np.ones(window) / window, mode='same')
    
    # use find_peaks to identify peaks within averaged/filtered data
    # save the peaks result and return as part of testbench result

    ## your code here peaks,_ = find_peaks(....)
    candidates, _ = find_peaks(signal, distance=int(0.25 * fs))

    heights = signal[candidates]
    local_ref = percentile_filter(heights, percentile=80, size=31, mode='nearest')

    keep = heights >= 0.35 * local_ref
    peaks = candidates[keep]
    beats = peaks
    
    # do not modify this line
    return signal, beats


# when running this file directly, this will execute first
if __name__ == "__main__":

    # place here so doesn't cause import error
    import matplotlib.pyplot as plt

    # database name
    database_name = 'mitdb_201'

    # set to true if you wish to generate a debug file
    file_debug = False

    # set to true if you wish to print overall stats to the screen
    print_debug = True

    # set to true if you wish to show a plot of each detection process
    show_plot = False

    ### DO NOT MODIFY BELOW THIS LINE!!! ###

    # path to ekg folder
    path_to_folder = "C:/Users/jmher/OneDrive/Documents/GitHub/ENGR315-fa2026-student/data/ekg/"
    # select a signal file to run
    signal_filepath = path_to_folder + database_name + ".csv"

    # call main() and run against the file. Should return the filtered
    # signal and identified peaks
    (signal, peaks) = detect_heartbeats(signal_filepath)

    # stop with a clear message if detect_heartbeats() is not finished yet
    if peaks is None:
        raise SystemExit("detect_heartbeats() returned None for beats. Finish the steps above and return the peak indices.")

    # matched is a list of (peak, annotation) pairs; unmatched is a list of peaks that were
    # not matched to any annotation; and remaining is annotations that were not matched.
    annotation_path = path_to_folder + database_name + "_annotations.txt"
    tb = EKGTestBench(annotation_path)
    peaks_list = peaks.tolist()
    (matched, unmatched, remaining) = tb.generate_stats(peaks_list)

    # if was matched, then is true positive
    true_positive = len(matched)

    # if response was unmatched, then is false positive
    false_positive = len(unmatched)

    # whatever remains in annotations is a missed detection
    false_negative = len(remaining)

    # calculate f1 score
    f1 = true_positive / (true_positive + 0.5 * (false_positive + false_negative))

    # if we wish to show the resulting plot
    if show_plot:
        # make a nice plt of results
        plt.title('Signal for ' + database_name + " with detections")

        plt.plot(signal, label="Filtered Signal")
        plt.plot(peaks, signal[peaks], 'p', label='Detected Peaks')

        true_annotations = np.asarray(tb.annotation_indices)
        plt.plot(true_annotations, signal[true_annotations], 'o', label='True Annotations')

        plt.legend()

        # uncomment line to show the plot
        plt.show()

    # if we wish to save all the stats to a file
    if file_debug:
        # print out more complex stats to the debug file
        debug_file_path = database_name + "_debug_stats.txt"
        debug_file = open(debug_file_path, 'w')

        # print out indices of all false positives
        debug_file.writelines("-----False Positives Indices-----\n")
        for fp in unmatched:
            debug_file.writelines(str(fp) + "\n")

        # print out indices of all false negatives
        debug_file.writelines("-----False Negatives Indices-----\n")
        for fn in remaining:
            debug_file.writelines(str(fn.sample) + "\n")

        # close file that we writing
        debug_file.close()

    if print_debug:
        print("-------------------------------------------------")
        print("Database|\t\tTP|\t\tFP|\t\tFN|\t\tF1")
        print(database_name, "|\t\t", true_positive, "|\t", false_positive, '|\t', false_negative, '|\t', round(f1, 3))
        print("-------------------------------------------------")

    print("Done!")
