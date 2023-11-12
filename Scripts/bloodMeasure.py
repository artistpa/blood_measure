import spidev
import bloodFunctions as b
import time as time

start = time.time()
try:
    b.initSpiAdc()
    measures = []
    while (time.time() - start < 30):
        measures.append(b.getAdc())
    b.save(measures, start, start + 30)
finally:
    b.deinitSpiAdc()