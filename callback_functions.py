import pandas as pd
import dash
from dash.dependencies import Input, Output, State


class Page_1_Interactive_DataFrame:
    def __init__(self, 
                 app,
                 d0_user, 
                 input_widget_1, input_widget_2, input_widget_3, input_widget_4, input_widget_5, input_widget_6):

        self.app = app
        
        self.df_full = d0_user

        self.input_widget_1 = input_widget_1
        self.input_widget_2 = input_widget_2
        self.input_widget_3 = input_widget_3
        self.input_widget_4 = input_widget_4
        self.input_widget_5 = input_widget_5
        self.input_widget_6 = input_widget_6

        self.app.callback(
            Output(component_id="graph_vis_page1_b1_year_data", component_property='data'),
            [Input(component_id=self.input_widget_2, component_property='value'),
             Input(component_id=self.input_widget_3, component_property='value'),
             Input(component_id=self.input_widget_4, component_property='value'),
             Input(component_id=self.input_widget_5, component_property='value'),
             Input(component_id=self.input_widget_6, component_property='value'),],
        )(self.update_dataframe_1)

        self.app.callback(
            Output(component_id="graph_vis_page1_b2_quarter_month_data_2", component_property='data'),
            Input(component_id=self.input_widget_1, component_property='value')
        )(self.update_dataframe_2)

        self.app.callback(
            Output(component_id="graph_vis_page1_b2_quarter_month_data_1", component_property='data'),
            [Input(component_id=self.input_widget_1, component_property='value'),
             Input(component_id=self.input_widget_4, component_property='value'),
             Input(component_id=self.input_widget_5, component_property='value'),
             Input(component_id=self.input_widget_6, component_property='value'),],
        )(self.update_dataframe_3)

        self.app.callback(
            Output(component_id="graph_vis_page1_filter_data", component_property='data'),
            [Input(component_id=self.input_widget_1, component_property='value'),
             Input(component_id=self.input_widget_2, component_property='value'),
             Input(component_id=self.input_widget_3, component_property='value'),
             Input(component_id=self.input_widget_4, component_property='value'),
             Input(component_id=self.input_widget_5, component_property='value'),
             Input(component_id=self.input_widget_6, component_property='value'),],
        )(self.update_dataframe_4)

    def update_dataframe_1(self, input_value_1, input_value_2, input_value_3, input_value_4, input_value_5):
        temp = self.df_full[(
            (self.df_full['entry_quarter'].isin(input_value_1)) &
            (self.df_full['entry_month'].isin(input_value_2)) &
            (self.df_full['gender'].isin(input_value_3)) &
            (self.df_full['age_group'].isin(input_value_4)) &
            (self.df_full['know_method'].isin(input_value_5))
            )]
        return temp.to_json(date_format='iso', orient='split')

    def update_dataframe_2(self, input_value_1):
        temp = self.df_full[
            self.df_full['entry_year'].isin(input_value_1)
            ]
        return temp.to_json(date_format='iso', orient='split')

    def update_dataframe_3(self, input_value_1, input_value_2, input_value_3, input_value_4):
        temp = self.df_full[(
            (self.df_full['entry_year'].isin(input_value_1)) &
            (self.df_full['gender'].isin(input_value_2)) &
            (self.df_full['age_group'].isin(input_value_3)) &
            (self.df_full['know_method'].isin(input_value_4))
            )]
        return temp.to_json(date_format='iso', orient='split')

    def update_dataframe_4(self, input_value_1, input_value_2, input_value_3, input_value_4, input_value_5, input_value_6):
        temp = self.df_full[(
            (self.df_full['entry_year'].isin(input_value_1)) &
            (self.df_full['entry_quarter'].isin(input_value_2)) &
            (self.df_full['entry_month'].isin(input_value_3)) &
            (self.df_full['gender'].isin(input_value_4)) &
            (self.df_full['age_group'].isin(input_value_5)) &
            (self.df_full['know_method'].isin(input_value_6))
            )]
        return temp.to_json(date_format='iso', orient='split')
    

class Page_2_Interactive_DataFrame:
    def __init__(self, app, d1_class):

        self.dat = d1_class

        self.app = app

        self.app.callback(
            Output(component_id = "graph_vis_page2_by_cat_data", component_property="data"),
            [Input(component_id = "class_year", component_property="value"),
             Input(component_id = "class_month", component_property="value")]
        )(self.update_by_cat_data)

        self.app.callback(
            Output(component_id = "graph_vis_page2_time_data", component_property="data"),
            [Input(component_id = "class_category", component_property="value"),
             Input(component_id = "page_2_radios", component_property="value"),
             Input(component_id = "class_radio_year", component_property="value")]
        )(self.update_regular_data)

    def update_by_cat_data(self, year_inputs, month_inputs):
        df = self.dat[
            (self.dat['end_year'].isin(year_inputs)) & 
            (self.dat['end_month'].isin(month_inputs))
            ]
        return df.to_json(date_format='iso', orient='split')

    def update_regular_data(self, cat_inputs, mode_inputs, year_input):
        df = self.dat[self.dat['class_category'].isin(cat_inputs)]
        if mode_inputs != 1:
            df = df[df['end_year'].isin(year_input)]
        return df.to_json(date_format='iso', orient='split')
    

