import sys, os, signal

if os.uname()[4][:5]=='armv7':
	from snowboy.snowboy_rpi_armv7 import snowboydecoder
elif os.uname()[4][:5]=='armv6':
	from snowboy.snowboy_rpi_armv6 import snowboydecoder
else:
	from snowboy.snowboy_x86_64 import snowboydecoder


interrupted = False


def signal_handler(signal, frame):
    global interrupted
    interrupted = True


def interrupt_callback():
    global interrupted
    return interrupted

def detected():
    snowboydecoder.play_audio_file()
    sys.exit(0)

if len(sys.argv) == 1:
    print("Error: need to specify model name")
    print("Usage: python demo.py your.model sensitivity[Optional]")
    sys.exit(-1)

if len(sys.argv) == 2:
    sensi = sys.argv[2]
else:
    sensi=0.5

"""Detection sensitivity controls how sensitive the detection is. It is a value
between 0 and 1. Increasing the sensitivity value lead to better detection rate,
but also higher false alarm rate. It is an important parameter that you should
play with in your actual application."""

model = sys.argv[1]

# capture SIGINT signal, e.g., Ctrl+C
signal.signal(signal.SIGINT, signal_handler)

detector = snowboydecoder.HotwordDetector(model, sensitivity=sensi)
print('Listening... Press Ctrl+C to exit')

# main loop
detector.start(detected_callback=detected,
               interrupt_check=interrupt_callback,
               sleep_time=0.03)

detector.terminate()

if(not interrupted):
    sys.exit(0)
