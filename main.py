import dash
import pandas as pd
import numpy as np
import json
from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import plotly.express as px
from dash.dependencies import Input, Output

from callback_functions import *
from compute_functions import *
from graph_functions import *
from layout import *


#### initialize app
app = dash.Dash(external_stylesheets=[dbc.themes.JOURNAL, dbc.icons.FONT_AWESOME])
server = app.server
app.config.suppress_callback_exceptions = True


#### callbacks
callback_dropdown_select_and_clear(app, "customer_entry_year", "all-select-1", "none-select-1")
callback_dropdown_select_and_clear(app, "customer_entry_quarter", "all-select-2", "none-select-2")
callback_dropdown_select_and_clear(app, "customer_entry_month", "all-select-3", "none-select-3")
callback_dropdown_select_and_clear(app, "customer_gender", "all-select-4", "none-select-4")
callback_dropdown_select_and_clear(app, "customer_age", "all-select-5", "none-select-5")
callback_dropdown_select_and_clear(app, "customer_know_method", "all-select-6", "none-select-6")
callback_dropdown_select_and_clear(app, "class_year", "all-select-7", "none-select-7")
callback_dropdown_select_and_clear(app, "clas_month", "all-select-8", "none-select-8")
callback_dropdown_select_and_clear(app, "class_category", "all-select-9", "none-select-9")
callback_dropdown_select_and_clear(app, "class_radio_year", "all-select-10", "none-select-10")

callback_collapse_expand(app, "collapse-page2-sess","collapse-button-page2-sess")
callback_collapse_expand(app, "collapse-page2-reg","collapse-button-page2-reg")
callback_collapse_expand(app, "collapse-page2-attd","collapse-button-page2-attd")
callback_collapse_expand(app, "collapse-page2-hour","collapse-button-page2-hour")
callback_collapse_expand(app, "collapse","collapse-button-1")

callback_dispaly_hide(app, 'dropdownmenu_hide', 'page_2_radios')
callback_dispaly_hide(app, 'collapse-button-page2-attd', 'page_2_radios')
callback_dispaly_hide(app, 'collapse-button-page2-hour', 'page_2_radios')

callback_update_secondary_options(app, "collapse_choose_mode_b_options", "collapse_choose_vis_mode",
                                    {
                                        "Overall Trend across time (selected criteria)": [""], 
                                        "Comparison between groups (selected period)": [
                                            "Grouping Variable: Gender", 
                                            "Grouping Variable: Age", 
                                            "Grouping Variable: Accesibility Levels", 
                                            "Grouping Variable: Hospitalization",
                                            "Grouping Variable: Residential Care",
                                            "Grouping Variable: Referral methods"
                                            ]
                                    }
                                )

callback_update_clinic_year_range(app, "final-clinic-year-selector", "first-clinic-year-selector", final_clinic_date_options) 


#### Page 1 objects

reactive_page_1 = Page_1_Interactive_DataFrame(
    app = app,
    d0_user = d0_user, 
    input_widget_1 = "customer_entry_year", 
    input_widget_2 = "customer_entry_quarter", 
    input_widget_3 = "customer_entry_month", 
    input_widget_4 = "customer_gender", 
    input_widget_5 = "customer_age", 
    input_widget_6 = "customer_know_method"
)

compute_page_1 = Page_1_Compute(d0_user, d1_class, d1_class_reg)
entry2class_lead_time_df = compute_page_1.entry2class_lead_time(compute_page_1.df_user, "user_id")['raw_data']
lifetime_registration_df = compute_page_1.lifetime_joined_sessions(compute_page_1.df_user, "user_id")['raw_data']

graph_vis_page1_b1_year = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_b1_year",
    output_fig_data_id = ["graph_vis_page1_b1_year_data", "graph_vis_page1_b1_year_data"],
    dx = "entry_year", 
    dy = "new_admitted_users", 
    dcolor = 'lightsalmon', 
    xaxis_title = "Entry Year", yaxis_title = "Count", title="Number of New Users By Year"
)

graph_vis_page1_b2_quarter = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_b2_quarter_month",
    output_fig_data_id = ["graph_vis_page1_b2_quarter_month_data_1", "graph_vis_page1_b2_quarter_month_data_2"],
    standalone_switch_id = "standalone-switch-quarter",
    dx = "entry_quarter", 
    dy = "new_admitted_users", 
    dcolor = 'lightsalmon', 
    xaxis_title = "Entry Quarter within the selected Year(s)", yaxis_title = "Count", title="Number of New Users By Quarter"
)

