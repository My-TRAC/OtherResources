#!/bin/python2

import sys, os
import pandas as pd
from sets import Set
import processColumns as pc

data = pd.read_csv(sys.argv[1], sep = ",",dtype=str)
data_cols = ['TIMESTAMP','SCOPE','NTRIPS_W','NTRIPS_E','NTRIPS_P','NTRIPS_L','MODE','TRANSF','TOOLS','MAAS','COST','PTP','FLEX','HAPPINESS','TOLERANCE','PRE','M_COST','M_TIME','M_RELIABILITY','M_COMFORT','M_FLEXIBILITY','M_AVAILABILITY','M_SAFETY','M_SECURITY','M_LIVEINFO','M_ACTIVITIES','M_ACCESSIBILITY','M_WEATHER','M_PARKING','R_TIME','R_COST','R_NTRANSF','R_CROWDEDNESS','R_CONDITIONS','T_TIME','T_COST','T_NTRANSF','T_MODE','FLEXIBILITY','RELIABILITY','AVAILABILITY','SAFETY','SECURITY','ACCESSIBILITY','COMFORT','GENDER','AGE','INCOME','OCCUPATION','HOUSEHOLD','NCARS','NMOTO','NBIKE','HOMELOC','SMUSAGE','SOCIALMEDIA','ACCEPT','EVALUATION','X','MAIL']
data.columns=data_cols
data=data.drop(columns=['X','MAIL'])




