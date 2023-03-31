def es_bisiesto(anyo):
    if anyo % 4 == 0:
        if anyo % 100 == 0:
            if anyo % 400 == 0:
                print('Es bisiesto!')
            else:
                print('No es bisiesto.')
        else:
            print('Es bisiesto!')
    else:
        print('No es bisiesto.')


es_bisiesto(2008)