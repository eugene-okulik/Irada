fresult = 'operation result: 42'
sresult = 'operation result: 514'
fprogram = 'result of programs work: 9'

findex = fresult.index(':')
findex2 = sresult.index(':')
findex3 = fprogram.index(':')


firstres = int(fresult[findex+2:])
print(firstres + 10)

secres = int(sresult[findex2+2:])
print(secres + 10)

third = int(fprogram[findex3+2:])
print(third + 10)