graph_vis_page1_b3_month = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_b3_month",
    output_fig_data_id = ["graph_vis_page1_b2_quarter_month_data_1", "graph_vis_page1_b2_quarter_month_data_2"],
    standalone_switch_id = "standalone-switch-month",
    dx = "entry_month", 
    dy = "new_admitted_users", 
    dcolor = 'lightsalmon', 
    xaxis_title = "Entry Month within the selected Year(s)", yaxis_title = "Count", title="Number of New Users By Month"
)

graph_gauge_1 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_guage_1",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dy = "accessibility_5km_60min",
    alert_level_1 = 50,
    alert_level_2 = 55,
    gauge_threshold = 65,
    gauge_upper_limit = 100,
    gauge_text = "Able to Meet Low Accessibility Level %",
    chart_type = "indicator"
)

graph_gauge_2 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_guage_2",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dy = "accessibility_3km_30min",
    alert_level_1 = 30,
    alert_level_2 = 35,
    gauge_threshold = 45,
    gauge_upper_limit = 60,
    gauge_text = "Able to Meet Moderate Accessibility Level %",
    chart_type = "indicator"
)

graph_gauge_3 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_guage_3",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dy = "accessibility_1km_10min",
    alert_level_1 = 2,
    alert_level_2 = 4,
    gauge_threshold = 5,
    gauge_upper_limit = 10,
    gauge_text = "Able to Meet High Accessibility Level %",
    chart_type = "indicator"
)

graph_vis_page1_pie1 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_pie1",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dx = "gender",
    dy = "new_admitted_users",
    dcolor = px.colors.qualitative.Pastel,
    subtitle = "Gender",
    chart_type = "pie"
)
graph_vis_page1_pie2 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_pie2",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dx = "age_group",
    dy = "new_admitted_users",
    dcolor = px.colors.qualitative.Pastel,
    subtitle = "Age Group",
    chart_type = "pie",
    pie_sorting_list = age_options
)

graph_vis_page1_pie3 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_pie3",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dx = "hospital_residential_care",
    dy = "new_admitted_users",
    dcolor = px.colors.qualitative.Pastel,
    subtitle = "Source",
    chart_type = "pie",
    pie_regroup = True,
    pie_regroup_threshold = 50,
)

graph_vis_page1_pie4 = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_pie4",
    output_fig_data_id = "graph_vis_page1_filter_data",
    dx = "know_method",
    dy = "new_admitted_users",
    dcolor = px.colors.qualitative.Pastel,
    subtitle = "Source",
    chart_type = "pie",
    pie_regroup = True,
    pie_regroup_threshold = 50,
)

graph_vis_page1_dist1_fixed = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_dist1_fixed",
    output_fig_data_id = "graph_vis_page1_filter_data",
    supp_info_df = entry2class_lead_time_df,
    supp_info_col =  "lead_time",
    dx = "lead_time",
    dcolor = px.colors.qualitative.Vivid, 
    bins = 200,
    chart_type = "histogram",
    xaxis_title = "Lead Time between Entry and First Class",
    yaxis_title = "Count"
)
graph_vis_page1_dist1_subgrp = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_dist1_subgrp",
    output_fig_data_id = "graph_vis_page1_filter_data",
    output_legend_id = "distplot_1_radios",
    supp_info_df = entry2class_lead_time_df,
    supp_info_col = "lead_time",
    dx = "lead_time",
    dcolor = px.colors.qualitative.Vivid,
    bins = 200,
    chart_type = "histogram",
    xaxis_title = "Lead Time between Entry and First Class",
    yaxis_title = "Count",
)

graph_vis_page1_dist2_fixed = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_dist2_fixed",
    output_fig_data_id = "graph_vis_page1_filter_data",
    supp_info_df = lifetime_registration_df,
    supp_info_col = "log_joined_sessions",
    dx = "log_joined_sessions",
    dcolor = px.colors.qualitative.Vivid, 
    bins = 30,
    chart_type = "histogram",
    xaxis_title = "Log Number of All-Time Registered Sessions",
    yaxis_title = "Count"
)
graph_vis_page1_dist2_subgrp = Page_1_Visualize(
    app = app,
    output_fig_id = "graph_vis_page1_dist2_subgrp",
    output_fig_data_id = "graph_vis_page1_filter_data",
    output_legend_id = "distplot_2_radios",
    supp_info_df = lifetime_registration_df,
    supp_info_col = "log_joined_sessions",
    dx = "log_joined_sessions",
    dcolor = px.colors.qualitative.Vivid,
    bins = 30,
    chart_type = "histogram",
    xaxis_title = "Log Number of All-Time Registered Sessions",
    yaxis_title = "Count",
)


#### Page 2 objects

