import pandas as pd
import numpy as np
from datetime import datetime


class Page_Main_Compute:
    def __init__(self, d0_user, d1_class, d2_phys):
        self.df0 = d0_user
        self.df1 = d1_class
        self.df2 = d2_phys
        self.recent_2_years = sorted(list(set(self.df0['entry_year'])))[-2:]
        
        self.df2a = self.df2[(self.df2['first_clinic_year'] != '1899-1900') & (self.df2['first_clinic_year'].notnull())]
        self.df2b = self.df2[(self.df2['final_clinic_year'] != '1899-1900') & (self.df2['final_clinic_year'].notnull())]

        self.new_entry = self.current_and_percentage(self.df0, "entry_year", "user_id", "count")
        self.contacts = self.group_aggregate_percentage(self.df0, ["entry_year"], "contact_consent", "Available").reset_index()
        self.new_contact_consent = self.current_and_percentage(self.contacts, "entry_year", "contact_consent", "sum")
        
        self.total_class = self.current_and_percentage(self.df1, "end_year", "class_id", "count")
        self.total_class_sess = self.current_and_percentage(self.df1, "end_year", "num_session", "sum")
        self.total_class_mins = self.current_and_percentage(self.df1, "end_year", "total_mins", "sum")
        self.total_class_registry = self.current_and_percentage(self.df1, "end_year", "num_registry", "sum")
        
        self.total_physio_intakes = self.current_and_percentage(self.df2a, "first_clinic_year", "user_id", "count")
        self.total_physio_discharges = self.current_and_percentage(
            self.df2b[self.df2b['final_status'] == "Discharge"], 
            "final_clinic_year", "user_id", "count")
        self.total_physio_intakes_with_pre_ax = self.current_and_percentage(
            self.df2a[self.df2a['referral_purpose'] != "Unspecified"], 
            "first_clinic_year", "user_id", "count")
        self.total_physio_dc_follow = self.current_and_percentage(
            self.df2b[self.df2b['final_status'] == "Doctor Followup"], 
            "final_clinic_year", "user_id", "count")

        self.aggregate_users_yr = self.group_aggregate(
            self.df0, 
            ['entry_year'], ['user_id'], ['count']
            )
        self.aggregate_users_qr = self.group_aggregate(
            self.df0[self.df0['entry_year'].isin(self.recent_2_years)], 
            ['entry_year','entry_quarter'], ['user_id'], ['count']
            )
        self.aggregate_users_mn = self.group_aggregate(
            self.df0[self.df0['entry_year'].isin(self.recent_2_years)], 
            ['entry_year','entry_month'], ['user_id'], ['count']
            )

    def current_and_percentage(self, df, year_col, value_col, method):
        new = df[df[year_col] == df[year_col].max()]
        prior = df[df[year_col] == sorted([x for x in list(set(df[year_col]))])[-2]]

        if method == "count":
            new_value = len(list(set(new[value_col])))
            prior_value = len(list(set(prior[value_col])))
        elif method == "sum":
            new_value = new[value_col].sum()
            prior_value = prior[value_col].sum()
        elif method == "mean":
            new_value = new[value_col].mean()
            prior_value = prior[value_col].mean()

        percent_change = (new_value - prior_value) / prior_value * 100
        return [new_value, percent_change]

    def group_aggregate(self, df, group_col, attribute_list, agg_methods):
        aggdf = df.groupby(group_col).agg({x: agg_methods for x in attribute_list})
        return aggdf
    
    def group_aggregate_percentage(self, df, group_col, attribute, criteria_value):
        aggdf = df.groupby(group_col)[attribute].apply(lambda x: (x == criteria_value).sum() / x.count())
        return aggdf


