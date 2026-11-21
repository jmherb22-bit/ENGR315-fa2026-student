"""
CULMINATING ASSIGNMENT 3: Musical Note Detection

Create a program which detects the note being played from the given audio file based on its frequency.
It is up to you to employ an appropriate methodology to process the audio signal and detect the note.
The relevant data file is named "Guitar-note-1.wav" and is located in data > musical-notes.
In the same directory, we also provide a reference for the corresponding frequencies of each note.

Your code needs to be successful as well as sufficiently commented/documented to receive full credit.
We have provided a possible method for converting the .wav file to usable data below.
All file paths need to be relative and execute from this file's directory;
the Visual Studio Code setting "Python > Terminal: Execute in File Dir" 
must be enabled in File > Preferences > Settings.

See Canvas for additional requirements.
"""

import numpy as np
import pandas as pd
from matplotlib import pyplot as plt
from scipy import signal
from scipy.io import wavfile

# Read WAV file (replace "None")
sampling_rate, audio_data = wavfile.read("data/musical-notes/Guitar-note-1.wav")

# convert integer samples to float and convert stereo to mono
audio_data = audio_data.astype(float)
if audio_data.ndim > 1:
    audio_data = audio_data.mean(axis=1)

# Time axis built from the sample count
time = np.arange(len(audio_data)) / sampling_rate

"""
Task 1: Create a plot of the audio signal over time for its entire duration. For all graphs, include appropriate labels, titles, and legends. 
Include this plot as generated for Guitar-note-1 in your report.
"""
plt.figure(figsize=(10, 6))
plt.plot(time, audio_data)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title("Audio Signal")
plt.legend()
plt.grid(True)
plt.show()
"""
Task 2: Develop a signal processing methodology appropriate for this problem. Create another plot(s) showing only a few periods of interest 
(relevant to the waveform of the musical note being played) of the original signal as well as your processed signal. For all graphs, include 
appropriate labels, titles, and legends. You may supplement this with more than one plot if you believe that is appropriate. 
Include this plot(s) as generated for Guitar-note-1 in your report.
"""
def bandpass(data, fs, low=60, high=2500): #butterworth bandpass filter
    sos = signal.butter(4, [low, high], btype="bandpass", fs=fs, output="sos")
    return signal.sosfiltfilt(sos, data)


def detect_frequency(data, fs, fmin=60, fmax=2500): #Find main freq and return the spectrum for plotting
    x = data - np.mean(data) # remove DC offset
    x = x * np.hanning(len(x)) # window to reduce spectral leakage
    n_fft = 8 * len(x) # zero-pad for finer bin spacing
    spectrum = np.abs(np.fft.rfft(x, n=n_fft))
    freqs = np.fft.rfftfreq(n_fft, d=1 / fs)
    band = (freqs >= fmin) & (freqs <= fmax)
    peak = np.argmax(spectrum[band])
    return freqs[band][peak], freqs, spectrum


def frequency_to_note(freq, ref_df): #Compare freq to note freq 
    """Return the note whose reference frequency is closest to freq."""
    idx = (ref_df["Frequency"] - freq).abs().idxmin()
    return ref_df.loc[idx, "Note"], ref_df.loc[idx, "Frequency"]


filtered = bandpass(audio_data, sampling_rate)
f0, freqs, spectrum = detect_frequency(filtered, sampling_rate)

# Zoom in on periods shortly after note start 
period = 1 / f0
start = int(0.1 * sampling_rate)
stop = start + int(5 * period * sampling_rate)

plt.figure(figsize=(10, 6))
plt.plot(time[start:stop], audio_data[start:stop], label="Original", alpha=0.6)
plt.plot(time[start:stop], filtered[start:stop], label="Band-pass filtered", linewidth=2)
plt.xlabel("Time (s)")
plt.ylabel("Amplitude")
plt.title(f"Original vs. Processed Signal (~5 periods, f0 ≈ {f0:.1f} Hz)")
plt.legend()
plt.grid(True)
plt.show()

# Frequency spectrum with the detected peak marked
plt.figure(figsize=(10, 6))
plt.plot(freqs, spectrum, label="FFT magnitude")
plt.axvline(f0, color="r", linestyle="--", label=f"Peak: {f0:.1f} Hz")
plt.xlim(0, 2500)
plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("Frequency Spectrum of Filtered Signal")
plt.legend()
plt.grid(True)
plt.show()

"""
Task 3: Employ an appropriate signal detection methodology to identify the note being played 
(i.e., 'A1', 'A#1', 'B1', 'C1', ... 'F7', 'F#7', G7, 'G#7', etc.) based on the signal's main frequency; 
each note corresponds to a specific frequency, such as 'C3', which is 131 Hz. 
A supplementary file note-frequencies-reference.csv for each note and its corresponding frequency has been added to the repository 
for you to reference. Your code must be able to accurately determine the note for any of the given audio files without alteration. 
Apply your code to all five recordings and include in your report a table showing the file name, detected frequency (Hz), 
and corresponding musical note for each recording.
"""
# Reference table
ref = pd.read_csv("data/musical-notes/note-frequencies-reference.csv")
ref.columns = ["Note", "Frequency"]

results = []
for i in range(1, 6):
    file_name = f"Guitar-note-{i}.wav"

    # Same read line as the starter, with a variable file path
    sampling_rate, audio_data = wavfile.read(f"data/musical-notes/{file_name}")
    audio_data = audio_data.astype(float)
    if audio_data.ndim > 1:
        audio_data = audio_data.mean(axis=1)

    filtered = bandpass(audio_data, sampling_rate)
    freq, _, _ = detect_frequency(filtered, sampling_rate)
    note, ref_freq = frequency_to_note(freq, ref)

    results.append({
        "File": file_name,
        "Detected Frequency (Hz)": round(freq, 2),
        "Note": note,
        "Reference Frequency (Hz)": ref_freq,
    })

results_df = pd.DataFrame(results)
print(results_df.to_string(index=False))