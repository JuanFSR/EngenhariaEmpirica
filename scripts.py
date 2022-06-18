import numpy as np
from math import sqrt

def getDateFormat(data):
    valoresDateFormat = []
    ano = []
    mes = []
    dia = []

    for idx, a in enumerate(data):
        valoresDateFormat.append([])

        for idx2, date in enumerate(a.split('T')[0].split('-')):

            if idx2 == 0: 
                ano.append(int(date))
            elif idx2 == 1: 
                mes.append(int(date))
            elif idx2 == 2: 
                dia.append(int(date))
                valoresDateFormat[idx].append([ano, mes, dia])
    
    return valoresDateFormat

def returnY(max):
    y = []
    for i in range(1, max+1):
        y.append(i)
    return y

def cohend(d1, d2):
	n1, n2 = len(d1), len(d2)
	s1, s2 = np.var(d1, ddof=1), np.var(d2, ddof=1)
	s = sqrt(((n1 - 1) * s1 + (n2 - 1) * s2) / (n1 + n2 - 2))
	u1, u2 = np.mean(d1), np.mean(d2)
	return (u1 - u2) / s