class Page_3_Interactive_DataFrame:
    def __init__(self, app, d0_user, d2_phys):
        
        self.df0 = d0_user
        self.df_base = d2_phys

        self.app = app
        
        self.app.callback(
            Output(component_id="page_3_interactive_data", component_property="data"),
            [Input(component_id="first-clinic-year-selector", component_property="value"),
             Input(component_id="final-clinic-year-selector", component_property="value"),
             Input(component_id="sport_injury_id", component_property="value"),
             Input(component_id="pain_pos_id", component_property="value"),]
        )(self.computed_dataframe)

    def computed_dataframe(self, input_first_date, input_final_date, input_sports_injury, input_pain_pos):
        df = self.df_base[
            (self.df_base['first_clinic_year'] >= input_first_date) &
            (self.df_base['final_clinic_year'] <= input_final_date)
            ]
        df['sports_injury'][pd.isnull(df['sports_injury'])] = 99
        df = df[df['sports_injury'].isin(input_sports_injury)]
        dfl = []
        for v in input_pain_pos:
            dfl.append(df[df[v] == 1])
        dfl = pd.concat(dfl, axis=0).drop_duplicates().reset_index(drop=True)
        return dfl.to_json(date_format='iso', orient='split')
    

class Page_4_Interactive_DataFrame:
    def __init__(self, app, d0_user, d2_phys):
        self.d0 = d0_user
        self.d2 = d2_phys
        self.app = app

        self.app.callback(
            Output(component_id="page_4_interactive_data", component_property="data"),
            [Input(component_id="date-picker", component_property="value"),]
        )(self.filtered_dataframe)
    
    def filtered_dataframe(self, input_dates):
        dat = self.d2[['user_id','referral_release_date']].merge(self.d0[['user_id','referral_district']], how="left", on="user_id")
        if input_dates != None:
            dat = dat[dat['referral_release_date'] >= input_dates[0]]
            dat = dat[dat['referral_release_date'] <= input_dates[1]]
        return dat.to_json(date_format='iso', orient='split')


class callback_collapse_expand:
    def __init__(self, app, output_widget_id, input_button_id):
        self.app = app
        self.output_widget_id = output_widget_id
        self.input_button_id = input_button_id
        
        self.app.callback(
            Output(self.output_widget_id, "is_open"),
            Input(self.input_button_id, "n_clicks"),
            State(self.output_widget_id, "is_open")
        )(self.enable_collapse)
    
    def enable_collapse(self, button_click, is_open):
        if button_click:
            return not is_open
        return is_open
    

class callback_dispaly_hide:
    def __init__(self, app, output_widget_id, input_controller_id):
        self.app = app
        self.output_widget_id = output_widget_id
        self.input_controller_id = input_controller_id
        
        self.app.callback(
            Output(component_id=self.output_widget_id, component_property='style'),
            Input(component_id=self.input_controller_id, component_property='value')
        )(self.dispaly_hide_page_2)
        
    def dispaly_hide_page_2(self, display_mode):
        if display_mode == 2 or display_mode == 3:
            return {'display': 'inline'}
        elif display_mode == 1:
            return {'display': 'none'}
        

class callback_dropdown_select_and_clear:
    def __init__(self, app, output_menu_id, input_nclick_id_all, input_nclick_id_none):
        self.app = app
        self.output_menu_id = output_menu_id
        self.input_nclick_id_all = input_nclick_id_all
        self.input_nclick_id_none = input_nclick_id_none
        
        self.app.callback(
            Output(component_id=self.output_menu_id, component_property="value"),
            [Input(component_id=self.input_nclick_id_all, component_property="n_clicks"),
             Input(component_id=self.input_nclick_id_none, component_property="n_clicks")],
            State(component_id=self.output_menu_id, component_property="options"),
            prevent_initial_call=True
        )(self.update_state)
        
    def update_state(self, button_click_1, button_click_2, options):
        triggered_id = dash.ctx.triggered_id
        if triggered_id == self.input_nclick_id_all:
            all_or_none_value = [v['value'] for v in options]
        elif triggered_id == self.input_nclick_id_none:
            all_or_none_value = []
        return all_or_none_value
    

class callback_update_secondary_options:
    def __init__(self, app, output_widget_id, input_controller_id, input_option_value_dict):
        self.app = app
        self.output_widget_id = output_widget_id
        self.input_controller_id = input_controller_id
        self.input_option_value_dict = input_option_value_dict
        
        self.app.callback(
            Output(component_id=self.output_widget_id, component_property="options"),
            Input(component_id=self.input_controller_id, component_property="value")
        )(self.update_collapse_choose_secondary_options)

    def update_collapse_choose_secondary_options(self, input_value):
        return self.input_option_value_dict[input_value]
    

class callback_update_clinic_year_range:
    def __init__(self, app, output_date_widget_id, input_date_widget_id, output_date_options):
        self.app = app
        self.output_date_widget_id = output_date_widget_id
        self.input_date_widget_id = input_date_widget_id
        self.output_date_options = output_date_options

        self.app.callback(
            Output(component_id = self.output_date_widget_id, component_property="options"),
            Input(component_id = self.input_date_widget_id, component_property="value")
        )(self.update_clinic_year_range)

    def update_clinic_year_range(self, first_value):
        return [{"label":x, "value":x} for x in self.output_date_options if x >= first_value]


