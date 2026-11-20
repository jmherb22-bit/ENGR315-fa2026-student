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

from scipy import signal
from scipy.io import wavfile

# Read WAV file (replace "None")
sampling_rate, audio_data = wavfile.read("data/musical-notes/Guitar-note-1.wav")

"""
Task 1: Create a plot of the audio signal over time for its entire duration. For all graphs, include appropriate labels, titles, and legends. 
Include this plot as generated for Guitar-note-1 in your report.
"""
frequency, time, spectrogram = signal.spectrogram(audio_data, sampling_rate)


"""
Task 2: Develop a signal processing methodology appropriate for this problem. Create another plot(s) showing only a few periods of interest 
(relevant to the waveform of the musical note being played) of the original signal as well as your processed signal. For all graphs, include 
appropriate labels, titles, and legends. You may supplement this with more than one plot if you believe that is appropriate. 
Include this plot(s) as generated for Guitar-note-1 in your report.
"""

"""
Task 3: Employ an appropriate signal detection methodology to identify the note being played 
(i.e., 'A1', 'A#1', 'B1', 'C1', ... 'F7', 'F#7', G7, 'G#7', etc.) based on the signal's main frequency; 
each note corresponds to a specific frequency, such as 'C3', which is 131 Hz. 
A supplementary file note-frequencies-reference.csv for each note and its corresponding frequency has been added to the repository 
for you to reference. Your code must be able to accurately determine the note for any of the given audio files without alteration. 
Apply your code to all five recordings and include in your report a table showing the file name, detected frequency (Hz), 
and corresponding musical note for each recording.
"""

