import pandas as pd
import numpy as np

#### data 
d0_user = pd.read_excel("./data/userinfo.xlsx")
d1_class = pd.read_excel("./data/classinfo.xlsx")
d1_class_reg = pd.read_excel("./data/class_registration.xlsx")
d2_phys = pd.read_excel("./data/physio_clinic_records.xlsx")

#### filtering variable setup
year_options_1 = sorted(list(set(d0_user['entry_year'])))
quarter_options_1 = sorted(list(set(d0_user['entry_quarter'])))
year_options_2 = sorted(list(set(d1_class['end_year'])))
month_options_2 = sorted(list(set(d1_class['end_month'])))

d0_user['gender'] = d0_user['gender'].apply(
    lambda x: 'Male' if str(x).strip() == "M" else 'Female' if str(x).strip() == "F" else np.nan
    )
d0_user['accessibility_levels'] = d0_user.apply(
    lambda x: 'High (1km; 10min)' if x['accessibility_1km_10min'] == 1 else 
              'Intermediate (3km; 30min)' if x['accessibility_3km_30min'] == 1 else
              'Low (5km; 60min)' if x['accessibility_5km_60min'] == 1 else 
              'Poor',
    axis = 1)
d0_user['initial_service_plan'] = d0_user['initial_service_plan'].apply(lambda x: 'Plan ' + str(x))
d0_user['assigned_service_plan'] = d0_user['assigned_service_plan'].apply(lambda x: 'Plan ' + str(x))
d0_user['hospital_residential_care'] = d0_user.apply(
    lambda x: 'prior hospitalization & residential care'if x['hospitalization'] == 1 and x['residential_care'] == 1 else
                'prior hospitalization' if x['hospitalization'] == 1 and x['residential_care'] == 0 else
                'prior residential care' if x['hospitalization'] == 0 and x['residential_care'] == 1 else
                'no hospitalization; no residential care',
    axis = 1)
d0_user['hospitalization'] = d0_user['hospitalization'].apply(lambda x: 'No' if x == 0 else 'Yes' if x == 1 else '')
d0_user['residential_care'] = d0_user['residential_care'].apply(lambda x: 'No' if x == 0 else 'Yes' if x == 1 else '')


gender_options = ["Male", "Female"]
age_options = ['<40', '40-49', '50-59', '60-64', '65-69', '>=70']
know_method_options = sorted(list(set(d0_user['know_method'])))
bool_options = ["No", "Yes"]

d2_phys['first_clinic_year'][d2_phys['first_clinic_year'] <= "2015-2016"] = "2016 or before"
d2_phys['final_clinic_year'][d2_phys['final_clinic_year'] <= "2015-2016"] = "2016 or before"

first_clinic_date_options = sorted([x for x in list(set(d2_phys['first_clinic_year'])) if pd.notnull(x) and x != '1899-1900'])
final_clinic_date_options = sorted([x for x in list(set(d2_phys['final_clinic_year'])) if pd.notnull(x) and x != '1899-1900'])

min_referral_release_date = min(d2_phys['referral_release_date'])
max_referral_release_date = max(d2_phys['referral_release_date'])

pain_pos_inclusion_value = 1
pain_pos_options = list(pd.DataFrame(
    d2_phys.iloc[:,14:].apply(lambda x: x.sum(), axis = 0)[
        d2_phys.iloc[:,14:].apply(lambda x: x.sum(), axis = 0) > pain_pos_inclusion_value
        ]
    ).index)