class Page_1_Compute:
    def __init__(self, d0_user, d1_class, d1_class_reg):
        self.df_user = d0_user

        self.df_reg = d1_class_reg.groupby(['user_id']).agg({'registrationDate': ['min'], 'start_date': ['min']}).reset_index()
        self.df_reg.columns = ['user_id','first_class_registrationDate','first_class_date']
        
        self.df_reg_count = d1_class_reg.groupby(['user_id']).agg({'registrationDate': ['count']}).reset_index()
        self.df_reg_count.columns = ['user_id','registration_counts']
        self.df_reg_count['registration_counts'] = self.df_reg_count['registration_counts'].apply(lambda x: np.log(x))
        self.df_reg_count.columns = ['user_id','log_registration_counts']
        
        self.df_sess_counts = d1_class_reg.merge(d1_class[['class_id','num_session']], how="left", left_on="class_id", right_on="class_id")
        self.df_sess_counts = self.df_sess_counts.groupby(['user_id']).agg({'num_session': ['sum']}).reset_index()
        self.df_sess_counts.columns = ['user_id','joined_sessions']
        self.df_sess_counts['joined_sessions'] = self.df_sess_counts['joined_sessions'].apply(lambda x: np.log(x))
        self.df_sess_counts.columns = ['user_id','log_joined_sessions'] 

    def new_admission(self, interactive_df, group_col):
        return interactive_df.groupby(group_col).agg({"user_id": ['count']})
    
    def contact_info_percentage(self, interactive_df, group_col):
        return interactive_df.groupby(group_col)["contact_consent"].apply(lambda x: (x == "Available").sum() / x.count())
    
    def high_accessiblity_percentage(self, interactive_df, group_col):
        return interactive_df.groupby(group_col)["accessibility_1km_10min"].apply(lambda x: x.sum()/x.count()*100)
    
    def moderate_accessiblity_percentage(self, interactive_df, group_col):
        return interactive_df.groupby(group_col)["accessibility_3km_30min"].apply(lambda x: x.sum()/x.count()*100)
    
    def low_accessiblity_percentage(self, interactive_df, group_col):
        return interactive_df.groupby(group_col)["accessibility_5km_60min"].apply(lambda x: x.sum()/x.count()*100)
    
    def hospitalization_percentage(self, interactive_df, group_col):
        return interactive_df.groupby(group_col)["hospitalization"].apply(lambda x: x.sum()/x.count()*100)
    
    def residential_care_percentage(self, interactive_df, group_col):
        return interactive_df.groupby(group_col)["residential_care"].apply(lambda x: x.sum()/x.count()*100)
    
    def entry2class_lead_time(self, interactive_df, group_col):
        temp = interactive_df.merge(self.df_reg, how='left', left_on=['user_id'], right_on=['user_id']).reset_index()
        temp['lead_time'] = temp.apply(lambda x: x['first_class_date'] - x['entry_date'], axis=1)
        temp['lead_time'] = temp['lead_time'].apply(lambda x: x.days)
        return {"raw_data": temp,  "aggregate_info": temp.groupby(group_col).agg({'lead_time': np.mean})}
    
    def lifetime_joined_sessions(self, interactive_df, group_col):
        temp = interactive_df.merge(self.df_sess_counts, how='left', left_on=['user_id'], right_on=['user_id']).reset_index()
        return {"raw_data": temp, "aggregate_info": temp.groupby(group_col).agg({'log_joined_sessions': np.mean})}
    

class Page_2_Compute:

    def two_variable_calculation(df, col_a, col_b, operator, operation_logic_order=None):
        sum_var_1 = df[col_a]
        sum_var_2 = df[col_b]

        assert operator in ["sum","subtract","product","division"], \
            "The operator must be one of the followings: ['sum','subtract','product','division']"

        if operator == "sum":
            return sum_var_1 + sum_var_2
        elif operator == "product":
            return sum_var_1 * sum_var_2
        elif operator == "subtract":
            if operation_logic_order == "a - b":
                return sum_var_1 - sum_var_2
            elif operation_logic_order == "b - a":
                return sum_var_2 - sum_var_1
            else:
                raise ValueError("Should be either 'a - b' or 'b - a'")
        elif operator == "division":
            if operation_logic_order == "a / b":
                return sum_var_1 / sum_var_2
            elif operation_logic_order == "b / a":
                return sum_var_2 / sum_var_1
            else:
                raise ValueError("Should be either 'a / b' or 'b / a'")
    
    def differentiate_single_double_var(
        two_variable_calculation,
        plot_df, group_cols, set_cols, set_fns, 
        two_var_operations, two_var_operations_logic, two_var_col_name
        ):
        if isinstance(set_cols, list) == True:
            plot_df = plot_df[group_cols + set_cols].groupby(group_cols).agg(
                {set_cols[0]: set_fns[0], set_cols[1]: set_fns[1]}
                ).reset_index()
            plot_df.columns = group_cols + set_cols
            plot_df[two_var_col_name] = two_variable_calculation(
                plot_df, set_cols[0], set_cols[1], two_var_operations, two_var_operations_logic
                )
            plot_df = plot_df[group_cols + [two_var_col_name]]
            var = two_var_col_name
        else:
            plot_df = plot_df.groupby(group_cols).agg({set_cols: set_fns}).reset_index()
            plot_df.columns = group_cols + [set_cols]
            var = set_cols
        return plot_df, var
            

class Page_3_Compute:

    def compute_lt(baseline, period):
        baseline = baseline.apply(lambda x: 
                                  str(x).replace("T", " ").replace(".000Z", "") 
                                  if x != None and pd.isnull(x) == False and x != 'nan' else 'nan')
        period = period.apply(lambda x: 
                              str(x).replace("T", " ").replace(".000Z", "") 
                              if x != None and pd.isnull(x) == False and x != 'nan' else 'nan')
        delta = [datetime.strptime(period.iloc[x], "%Y-%m-%d %H:%M:%S") - datetime.strptime(baseline.iloc[x], "%Y-%m-%d %H:%M:%S")  
                 if period.iloc[x] != 'nan' and baseline.iloc[x] != 'nan' else np.nan
                 for x in range(len(period))]
        return [x.days for x in pd.Series(delta)]
    
