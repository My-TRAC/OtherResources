def process_timestamp(value):
    if value.find('P')!=-1:
        return value[0:value.find('P')]
    return value[0:value.find('A')]

def process_homeloc(value):
    if value == 'Urbana':
        return 1
    if value == 'Suburbana':
        return 2
    if value == 'Rural':
        return 3

def process_number(value):
    if len(value) == 2:
        return 5
    return value

def process_household(value):
    try:
        return int(value.strip())
    except ValueError:
        if value == 'Cinc':
            return 5
        if value =='Cuatre':
            return 4
        if value =='Dos':
            return 2
        if value =='Sis':
            return 6
        if value =='Tres':
            return 3
        print "Error processing household. Value = " +value
        return -1


def process_occupation(value):
    if 'Treballador' in value:
        return 1
    if value == 'Empresa privada':
        return 2
    if value == 'Atur':
        return 4
    if value == 'Jubilitat':
        return 5
    if value == 'Estudiant':
        return 6
    return 3


def process_income(value):
    if '12.000' in value and '25.000' in value:
        return 2
    if '12.000' in value:
        return 1
    if '25.000' in value:
        return 3
    
def process_age(value):
    if '18' in value:
        return 1
    if '25' in value:
        return 2
    if '35' in value:
        return 3
    if '45' in value:
        return 4
    if '55' in value:
        return 5
    return 6

def process_sex(value):
    if value == 'Dona':
        return 1
    if value == 'Home':
        return 0

def process_scale(value):
    if 'alta' in value:
        return 5
    if 'baixa' in value:
        return 1
    return value

def process_importance(value):
    if 'No' in value:
        # print value + ' 1'
        return 1         
    if 'Una' in value:
        # print value + ' 2'
        return 2
    if value == 'Important':
        # print value + ' 3'
        return 3
    if 'Molt' in value:
        # print value + ' 4'
        return 4
    if 'Extramadament' in value or 'Extremadament':
        # print value + ' 5'
        return 5

def process_ptp(value):
    if value == 'Yes':
        return 1
    return 2

def process_flex(value):
    # print value
    if 'fixes' in value:
        return 1
    return 2
def process_cost(value):

    if '20-40' in value:
        return 2
    if '40 -60' in value:
        return 3
    if '>60' in value:
        return 4
    return 1

def process_scope(value):
    if value.find('(') !=-1:
        return 3
    if value == 'Feina':
        return 1
    if value == 'Estudis':
        return 2
    if value =='Plaer':
        return 4                                         

def process_ntrips(value):
    if value == '0':
        return 0
    if value == '<5':
        return 1
    if value == '5-10':
        return 2
    if value =='10-15':
        return 3
    if value =='>15':
        return 4

def process_mode(value):
    if value == 'Cotxe':
        return 1
    if value == 'Bus':
        return 2
    if value == 'Metro':
        return 3
    if value == 'Tren':
        return 4
    if value == 'Tramvia':
        return 5
    if value == 'Bicicleta':
        return 6
    if value == 'Moto':
        return 7
    if value == 'Caminant':
        return 8

    print "Error processing mode. Value = " + value
    return -1

def process_transf(value):
    try:
        return int(value)
    except ValueError:
        value=value.lower().strip()                                   
        if value.startswith('cap') or value.startswith('ninguno') or value.startswith('nada') or value.startswith('zero'):
            return 0
        if value.startswith('un') or value.startswith('uno'):
            return 1
        if value.startswith('dos'):
            return 2

        print "Error processing transfers. Value = " + value 

        return -1

def process_YesNo(value):
    if value == 'No':
        return 0
    return 1                                   

def process_maas(value):
    return_value=''
    if 'Taxi' in value:
        return_value+=',1'
    if 'Uber' in value:
        return_value+=',2'
    if 'Car-sharing' in value:
        return_value+=',3'
    if 'Car-pooling' in value:
        return_value+=',4'
    if return_value=='':
        return_value=',0'

    return return_value[1:]

def process_mass_t(value):
    if 'Taxi' in value:
        return 1
    return 0

def process_mass_u(value):
    if 'Uber' in value:
        return 1
    return 0

def process_mass_cs(value):
    if 'Car-sharing' in value:
        return 1
    return 0

def process_mass_cp(value):
    if 'Car-pooling' in value:
        return 1
    return 0
   