reactive_page_2 = Page_2_Interactive_DataFrame(app, d1_class)

two_variable_calculation = Page_2_Compute.two_variable_calculation
differentiate_single_double_var = Page_2_Compute.differentiate_single_double_var

graph_vis_page2_sess_by_cat = Page_2_Visualize(
    app = app,
    output_fig_id="graph_vis_page2_sess_by_cat",
    output_fig_data_id="graph_vis_page2_by_cat_data",
    dx = "class_category",
    dy = "num_session",
    dcolor = px.colors.qualitative.Pastel,
    subtitle = "Sessions",
    chart_type = "pie",
    pie_regroup = True,
    pie_regroup_threshold = 50,
)
graph_vis_page2_reg_by_cat = Page_2_Visualize(
    app = app,
    output_fig_id="graph_vis_page2_reg_by_cat",
    output_fig_data_id="graph_vis_page2_by_cat_data",
    dx = "class_category",
    dy = "num_registry",
    dcolor = px.colors.qualitative.Pastel,
    subtitle = "Registrants",
    chart_type = "pie",
    pie_regroup = True,
    pie_regroup_threshold = 50,
)

graph_vis_page2_reg = Page_2_Visualize(
    app = app,
    output_fig_id="graph_vis_page2_reg",
    output_fig_data_id="graph_vis_page2_time_data",
    collapse_dropdown_id="collapse-dropdown-page2-reg",
    aggregate_cols_0 = "num_registry",
    aggregate_cols_1 = "num_booking",
    aggregate_fns_0 = np.sum,
    aggregate_fns_1 = np.sum,
    line_color = "lightsalmon",
    title = "Total Number of Registration",
    title_second = "Total Number of Appointed / Reserved Places in all Sessions",
    yaxis_title = "Counts",
    yaxis_title_second = "Counts",
    chart_type = "line",
    year_options = year_options_2
)

graph_vis_page2_sess = Page_2_Visualize(
    app = app,
    output_fig_id="graph_vis_page2_sess",
    output_fig_data_id="graph_vis_page2_time_data",
    collapse_dropdown_id="collapse-dropdown-page2-sess",
    aggregate_cols_0 = "num_session",
    aggregate_cols_1 = "class_id",
    aggregate_fns_0 = np.sum,
    aggregate_fns_1 = pd.Series.nunique,
    line_color = "lightsalmon",
    title = "Number of Sessions",
    title_second = "Number of Classes",
    yaxis_title = "Counts",
    yaxis_title_second = "Counts",
    chart_type = "line",
    year_options = year_options_2
)

graph_vis_page2_attd_rate = Page_2_Visualize(
    app = app,
    output_fig_id="graph_vis_page2_attd_rate",
    output_fig_data_id="graph_vis_page2_time_data",
    collapse_dropdown_id="collapse-dropdown-page2-attd",
    bar_color = "lightsalmon",
    line_color = "brown",
    title = "Number of Attendance / Attendance Rate",
    yaxis_title = "Counts",
    yaxis_title_second = "Rate (%)",
    aggregate_cols_0 = "num_attend",
    aggregate_cols_1 = ["num_attend","num_booking"],
    aggregate_fns_0 = np.sum,
    aggregate_fns_1 = [np.sum, np.sum],
    two_var_operations = "division",
    two_var_operations_logic = "a / b",
    two_var_col_name = "attendance_rate",
    chart_type = "combo",
    year_options = year_options_2
)

graph_vis_page2_hour_per_user = Page_2_Visualize(
    app = app,
    output_fig_id="graph_vis_page2_hour_per_user",
    output_fig_data_id="graph_vis_page2_time_data",
    collapse_dropdown_id="collapse-dropdown-page2-hour",
    bar_color = "lightsalmon",
    line_color = "brown",
    title = "Total Hours / Completion Rate of Sessional Attendance Hours",
    yaxis_title = "Total Hours",
    yaxis_title_second = "Rate (%)",
    aggregate_cols_0 = "total_hours",
    aggregate_cols_1 = ["completed_attendance_hours","scheduled_attendance_hours"],
    aggregate_fns_0 = np.sum,
    aggregate_fns_1 = [np.sum, np.sum],
    two_var_operations = "division",
    two_var_operations_logic = "a / b",
    two_var_col_name = "hours_completion_rate",
    chart_type = "combo",
    year_options = year_options_2
)


#### Page 3 objects

compute_page_3 = Page_3_Interactive_DataFrame(app, d0_user, d2_phys)

compute_lt = Page_3_Compute.compute_lt

