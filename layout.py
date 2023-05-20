from dash import dcc
from dash import html
import dash_bootstrap_components as dbc
import dash_mantine_components as dmc

from main_init_object import *


page_select_style = {
    "position": "fixed",
    "top": 0,
    "left": 0,
    "bottom": 0,
    "width": "24rem",
    "padding": "2rem 1rem",
    "background-color": "#34373A",
}
page_select_pane = html.Div([
    html.Img(src="assets/banner.jpg", style={'height':'160px', 'width':'320px'}),
    html.Br(),
    html.Br(),
    dbc.Nav([
        dbc.NavLink(
            html.Div([
                html.I(className="fas fa-house"),
                html.Label("  Home: Key Figures", style={"fontSize": 16, "font-weight": "bold", 'padding-left': '10px'})
                ]), 
            href="/", active="exact"
        ),
        dbc.NavLink(
            html.Div([
                html.I(className="fas fa-clipboard"),
                html.I(className="fas fa-users", style={'padding-left': '2px'}),
                html.Label("  1:   Customer Demographics", style={"fontSize": 16, "font-weight": "bold", 'padding-left': '10px'})
                ]), 
            href="/page-customer", active="exact",
        ),
        dbc.NavLink(
            html.Div([
                html.I(className="fas fa-clipboard"),
                html.I(className="fas fa-chalkboard-user", style={'padding-left': '2px'}),
                html.Label("  2:   Class Statistics", style={"fontSize": 16, "font-weight": "bold", 'padding-left': '10px'})
                ]), 
            href="/page-class", active="exact",
        ),
        dbc.NavLink(
            html.Div([
                html.I(className="fas fa-clipboard"),
                html.I(className="fas fa-stethoscope", style={'padding-left': '2px'}),
                html.Label("  3:   Physiotherapy Statistics", style={"fontSize": 16, "font-weight": "bold", 'padding-left': '10px'})
                ]), 
            href="/page-physio", active="exact",
        ),
        dbc.NavLink(
            html.Div([
                html.I(className="fas fa-clipboard"),
                html.I(className="fas fa-globe", style={'padding-left': '2px'}),
                html.Label("  4:   Referral Service Points (Map)", style={"fontSize": 16, "font-weight": "bold", 'padding-left': '10px'})
                ]), 
            href="/page-refer-service-map", active="exact",
        ),
    ], vertical=True, pills=True),
], style=page_select_style)


page_main_layout = html.Div([
    dbc.Row([
        html.H1("Health and Wellness Operations BI Dashboard", style={'fontSize': 36, "font-weight": "bold"}),
        html.Hr(),
    ]),
    dbc.Row([
        #### Tile a ####
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("New Users at Current Year (Change)", 
                                       style={'background':'SlateGrey',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_a1),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
                        dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("New User Completed Registration Rate (%) at Current Year (Change)", 
                                       style={'background':'SlateGrey',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_a2),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Tabs(id="tabs-main", children=[
                        dbc.Tab(
                            dbc.Card([
                                dbc.CardBody(
                                    dcc.Graph(figure=graph_vis_main_a2_year, id="out_main_a2_year")
                                ),
                            ], style={
                                    "width": "100%",
                                    "border-radius": "1%",
                                    "background": "AliceBlue",
                                }
                            ),
                        label="By Year",
                        active_label_style={"color": "orange", "font-weight": "bold"}
                        ),
                        dbc.Tab(
                            dbc.Card([
                                dbc.CardBody(
                                    dcc.Graph(figure=graph_vis_main_a2_quarter, id="out_main_a2_quarter")
                                ),
                            ], style={
                                    "width": "100%",
                                    "border-radius": "1%",
                                    "background": "AliceBlue",
                                }
                            ),
                        label="By Quarter",
                        active_label_style={"color": "orange", "font-weight": "bold"}
                        ),
                        dbc.Tab(
                            dbc.Card([
                                dbc.CardBody(
                                    dcc.Graph(figure=graph_vis_main_a2_month, id="out_main_a2_month")
                                ),
                            ], style={
                                    "width": "100%",
                                    "border-radius": "1%",
                                    "background": "AliceBlue",
                                }
                            ),
                        label="By Month",
                        active_label_style={"color": "orange", "font-weight": "bold"}
                        ),
                   ])
                ], width = 12),
            ]),
        ], width = 6),
        #### Tile b ####
        dbc.Col([
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Classes at Current Year (Change)", 
                                       style={'background':'DarkOliveGreen',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_b1),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Sessions at Current Year (Change)", 
                                       style={'background':'DarkOliveGreen',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_b2),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Class Hours at Current Year (Change)", 
                                       style={'background':'DarkOliveGreen',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_b3),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Class Attendance at Current Year (Change)", 
                                       style={'background':'DarkOliveGreen',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_b4),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
            ]),
            html.Br(),
            html.Br(),
            #### Tile c ####
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Clinic Intake at Current Year (Change)", 
                                       style={'background':'SaddleBrown',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_c1),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Clinic Intake with Pre-assessment at Current Year (Change)", 
                                       style={'background':'SaddleBrown',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_c2),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
            ]),
            html.Br(),
            html.Br(),
            dbc.Row([
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Clinic Direct Discharge at Current Year (Change)", 
                                       style={'background':'SaddleBrown',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_c3),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
                dbc.Col([
                    dbc.Card([
                        dbc.CardHeader("Total Clinic Discharge to Doctor Follow-up at Current Year (Change)", 
                                       style={'background':'SaddleBrown',"color":"Snow", "font-weight": "bold"}), 
                        dbc.CardBody(card_vis_main_c4),
                    ], style={
                            "width": "100%",
                            "border-radius": "1%",
                            "background": "AliceBlue",
                        }
                    ),
                ], width = 6),
            ]),
        ], width = 6),
    ]),
])


