# Input File Name
filename = input('Enter the file name: ')
try:
    filehandle = open(filename)
except:
    print('File cannot be opened: ', filename)
    quit()

# Collecting DSPAM
count = 0
fspam = 0.0
for line in filehandle:
    line = line.rstrip()
    if line.startswith('X-DSPAM-Confidence:'):
        count+= 1
        dspam = line[18+1 : ]
        dspam = float(dspam)
        fspam+= dspam

fspam = fspam / count
print(fspam)
