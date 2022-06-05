lista_notowan = [('CCC',122.55,121.7,123.5,122.4),
('ERG',43,41.2,44.8,43.6),
('IMS',2.99,2.99,3.05,3.05),
('INTROL',5.08,4.84,5.08,4.94),
('PEPCO',47.25,46.945,48.2,48),
('ROPCZYCE',31.4,30.7,31.4,31.3),
('TSGAMES',350.6,348,359.6,352.6),
('WIRTUALNA',151,145.8,155.4,147.8)]

kursy_walut = {
'1 USD':3.9911,
'1 AUD':2.9424,
'1 HKD':0.5127,
'1 CAD':3.1997,
'1 EUR':4.6065,
'100 HUF':1.28,
'1 CHF':4.362,
'1 GBP':5.3604,
'100 JPY':3.5065,
'10000 IDR':2.7856,
'1 CNY':0.6235}

#zaktualizowanie slownika kursow walut- funkcja na zmiane nazw kluczy
def keep_three_last_elements(dictionary):
    new_dictionary = {}
    for key in dictionary:
        new_dictionary[key[-3:]] = dictionary[key]
    return new_dictionary

kursy_walut = keep_three_last_elements(kursy_walut)

#zmiana wartosci walut na jednostke
kursy_walut.update(HUF=0.0128, JPY=0.035065, IDR=0.00027856)

#funkcja
def maxZmGPW(lista_notowan, kursy_walut, waluta):
    if len(lista_notowan) == 0:
        return None
    else:
        max_zmiennosc = 0
        for i in range(len(lista_notowan)):
            zmiennosc = (lista_notowan[i][3] + lista_notowan[i][4]) / (lista_notowan[i][1] + lista_notowan[i][2])
            if zmiennosc > max_zmiennosc:
                max_zmiennosc = zmiennosc
                max_zmiennosc_index = i
        if waluta in kursy_walut:
            return (lista_notowan[max_zmiennosc_index][0],
                    lista_notowan[max_zmiennosc_index][1] / kursy_walut[waluta],
                    lista_notowan[max_zmiennosc_index][2] / kursy_walut[waluta],
                    lista_notowan[max_zmiennosc_index][3] / kursy_walut[waluta],
                    lista_notowan[max_zmiennosc_index][4] / kursy_walut[waluta])
        else:
            return (lista_notowan[max_zmiennosc_index][0], 0, 0, 0, 0)



maxZmGPW(lista_notowan, kursy_walut, "EUR")