page_customer_layout = html.Div([
    dbc.Row([
        html.H1("Health and Wellness Operations BI Dashboard", style={'fontSize': 36, "font-weight": "bold"}),
        html.Hr(),
    ]),
    dbc.Row([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='customer_entry_year',
                            options = [{"label":x, "value":x} for x in year_options_1],
                            value = year_options_1,
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-1", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-1", color="info", n_clicks=0)]
                        ),
                    ], label="Customer Entry Year: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='customer_entry_quarter',
                            options = [{"label":x, "value":x} for x in quarter_options_1],
                            value = quarter_options_1,
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-2", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-2", color="info", n_clicks=0)]
                        ),
                    ], label="Customer Entry Quarter: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='customer_entry_month',
                            options = [{"label":x+1, "value":x+1} for x in range(12)],
                            value = [x+1 for x in range(12)],
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-3", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-3", color="info", n_clicks=0)]
                        ),
                    ], label="Customer Entry Month: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='customer_gender',
                            options = [{"label":x, "value":x} for x in gender_options],
                            value = gender_options,
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-4", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-4", color="info", n_clicks=0)]
                        ),
                    ], label="Gender: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='customer_age',
                            options = [{"label":x, "value":x} for x in age_options],
                            value = age_options,
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-5", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-5", color="info", n_clicks=0)]
                        ),
                    ], label="Age Group: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='customer_know_method',
                            options = [{"label":x, "value":x} for x in know_method_options],
                            value = know_method_options,
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-6", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-6", color="info", n_clicks=0)]
                        ),
                    ], label="Know Methods: ", toggle_style={"width":"100%"})
                ], width = 2),
            ]),
        ], style = {"width":"100%"}),
    ]),
    html.Br(),
    html.Br(),
    ######### Year, Quarter, Month line charts
    dbc.Row([
        dbc.Col([
            html.Div([
                dbc.Button(
                    "Expand to choose visualization mode: ",
                    id="collapse-button-1",
                    className="mb-3",
                    color="secondary",
                    n_clicks=0,
                    
                ),
                dbc.Collapse(
                    dbc.Card(dbc.CardBody(
                        html.Div([
                            dbc.Row([
                                dbc.Col([
                                    dcc.Dropdown(id='collapse_choose_vis_mode',
                                        options = ["Overall Trend across time (selected criteria)", 
                                                   "Comparison between groups (selected period)"],
                                        multi = False,
                                        clearable = False,
                                        value = "Overall Trend across time (selected criteria)"
                                    ),
                                ], width = 4),
                                dbc.Col([
                                    dcc.Dropdown(id='collapse_choose_mode_b_options'),
                                ], width = 4),
                            ])
                        ])
                    )),
                    id="collapse",
                    is_open=False,
                ),
            ]),
            html.Div([
                dcc.Store(id="graph_vis_page1_b1_year_data"),
                dcc.Store(id="graph_vis_page1_b2_quarter_month_data_1"),
                dcc.Store(id="graph_vis_page1_b2_quarter_month_data_2"),
            ]),
            dbc.Tabs(id="tabs-page-1", children=[
                dbc.Tab(
                    dbc.Card([
                        html.Div([
                            dbc.Switch(
                                id="dummy-switch",
                                value=False
                            ),
                        ], style={"display":"none"}),
                        dbc.CardBody(
                            dcc.Graph(id="graph_vis_page1_b1_year")
                        ),
                    ], style={"width": "100%",
                              "border-radius": "1%",
                              "background": "BlanchedAlmond",}
                    ),
                label="By Year",
                active_label_style={"color": "orange", "fontSize": 16, "font-weight": "bold"}
                ),
                dbc.Tab(
                    dbc.Card([
                        html.Div([
                            dbc.Switch(
                                id="standalone-switch-quarter",
                                label = "Show All Years' Breakdown Data ",
                                value=False,
                                label_style={"color": "Maroon", "fontSize": 16, "font-weight": "bold"},
                            ),
                        ], style={"marginLeft": "85%", "marginTop": "10px", "marginRight": "5px"}),
                        dbc.CardBody(
                            dcc.Graph(id="graph_vis_page1_b2_quarter_month")
                        ),
                    ], style={"width": "100%",
                              "border-radius": "1%",
                              "background": "BlanchedAlmond",}
                    ),
                label="By Quarter",
                active_label_style={"color": "orange", "fontSize": 16, "font-weight": "bold"}
                ),
                dbc.Tab(
                    dbc.Card([
                        html.Div([
                            dbc.Switch(
                                id="standalone-switch-month",
                                label = "Show All Years' Breakdown Data ",
                                value=False,
                                label_style={"color": "Maroon", "fontSize": 16, "font-weight": "bold"},
                            ),
                        ], style={"marginLeft": "85%", "marginTop": "10px", "marginRight": "5px"}),
                        dbc.CardBody(
                            dcc.Graph(id="graph_vis_page1_b3_month")
                        ),
                    ], style={"width": "100%",
                              "border-radius": "1%",
                              "background": "BlanchedAlmond",}
                    ),
                label="By Month",
                active_label_style={"color": "orange", "fontSize": 16, "font-weight": "bold"}
                ),
            ])
        ], width = 12),
    ]),
    html.Br(),
    html.Br(),
    ######### Store Data to Browser
    html.Div([
        dcc.Store(id="graph_vis_page1_filter_data"),
    ]),
    ######### Gauge Charts
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_guage_1")
        ], width=4),
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_guage_2")
        ], width=4),
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_guage_3")
        ], width=4),
    ]),
    html.Br(),
    html.Br(),
    ######### Pie charts
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_pie1")
        ], width=6),
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_pie2")
        ], width=6),
    ]),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_pie3")
        ], width=6),
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_pie4")
        ], width=6),
    ]),
    html.Br(),
    html.Br(),
    ######### Distribution charts
    dbc.Row([
        html.H4("Select Grouping Variable for the chart on the right: ", style = {'fontSize': 16}),
        html.Div(
            [
                dbc.RadioItems(
                    id="distplot_1_radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Gender", "value": "gender"},
                        {"label": "Age Group", "value": "age_group"},
                        {"label": "Accessibility Levels", "value": "accessibility_levels"},
                        {"label": "Hospitalization", "value": "hospitalization"},
                        {"label": "Residential Care", "value": "residential_care"}
                    ],
                    value="gender",
                ),
                html.Div(id="output"),
            ],
            className="radio-group",
        )
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_dist1_fixed")
        ], width=6),
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_dist1_subgrp")
        ], width=6),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        html.H4("Select Grouping Variable for the chart on the right: ", style = {'fontSize': 16}),
        html.Div(
            [
                dbc.RadioItems(
                    id="distplot_2_radios",
                    className="btn-group",
                    inputClassName="btn-check",
                    labelClassName="btn btn-outline-primary",
                    labelCheckedClassName="active",
                    options=[
                        {"label": "Gender", "value": "gender"},
                        {"label": "Age Group", "value": "age_group"},
                        {"label": "Accessibility Levels", "value": "accessibility_levels"},
                        {"label": "Hospitalization", "value": "hospitalization"},
                        {"label": "Residential Care", "value": "residential_care"}
                    ],
                    value="gender",
                ),
                html.Div(id="output"),
            ],
            className="radio-group",
        )
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_dist2_fixed")
        ], width=6),
        dbc.Col([
            dcc.Graph(id="graph_vis_page1_dist2_subgrp")
        ], width=6),
    ])
])


