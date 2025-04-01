def data_magica(dia, mes, ano):
    if dia * mes == ano % 100:
        return True
    else:
        return False
    
print(data_magica(10, 6, 1960))
print(data_magica(10, 6, 1961))