data['TIMESTAMP'] = data['TIMESTAMP'].apply(pc.process_timestamp)
data['SCOPE'] = data['SCOPE'].apply(pc.process_scope)
data['NTRIPS_W'] = data['NTRIPS_W'].apply(pc.process_ntrips)
data['NTRIPS_E'] = data['NTRIPS_E'].apply(pc.process_ntrips)
data['NTRIPS_P'] = data['NTRIPS_P'].apply(pc.process_ntrips)
data['NTRIPS_L'] = data['NTRIPS_L'].apply(pc.process_ntrips)
data['MODE'] = data['MODE'].apply(pc.process_mode)
data['TRANSF'] = data['TRANSF'].apply(pc.process_transf)
data['TOOLS'] = data['TOOLS'].apply(pc.process_YesNo)
data['MAAS_TAXI'] = data['MAAS'].apply(pc.process_mass_t)
data['MAAS_UBER'] = data['MAAS'].apply(pc.process_mass_u)
data['MAAS_CS']= data['MAAS'].apply(pc.process_mass_cs)
data['MAAS_CP']= data['MAAS'].apply(pc.process_mass_cp)
data['MAAS'] = data['MAAS'].apply(pc.process_maas)
data['COST'] = data['COST'].apply(pc.process_cost)
data['PTP'] = data['PTP'].apply(pc.process_ptp)
data['FLEX'] = data['FLEX'].apply(pc.process_flex)
data['M_COST'] = data['M_COST'].apply(pc.process_importance)
data['M_TIME']  =  data['M_TIME'].apply(pc.process_importance) 
data['M_RELIABILITY'] = data['M_RELIABILITY'].apply(pc.process_importance) 
data['M_COMFORT'] =  data['M_COMFORT'].apply(pc.process_importance)  
data['M_FLEXIBILITY'] = data['M_FLEXIBILITY'].apply(pc.process_importance) 
data['M_AVAILABILITY'] = data['M_AVAILABILITY'].apply(pc.process_importance)  
data['M_SAFETY']  =  data['M_SAFETY'].apply(pc.process_importance) 
data['M_SECURITY'] =  data['M_SECURITY'].apply(pc.process_importance)  
data['M_LIVEINFO'] =  data['M_LIVEINFO'].apply(pc.process_importance)  
data['M_ACTIVITIES'] =  data['M_ACTIVITIES'].apply(pc.process_importance)  
data['M_ACCESSIBILITY'] = data['M_ACCESSIBILITY'].apply(pc.process_importance) 
data['M_WEATHER'] =  data['M_WEATHER'].apply(pc.process_importance)  
data['M_PARKING'] =  data['M_PARKING'].apply(pc.process_importance)  
data['R_TIME']  =  data['R_TIME'].apply(pc.process_importance) 
data['R_COST']  =  data['R_COST'].apply(pc.process_importance) 
data['R_NTRANSF'] =  data['R_NTRANSF'].apply(pc.process_importance)  
data['R_CROWDEDNESS'] = data['R_CROWDEDNESS'].apply(pc.process_importance) 
data['R_CONDITIONS'] =  data['R_CONDITIONS'].apply(pc.process_importance)  
data['T_TIME']  =  data['T_TIME'].apply(pc.process_importance) 
data['T_COST']  =  data['T_COST'].apply(pc.process_importance) 
data['T_NTRANSF'] =  data['T_NTRANSF'].apply(pc.process_importance)  
data['T_MODE']  =  data['T_MODE'].apply(pc.process_importance) 
data['FLEXIBILITY'] = data['FLEXIBILITY'].apply(pc.process_scale)  
data['RELIABILITY'] = data['RELIABILITY'].apply(pc.process_scale) 
data['AVAILABILITY']  = data['AVAILABILITY'].apply(pc.process_scale)  
data['SAFETY']  = data['SAFETY'].apply(pc.process_scale)  
data['SECURITY']  = data['SECURITY'].apply(pc.process_scale)  
data['ACCESSIBILITY'] = data['ACCESSIBILITY'].apply(pc.process_scale) 
data['COMFORT'] = data['COMFORT'].apply(pc.process_scale) 
data['GENDER']  =  data['GENDER'].apply(pc.process_sex)  
data['AGE'] =  data['AGE'].apply(pc.process_age) 
data['INCOME']  =  data['INCOME'].apply(pc.process_income) 
data['OCCUPATION'] =  data['OCCUPATION'].apply(pc.process_occupation)
data['HOUSEHOLD'] =  data['HOUSEHOLD'].apply(pc.process_household) 
data['NCARS'] =  data['NCARS'].apply(pc.process_number) 
data['NMOTO'] =  data['NMOTO'].apply(pc.process_number) 
data['NBIKE'] =  data['NBIKE'].apply(pc.process_number) 
data['HOMELOC'] =  data['HOMELOC'].apply(pc.process_homeloc) 
data['SMUSAGE'] =  data['SMUSAGE'].apply(pc.process_YesNo) 
data['SOCIALMEDIA']  =  data['SOCIALMEDIA'] 
data['ACCEPT']  =  data['ACCEPT'].apply(pc.process_YesNo) 
data['EVALUATION'] =  data['EVALUATION'].apply(pc.process_YesNo) 



data_cols_csv = ['TIMESTAMP','SCOPE','NTRIPS_W','NTRIPS_E','NTRIPS_P','NTRIPS_L','MODE','TRANSF','TOOLS','MAAS','MAAS_TAXI','MAAS_UBER','MAAS_CS','MAAS_CP','COST','PTP','FLEX','HAPPINESS','TOLERANCE','PRE','M_COST','M_TIME','M_RELIABILITY','M_COMFORT','M_FLEXIBILITY','M_AVAILABILITY','M_SAFETY','M_SECURITY','M_LIVEINFO','M_ACTIVITIES','M_ACCESSIBILITY','M_WEATHER','M_PARKING','R_TIME','R_COST','R_NTRANSF','R_CROWDEDNESS','R_CONDITIONS','T_TIME','T_COST','T_NTRANSF','T_MODE','FLEXIBILITY','RELIABILITY','AVAILABILITY','SAFETY','SECURITY','ACCESSIBILITY','COMFORT','GENDER','AGE','INCOME','OCCUPATION','HOUSEHOLD','NCARS','NMOTO','NBIKE','HOMELOC','SMUSAGE','SOCIALMEDIA','ACCEPT','EVALUATION']
data[data_cols_csv].to_csv(sys.argv[2])

