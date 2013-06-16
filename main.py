import math, wave, array

duration = 10 # seconds
freq = 23000 # of cycles per second (Hz) (frequency of the sine waves)
volume = 100 # percent
data = array.array('h') # signed short integer (-32768 to 32767) data
sampleRate = 96000 # of samples per second (standard)
numChan = 1 # of channels (1: mono, 2: stereo)
dataSize = 2 # 2 bytes because of using signed short integers => bit depth = 16
numSamplesPerCyc = int(sampleRate / freq)
numSamples = sampleRate * duration

for i in range(numSamples):
    sample = 32767 * float(volume) / 100
    sample *= math.sin(math.pi * 2 * (i % numSamplesPerCyc) / numSamplesPerCyc)
    data.append(int(sample))

f = wave.open('SineWave_' + str(freq) + 'Hz.wav', 'w')
f.setparams((numChan, dataSize, sampleRate, numSamples, "NONE", "Uncompressed"))
f.writeframes(data.tostring())
f.close()