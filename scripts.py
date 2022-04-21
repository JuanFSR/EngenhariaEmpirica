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