import csv
import time


from midioutwrapper import *
mout, name = open_midioutput(interactive=True)
mw = MidiOutWrapper(mout, ch=1)
with open('data.csv', 'r', newline='') as csvfile:
    data = csv.DictReader(csvfile)
    for row in data:
        input("Enter for next Program change")
        mw.send_bank_select(msb=int(row['MSB']),lsb=int(row['LSB']))
        mw.send_program_change(int(row['PGM'])-1)
        print(row['NAME'])
input("Enter for next Program change")
print("END OF FILE")       
del mout