page_class_layout = html.Div([
    dbc.Row([
        html.H1("Health and Wellness Operations BI Dashboard", style={'fontSize': 36, "font-weight": "bold"}),
        html.Hr(),
    ]),
    dbc.Row([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='class_year',
                            options = [{"label":x, "value":x} for x in year_options_2],
                            value = year_options_2
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-7", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-7", color="info", n_clicks=0)]
                        ),
                    ], label="Class End Year: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='class_month',
                            options = [{"label":x+1, "value":x+1} for x in range(12)],
                            value = [x+1 for x in range(12)]
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-8", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-8", color="info", n_clicks=0)]
                        ),
                    ], label="Class End Month: ", toggle_style={"width":"100%"})
                ], width = 2),
            ])
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dcc.Store(id="graph_vis_page2_by_cat_data"),
        dbc.Col([
            dcc.Graph(id="graph_vis_page2_sess_by_cat")
        ], width = 6),
        dbc.Col([
            dcc.Graph(id="graph_vis_page2_reg_by_cat")
        ], width = 6),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Container([
            dbc.Row([
                dbc.Col([
                    dbc.DropdownMenu(children=[
                        dbc.Checklist(
                            id='class_category',
                            options = [{"label":x, "value":x} for x in sorted(list(set(d1_class['class_category'])))],
                            value = sorted(list(set(d1_class['class_category'])))
                        ),
                        dbc.ButtonGroup(
                            [dbc.Button("Select All",id="all-select-9", color="info", n_clicks=0), 
                             dbc.Button("Unselect All",id="none-select-9", color="info", n_clicks=0)]
                        ),
                    ], label="Class Category: ", toggle_style={"width":"100%"})
                ], width = 2),
                dbc.Col([
                    dbc.RadioItems(
                        id="page_2_radios",
                        className="btn-group",
                        inputClassName="btn-check",
                        labelClassName="btn btn-outline-danger",
                        labelCheckedClassName="active",
                        options=[
                            {"label": "Show Annual Trend(s)", "value":1},
                            {"label": "Show Quarterly Breakdowns per Year", "value":2},
                            {"label": "Show Monthly Breakdowns per Year", "value":3}
                        ],
                        value=1,
                    ),
                ], width = 6),
                dbc.Col([
                    html.Div([
                        dbc.DropdownMenu(children=[
                            dbc.Checklist(
                                id='class_radio_year',
                                options = [{"label":x, "value":x} for x in year_options_2],
                                value = year_options_2
                            ),
                            dbc.ButtonGroup(
                                [dbc.Button("Select All",id="all-select-10", color="info", n_clicks=0), 
                                 dbc.Button("Unselect All",id="none-select-10", color="info", n_clicks=0)]
                            ),
                        ], id = "dropdownmenu_hide", 
                           label="Please select year(s) for Quarter/Month: ", 
                           color="danger", 
                           style={"width": "100%"})
                    ], style= {'display': 'inline'})
                ], width = 4)
            ]),    
        ]),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dcc.Store(id="graph_vis_page2_time_data"),
        dbc.Col([
            dbc.Row([
                html.Div([
                    dbc.Button(
                        "Expand to choose variable: ",
                        id="collapse-button-page2-sess",
                        className="mb-3",
                        color="secondary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dbc.Card(dbc.CardBody(
                            dcc.Dropdown(id='collapse-dropdown-page2-sess',
                                        options = [{"label": "Number of Sessions", "value":0},
                                                   {"label": "Number of Classes", "value":1}],
                                        multi= False,
                                        value = 0
                            ),
                        )),
                        id="collapse-page2-sess",
                        is_open=False,
                    ),
                ]),
            ]),
            dbc.Row([
                dcc.Graph(id="graph_vis_page2_sess")
            ])
        ], width = 6),
        dbc.Col([
            dbc.Row([
                html.Div([
                    dbc.Button(
                        "Expand to choose variable: ",
                        id="collapse-button-page2-reg",
                        className="mb-3",
                        color="secondary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dbc.Card(dbc.CardBody(
                            dcc.Dropdown(id='collapse-dropdown-page2-reg',
                                        options = [{"label": "Number of Registrants", "value":0},
                                                   {"label": "Number of Scheduled Bookings", "value":1}],
                                        multi= False,
                                        value = 0
                            ),
                        )),
                        id="collapse-page2-reg",
                        is_open=False,
                    ),
                ]),
            ]),
            dbc.Row([
                dcc.Graph(id="graph_vis_page2_reg")
            ])
        ], width = 6),
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Row([
                html.Div([
                    dbc.Button(
                        "Expand to choose variable: ",
                        id="collapse-button-page2-attd",
                        className="mb-3",
                        color="secondary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dbc.Card(dbc.CardBody(
                            dcc.Dropdown(id='collapse-dropdown-page2-attd',
                                        options = [{"label": "Number of Attendance", "value":0}, 
                                                   {"label": "Attendance Rate", "value":1}],
                                        multi= False,
                                        value = 0
                            ),
                        )),
                        id="collapse-page2-attd",
                        is_open=False,
                    ),
                ], style= {'display': 'inline'}),
            ]),
            dbc.Row([
                dcc.Graph(id="graph_vis_page2_attd_rate")
            ])
        ], width = 6),
        dbc.Col([
            dbc.Row([
                html.Div([
                    dbc.Button(
                        "Expand to choose variable: ",
                        id="collapse-button-page2-hour",
                        className="mb-3",
                        color="secondary",
                        n_clicks=0,
                    ),
                    dbc.Collapse(
                        dbc.Card(dbc.CardBody(
                            dcc.Dropdown(id='collapse-dropdown-page2-hour',
                                        options = [{"label": "Total Hours", "value":0}, 
                                                   {"label": "Completion Rate of Sessional Attendance Hours", "value":1}],
                                        multi= False,
                                        value = 0
                            ),
                        )),
                        id="collapse-page2-hour",
                        is_open=False,
                    ),
                ], style= {'display': 'inline'}),
            ]),
            dbc.Row([
                dcc.Graph(id="graph_vis_page2_hour_per_user")
            ])
        ], width = 6),
    ])
])


