from multiprocessing import Process
import multiprocessing
from array import array
from multiprocessing import Queue
import pyaudio
import os
import wave
import sys

#Audio recording
FORMAT = pyaudio.paInt16
CHANNELS = 1
IN_RATE = 48000
OUT_RATE = 16000
CHUNK = 1024 * (IN_RATE/OUT_RATE)
MIN_VOLUME = 1000
# if the recording thread can't consume fast enough, the listener will start discarding
BUF_MAX_SIZE = CHUNK * 100


if len(sys.argv) == 1:
    print("Error: need to specify file path")
    print("Usage: python script.py your.path")
    sys.exit(-1)

WAVE_OUTPUT_FILENAME = sys.argv[1]+"file.raw"

def main():
        #voir  la taille de q
        q = Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK)))
        listen_p = Process(target=listen, args=(q,))
        listen_p.start()
        record_p = Process(target=record, args=(q,))
        record_p.start()

        try:
            while record_p.is_alive():
                listen_p.join(0.1)
                record_p.join(0.1)
            listen_p.terminate()


        except KeyboardInterrupt:
            listen_p.terminate()
            record_p.terminate()
        listen_p.join()
        record_p.join()

def downsample(chunk):
    return chunk[::int(1 / (OUT_RATE*1./IN_RATE) )]

def record(q):
    count = 0
    frames = []
    recording = True
    while count<40:
        chunk = q.get()
        vol = max(chunk) # voir valeur moyenne
        if vol >= MIN_VOLUME:
            recording = True
            count = 0
            #print(vol)
            #print(type(q.get))
        else:
            count = count+1
            #print("-")
        if recording:
            frames.append(downsample(chunk).tostring())

    if recording:
        waveFile = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        waveFile.setnchannels(CHANNELS)
        waveFile.setsampwidth(pyaudio.PyAudio().get_sample_size(FORMAT))
        waveFile.setframerate(OUT_RATE)
        waveFile.writeframes(b''.join(frames))
        waveFile.close()
        print("Fichier enregistre!")

    else:
        print("Annulation")

def listen(q,):
    stream = pyaudio.PyAudio().open(
        format=pyaudio.paInt16,
        channels=1,
        rate=IN_RATE,
        input=True,
        frames_per_buffer=1024,
        )
    while True:
        try:
            q.put(array('h', stream.read(CHUNK)))
        except Queue.full:
            pass  # discard


if __name__ == '__main__':
    """testVolume = pyaudio.PyAudio().open(
        format=pyaudio.paInt16,
        channels=2,
        rate=16000,
        input=True,
        frames_per_buffer=1024,
        )
    #tps avant lancement
    i=1;
    q0 = multiprocessing.Queue(maxsize=int(round(BUF_MAX_SIZE / CHUNK)))
    while (i<10):
            q0.put(array('h', testVolume.read(CHUNK)))
            i=i+1
    max(q0.get()))
    testVolume.stop_stream()
    testVolume.close()
    pyaudio.PyAudio().terminate()
    q0.close()"""
    main()