graphics_page_3 = Page_3_Visualize(
    app = app,
    bins = 500,
    sunburst_threshold = pain_pos_inclusion_value,
    chord_attribute_df = d0_user[['user_id','initial_service_plan','assigned_service_plan']],
    discrete_colors = px.colors.qualitative.Antique,
    gradient_colors = "YlOrBr",
    sankey_title = "Sankey Diagram for Treatment Assignment " + "<br>" + \
                    "(Initially proposed -> " + \
                      "First intake arranged -> " + \
                       "Finally assigned)",
    heat_x_title = "Initial Service Plan when applied",
    heat_y_title = "Finally assigned Service Plan after assessment",
    bar_color = "LightSalmon",
    bar_title = "Distribution of Physiotherapy Treatments / Consultations before Discharge",
    bar_xaxis_title = "Number of Physiotherapy Treatments / Consultations",
    bar_yaxis_title = "Counts",
    sunburst_title = "Pain Position Distribution",
    distplot_title = "Referral-to-First, First-to-Final and Hydro Therapy Lead Times Distribution"
    )

page_3_user_demog = lifetime_registration_df[['user_id','age','gender','log_joined_sessions']]
page_3_user_demog = page_3_user_demog[(~pd.isnull(page_3_user_demog['log_joined_sessions'])) & (page_3_user_demog['log_joined_sessions'] != -np.inf)]

graphics_page_3_scatter_1 = Page_3_Visualize(
    app = app,
    chart_type="scatter",
    output_fig_id="scatter_lead_time",
    output_fig_data_id="page_3_interactive_data",
    user_demog_df = page_3_user_demog,
    sc_xcol = "age",
    sc_ycol = "first2final_lead_time",
    sc_color_col = "gender",
    sc_size_col = "log_joined_sessions",
    sc_title="Age vs First-to-Final Therapy Lead Times; "+ "<br>" + "detailed by Gender & Log Number of Joined Sessions",
    xaxis_title="Age",
    yaxis_title="First-Final Clinic Lead Time",
)
graphics_page_3_scatter_2 = Page_3_Visualize(
    app = app,
    chart_type="scatter",
    output_fig_id="scatter_hydro_lead_time",
    output_fig_data_id="page_3_interactive_data",
    user_demog_df = page_3_user_demog,
    sc_xcol = "age",
    sc_ycol = "hydro_lead_time",
    sc_color_col = "gender",
    sc_size_col = "log_joined_sessions",
    sc_title="Age vs HydroTherapy Lead Times; "+ "<br>" + "detailed by Gender & Log Number of Joined Sessions",
    xaxis_title="Age",
    yaxis_title="HydroTherapy Lead Time",
)


#### Page 4 objects
compute_page_4 = Page_4_Interactive_DataFrame(app, d0_user, d2_phys)

with open('./assets/Hong_Kong_18_Districts.geojson', 'r', encoding='utf-8') as response:
    district_map = json.load(response)

district_map['features'] = [x for x in district_map['features'] if x['properties']['ENAME'] != "ISLANDS"]
districts = [x['properties']['ENAME'] for x in district_map['features']]
districts = [''.join([y[0] for y in x.split(" ")]) if len(x.split(" ")) > 1 else x.lower().capitalize() for x in districts]
districts[districts.index("KT")] = "KT-J"
districts[districts.index("KT")] = "KT-S"

n = 0
for f in district_map['features']:
    f['properties']['ID'] = districts[n]
    n += 1

graphics_page_4 = Page_4_Visualize(
    app = app,
    geojson_data = district_map,
    global_region_list = districts,
)


#### Set up URLs

CONTENT_STYLE = {
    "transition": "margin-left .5s",
    "margin-left": "25rem",
    "margin-right": "2rem",
    "padding": "2rem 1rem",
    "background-color": "#f8f9fa",
}

page_content = html.Div(id="page-content", style=CONTENT_STYLE)

app.layout = html.Div([dcc.Location(id="url"), page_select_pane, page_content])

@app.callback(
    Output("page-content", "children"), 
    [Input("url", "pathname")]
)
def render_page_content(pathname):
    if pathname == "/":
        return page_main_layout
    elif pathname == "/page-customer":
        return page_customer_layout
    elif pathname == "/page-class":
        return page_class_layout
    elif pathname == "/page-physio":
        return page_physio_layout
    elif pathname == "/page-refer-service-map":
        return page_poi_layout
    # If the user tries to reach a different page, return a 404 message
    return html.Div(
        [
            html.H1("404: Not found", className="text-danger"),
            html.Hr(),
            html.P(f"The pathname {pathname} was not recognised..."),
        ],
        className="p-3 bg-light rounded-3",
    )


#### Run and Port
if __name__ == "__main__":
    app.run_server(debug=True, port = 3004)