page_physio_layout = html.Div([
    dbc.Row([
        html.H1("Health and Wellness Operations BI Dashboard", style={'fontSize': 36, "font-weight": "bold"}),
        html.Hr(),
    ]),
    html.Div([
        dcc.Store(id="page_3_interactive_data"),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("First Clinic Year: "),
            dbc.Select(
                id='first-clinic-year-selector',
                options = [{"label":x, "value":x} for x in first_clinic_date_options],
                value = [x for x in first_clinic_date_options][0]
            ),
        ], width = 4),
        dbc.Col([
            dbc.Label("Final Clinic Year: "),
            dbc.Select(
                id='final-clinic-year-selector',
                options = [{"label":x, "value":x} for x in final_clinic_date_options],
                value = [x for x in final_clinic_date_options][-1]
            ),
        ], width = 4),
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Sports Injury: "),
            dbc.Checklist(
                options = [{"label":"Yes", "value":1}, 
                           {"label":"No", "value":0},
                           {"label":"Unknown", "value":99}],
                value = [99, 0, 1],
                inline = True,
                id="sport_injury_id",
            ),
        ], width = 4)
    ]),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dbc.Label("Pain Positions: "),
            dbc.Checklist(
                options = [{"label":x, "value":x} for x in pain_pos_options],
                value = [x for x in pain_pos_options],
                inline = True,
                id="pain_pos_id",
            ),
        ], width = 12)
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="sankey_diagram_treatments")
        ], width = 6),
        dbc.Col([
            dcc.Graph(id="chord_diagram_service_plans")
        ], width = 6)
    ]),
    html.Br(),
    html.Br(),
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="bar_total_num_treatments")
        ], width = 6),
        dbc.Col([
            dcc.Graph(id="sunburst_pain_pos")
        ], width = 6),
    ]),
    html.Br(),
    html.Br(),
    ######### Box-and-Whisker charts
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="histogram_treatments_lead_time")
        ], width = 12)
    ]),
    html.Br(),
    html.Br(),
    ######### Scatter charts
    dbc.Row([
        dbc.Col([
            dcc.Graph(id="scatter_lead_time")
        ], width = 6),
        dbc.Col([
            dcc.Graph(id="scatter_hydro_lead_time")
        ], width = 6)
    ]),
])


page_poi_layout = html.Div([
    dbc.Row([
        html.H1("Health and Wellness Operations BI Dashboard", style={'fontSize': 36, "font-weight": "bold"}),
        html.Hr(),
    ]),
    html.Div([
        dcc.Store(id="page_4_interactive_data"),
    ]),
    dbc.Row([
        dbc.Col([
            dbc.Label("Referral Release Date: "),
            dmc.DateRangePicker(
                id = "date-picker",
                value=[min_referral_release_date, max_referral_release_date],
                minDate = min_referral_release_date,
                maxDate = max_referral_release_date,
                style={"marginLeft": "5%"}, 
            )
        ], width = 6),
    ]),
    html.Br(),
    dbc.Row([
        dcc.Graph(id="map_plot")
    ])
])

