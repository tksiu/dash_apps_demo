import pandas as pd
import plotly
from dash import html
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots
from dash.dependencies import Input, Output

from compute_functions import Page_2_Compute, Page_3_Compute

two_variable_calculation = Page_2_Compute.two_variable_calculation
differentiate_single_double_var = Page_2_Compute.differentiate_single_double_var
compute_lt = Page_3_Compute.compute_lt


class Page_Main_Visualize:
    def __init__(self, df, xcol, ycol, dcolor, filter_col=None, title=None, xaxis_title=None, yaxis_title=None):
        self.df = df
        self.xcol = xcol
        self.ycol = ycol
        self.dcolor = dcolor
        self.filter_col = filter_col
        self.title = title
        self.xaxis_title = xaxis_title
        self.yaxis_title = yaxis_title

    def static_bar_visualizer_year(self):
        fig = go.Figure()
        colors = ['lightslategray'] * len(list(set(self.df[self.xcol])))
        colors[-1] = self.dcolor

        fig.add_trace(go.Bar(x = self.df[self.xcol], y = self.df[self.ycol], text = self.df[self.ycol], marker_color = colors))
        fig.update_traces(textposition='outside', hovertemplate="%{x}: %{y}<extra></extra>")
        fig.update_yaxes(range = [0, self.df[self.ycol].max() * 1.1])
        fig.update_layout(title = '<b>' + self.title + '<b>',
                            xaxis=dict(
                                    title = self.xaxis_title,
                                    titlefont_size=16,
                                    tickfont_size=14,
                                    tickmode='linear'
                                ),
                            yaxis=dict(
                                    title = self.yaxis_title,
                                    titlefont_size=16,
                                    tickfont_size=14,
                                ),
                            legend_title_text = "",
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1
                            )
        )
        return fig

    def static_bar_visualizer_compare(self):
        colours = {
            sorted(list(set(self.df[self.filter_col])))[0]: 'lightslategray',
            sorted(list(set(self.df[self.filter_col])))[1]: self.dcolor
        }
        fig = px.bar(x = self.df[self.xcol], y = self.df[self.ycol], color = self.df[self.filter_col], text = self.df[self.ycol],
                     barmode="group", color_discrete_map = colours)
        fig.update_traces(textposition='outside', hovertemplate="%{x}: %{y}")
        fig.update_yaxes(range = [0, self.df[self.ycol].max() * 1.1])
        fig.update_layout(title = '<b>' + self.title + '<b>',
                            xaxis=dict(
                                    title = self.xaxis_title,
                                    titlefont_size=16,
                                    tickfont_size=14,
                                    tickmode='linear'
                                ),
                            yaxis=dict(
                                    title = self.yaxis_title,
                                    titlefont_size=16,
                                    tickfont_size=14,
                                ),
                            legend_title_text = "",
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1
                                )
        )
        return fig
    
    def static_line_visualizer_compare(self):
        colours = ['lightslategray', self.dcolor]
        fig = px.line(self.df, x = self.xcol, y = self.ycol, color = self.filter_col, text = self.ycol,
                      markers=True, color_discrete_sequence = colours)
        fig.update_traces(textposition='bottom right', hovertemplate="%{x}: %{y}")
        fig.update_yaxes(range = [0, self.df[self.ycol].max() * 1.1])
        fig.update_layout(title = '<b>' + self.title + '<b>',
                            xaxis=dict(
                                    title = self.xaxis_title,
                                    titlefont_size=16,
                                    tickfont_size=14,
                                    tickmode='linear'
                                ),
                            yaxis=dict(
                                    title = self.yaxis_title,
                                    titlefont_size=16,
                                    tickfont_size=14,
                                ),
                            legend_title_text = "",
                            legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1
                                )
        )
        return fig

    def card_visualizer(self, value, percent):
        if percent > 0:
            obj =  [
                    html.P("{:,}".format(round(value,2)), className="card-value", style = {"font-weight": "bold", "fontSize": 20}),
                    html.Span([html.I(className="fas fa-arrow-circle-up up", style = {"color":"Teal"}),
                                html.Span(" {:.2f}%   ".format(percent), style = {"color":"Teal", "fontSize":20, "font-weight":"bold"}),
                                html.Span("vs Last Year", style = {"color":"Teal", "padding-left": "40px"})
                              ])
                    ]
        elif percent < 0:
            obj =  [
                    html.P("{:,}".format(round(value,2)), className="card-value", style = {"font-weight": "bold", "fontSize": 20}),
                    html.Span([html.I(className="fas fa-arrow-circle-down down", style = {"color":"Tomato"}),
                                html.Span(" {:.2f}%   ".format(percent), style = {"color":"Tomato", "fontSize":20, "font-weight":"bold"}),
                                html.Span("vs Last Year", style = {"color":"Tomato", "padding-left": "40px"})
                              ])
                    ]
        else:
            obj =  [
                    html.P("{:,}".format(round(value,2)), className="card-value", style = {"font-weight": "bold", "fontSize": 20}),
                    html.Span([html.I(className="fas fa-minus", style = {"color":"DimGray"}),
                                html.Span(" {:.2f}%   ".format(percent), style = {"color":"DimGray", "fontSize":20, "font-weight":"bold"}),
                                html.Span("vs Last Year", style = {"color":"DimGray", "padding-left": "40px"})
                              ])
                    ]
        return obj


class Page_1_Visualize:
    def __init__(self, app, output_fig_id, output_fig_data_id, output_legend_id=None, standalone_switch_id=None, chart_type=None, **kwargs):
        self.app = app
        self.output_fig_id = output_fig_id
        self.output_fig_data_id = output_fig_data_id
        self.output_legend_id = output_legend_id
        self.standalone_switch_id = standalone_switch_id if standalone_switch_id != None else "dummy-switch"
        
        self.xcol = kwargs['dx'] if 'dx' in kwargs else None
        self.ycol = kwargs['dy'] if 'dy' in kwargs else None
        self.dcolor = kwargs['dcolor'] if 'dcolor' in kwargs else None
        self.title = kwargs['title'] if 'title' in kwargs else None
        self.xaxis_title = kwargs['xaxis_title'] if 'xaxis_title' in kwargs else None
        self.yaxis_title = kwargs['yaxis_title'] if 'yaxis_title' in kwargs else None
        self.subtitle = kwargs['subtitle'] if 'subtitle' in kwargs else None
        self.bins = kwargs['bins'] if 'bins' in kwargs else None
        self.pie_regroup = kwargs['pie_regroup'] if 'pie_regroup' in kwargs else None
        self.pie_regroup_threshold = kwargs['pie_regroup_threshold'] if 'pie_regroup_threshold' in kwargs else None
        self.pie_sorting_list = kwargs['pie_sorting_list'] if 'pie_sorting_list' in kwargs else None
        self.hist_sorting_list = kwargs['hist_sorting_list'] if 'hist_sorting_list' in kwargs else None

        self.alert_level_1 = kwargs['alert_level_1'] if 'alert_level_1' in kwargs else None
        self.alert_level_2 = kwargs['alert_level_2'] if 'alert_level_2' in kwargs else None
        self.gauge_threshold = kwargs['gauge_threshold'] if 'gauge_threshold' in kwargs else None
        self.gauge_text = kwargs['gauge_text'] if 'gauge_text' in kwargs else None
        self.gauge_upper_limit = kwargs['gauge_upper_limit'] if 'gauge_upper_limit' in kwargs else None
        
        self.supp_info_df = kwargs['supp_info_df'] if 'supp_info_df' in kwargs else None
        self.supp_info_col =  kwargs['supp_info_col'] if 'supp_info_col' in kwargs else None
        if isinstance(self.supp_info_df, pd.DataFrame) and self.supp_info_col != None:
            self.supp_info_df = self.supp_info_df[['user_id', self.supp_info_col]]
        
        if isinstance(self.output_fig_data_id, list) and len(self.output_fig_data_id) > 1:

            self.app.callback(
                Output(component_id=self.output_fig_id, component_property='figure'),
                [Input(component_id="collapse_choose_vis_mode", component_property='value'),
                 Input(component_id="collapse_choose_mode_b_options", component_property='value'),
                 Input(component_id=self.output_fig_data_id[0], component_property='data'), 
                 Input(component_id=self.output_fig_data_id[1], component_property='data'),
                 Input(component_id=self.standalone_switch_id, component_property='value'),]
            )(self.lineplot_visualizer)              
        
        else: 
            
            if self.output_legend_id == None:
                if chart_type == "pie":
                    self.app.callback(
                        Output(component_id=self.output_fig_id, component_property='figure'),
                        Input(component_id=self.output_fig_data_id, component_property='data')
                    )(self.pie_chart_visualizer)
                elif chart_type == "histogram":
                    self.app.callback(
                        Output(component_id=self.output_fig_id, component_property='figure'),
                        Input(component_id=self.output_fig_data_id, component_property='data')
                    )(self.histogram_visualizer)
                elif chart_type == "indicator":
                    self.app.callback(
                        Output(component_id=self.output_fig_id, component_property='figure'),
                        Input(component_id=self.output_fig_data_id, component_property='data')
                    )(self.guage_chart_visualizer)

            else:
                if chart_type == "histogram":
                    self.app.callback(
                        Output(component_id=self.output_fig_id, component_property='figure'),
                        [Input(component_id=self.output_legend_id, component_property='value'),
                         Input(component_id=self.output_fig_data_id, component_property='data')]
                    )(self.multi_histogram_visualizer)
                elif chart_type == "density":
                    self.app.callback(
                        Output(component_id=self.output_fig_id, component_property='figure'),
                        [Input(component_id=self.output_legend_id, component_property='value'),
                         Input(component_id=self.output_fig_data_id, component_property='data')]
                    )(self.multi_distribution_curve_plot_visualizer)

    def lineplot_visualizer(self, mode_input, mode_option_input, df_callback_0, df_callback_1, switch_input):

        if mode_input == "Comparison between groups (selected period)" and mode_option_input != None and mode_option_input != "":
            plot_df = pd.read_json(df_callback_1, orient='split')
            
            legend_col_mapping = {
                "Grouping Variable: Gender": "gender", 
                "Grouping Variable: Age": "age_group", 
                "Grouping Variable: Accesibility Levels": "accessibility_levels", 
                "Grouping Variable: Hospitalization": "hospitalization", 
                "Grouping Variable: Residential Care": "residential_care", 
                "Grouping Variable: Referral methods": "know_method"
            }
            legend_col = legend_col_mapping[mode_option_input]
            
            plot_df = plot_df.groupby([self.xcol, legend_col]).agg({"user_id": ['count']}).reset_index()
            plot_df.columns = [self.xcol, legend_col, self.ycol]

            if legend_col == "age_group":
                opts = ['<40', '40-49', '50-59', '60-64', '65-69', '>=70']
                plot_df[legend_col] = plot_df[legend_col].astype("category")
                plot_df[legend_col] = plot_df[legend_col].cat.set_categories(opts)
                plot_df = plot_df.sort_values([self.xcol, legend_col])

            fig = px.line(plot_df, x=self.xcol, y=self.ycol, text=self.ycol, 
                          color=legend_col, markers=True, color_discrete_sequence=px.colors.qualitative.Pastel)
            
        else:
            plot_df = pd.read_json(df_callback_0, orient='split')
            
            if switch_input == True:
                plot_df = plot_df.groupby([self.xcol, "entry_year"]).agg({"user_id": ['count']}).reset_index()
                plot_df.columns = [self.xcol,"entry_year",self.ycol]
                
                fig = px.line(plot_df, x=self.xcol, y=self.ycol, color="entry_year",
                              markers=True, color_discrete_sequence=px.colors.qualitative.Pastel)
            else:
                plot_df = plot_df.groupby([self.xcol]).agg({"user_id": ['count']}).reset_index()
                plot_df.columns = [self.xcol,self.ycol]
                
                fig = go.Figure()
                fig.add_trace(
                    go.Scatter(x = plot_df[self.xcol], y = plot_df[self.ycol], text = plot_df[self.ycol],
                               marker_color = self.dcolor, mode='lines+markers+text')
                    )
                fig.update_traces(textposition="bottom right")
            
        fig.update_yaxes(range = [0, plot_df[self.ycol].max() * 1.1])
        fig.update_layout(
            title = '<b>' + self.title + '<b>',
            xaxis=dict(
                    title = self.xaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                    tickmode="linear",
                ),
            yaxis=dict(
                    title = self.yaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
        )
        return fig
    
    def guage_chart_visualizer(self, df_callback):
        plot_df = pd.read_json(df_callback, orient='split')
        percent = plot_df[self.ycol].sum() / plot_df[self.ycol].count() * 100
        fig = go.Figure()
        fig.add_trace(
            go.Indicator(
                value = percent,
                delta = {"reference": self.gauge_threshold, 
                         'increasing': {'color': "RebeccaPurple"},
                         'decreasing': {'color': "IndianRed"}},
                mode = "gauge+number+delta",
                gauge = {'axis': {'range': [0, self.gauge_upper_limit],
                                  'tickwidth': 1, 
                                  'tickcolor': "RosyBrown"},
                         'bar': {'color': "SandyBrown"},
                         'steps': [
                            {'range': [0, self.alert_level_1], 'color': "Wheat"},
                            {'range': [self.alert_level_1, self.alert_level_2], 'color': "Tan"}
                         ],
                         'threshold' : {'line': {'color': "DarkMagenta", 'width': 5}, 
                                        'thickness': 0.5, 
                                        'value': self.gauge_threshold}
                        },
                domain = {'row': 0, 'column': 0}
            )
        )
        fig.update_layout(
            template = {'data': {'indicator': [{
                                    'title': {'text': self.gauge_text},
                                    'mode' : "number+delta+gauge",
                                }]
                        }}
        )
        return fig

    def pie_chart_visualizer(self, df_callback):
        plot_df = pd.read_json(df_callback, orient='split')
        plot_df = plot_df.groupby([self.xcol]).agg({"user_id": ['count']}).reset_index()
        plot_df.columns = [self.xcol, self.ycol]
        
        if self.pie_regroup == True:
            plot_df[self.xcol][plot_df[self.ycol] < self.pie_regroup_threshold] = "Other"
            plot_df = plot_df.groupby([self.xcol]).agg({self.ycol: ['sum']}).reset_index()
            plot_df.columns = [self.xcol, self.ycol]
        
        fig = go.Figure()
        color_discrete_sequence = self.dcolor
        
        if self.pie_sorting_list != None:
            plot_df = plot_df.set_index(self.xcol)
            plot_df = plot_df.reindex(self.pie_sorting_list)
            plot_df = plot_df.reset_index()
            labels = list(plot_df[self.xcol])
            values = list(plot_df[self.ycol])
            fig.add_trace(go.Pie(labels=labels, values=values, sort = False,
                                 textinfo='label+value+percent', 
                                 textposition='inside', 
                                 insidetextorientation='horizontal'))
        else:
            labels = list(plot_df[self.xcol])
            values = list(plot_df[self.ycol])
            fig.add_trace(go.Pie(labels=labels, values=values, 
                                 textinfo='label+value+percent',
                                 textposition='inside', 
                                 insidetextorientation='horizontal'))
            
        fig.update_traces(hole=0.4, hoverinfo="label+value+percent", marker=dict(colors = color_discrete_sequence))
        fig.update_layout(
            annotations=[dict(text=self.subtitle, x=0.5, y=0.5, font_size=12, showarrow=False)],
            margin=dict(t=25, b=25, l=0, r=0)
        )
        return fig

    def histogram_visualizer(self, df_callback):
        hist_df = pd.read_json(df_callback, orient='split')
        hist_df = hist_df.merge(self.supp_info_df, how="left", left_on=["user_id"], right_on=["user_id"])
        hist_df['hist_count'] = 1
        hist_df = hist_df[[self.xcol, 'hist_count']]

        fig = px.histogram(hist_df, x=self.xcol, 
                           marginal="box", 
                           hover_data=hist_df.columns, 
                           nbins=self.bins, 
                           color_discrete_sequence=self.dcolor)
        fig.update_layout(
            xaxis=dict(
                    title = self.xaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
            yaxis=dict(
                    title = self.yaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
        )
        return fig

    def multi_histogram_visualizer(self, subgrp_callback, df_callback):
        hist_df = pd.read_json(df_callback, orient='split')
        hist_df = hist_df.merge(self.supp_info_df, how="left", left_on=["user_id"], right_on=["user_id"])
        hist_df['hist_count'] = 1
        hist_df = hist_df[[self.xcol, 'hist_count', subgrp_callback]]

        if subgrp_callback == "age_group":
            opts = ['<40', '40-49', '50-59', '60-64', '65-69', '>=70']
        elif subgrp_callback == "gender":
            opts = ['Female','Male']
        elif subgrp_callback == "accessibility_levels":
            opts = ['High (1km; 10min)', 'Intermediate (3km; 30min)', 'Low (5km; 60min)', 'Poor']
        else:
            opts = ["No","Yes"]
        
        hist_df[subgrp_callback] = hist_df[subgrp_callback].astype("category")
        hist_df[subgrp_callback] = hist_df[subgrp_callback].cat.set_categories(opts)
        hist_df = hist_df.sort_values([subgrp_callback])

        fig = px.histogram(hist_df, x=self.xcol, 
                           color=subgrp_callback,
                           marginal="box", 
                           hover_data=hist_df.columns, 
                           nbins=self.bins,
                           color_discrete_sequence=self.dcolor)
        fig.update_layout(
            xaxis=dict(
                    title = self.xaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
            yaxis=dict(
                    title = self.yaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
        )
        return fig
    
    def multi_distribution_curve_plot_visualizer(self, subgrp_callback, df_callback):
        plot_df = pd.read_json(df_callback, orient='split')

        if subgrp_callback == "age_group":
            opts = ['<40', '40-49', '50-59', '60-64', '65-69', '>=70']
        elif subgrp_callback == "gender":
            opts = ['Female','Male']
        elif subgrp_callback == "accessibility_levels":
            opts = ['High (1km; 10min)', 'Intermediate (3km; 30min)', 'Low (5km; 60min)', 'Poor']
        else:
            opts = ["No","Yes"]
        
        plot_df[subgrp_callback] = plot_df[subgrp_callback].astype("category")
        plot_df[subgrp_callback] = plot_df[subgrp_callback].cat.set_categories(opts)
        plot_df = plot_df.sort_values([subgrp_callback])

        group_labels = list(set(plot_df[subgrp_callback]))
        hist_data = list(set(plot_df[self.xcol]))
        colors = self.dcolor

        fig = plotly.figure_factory.create_distplot(hist_data, group_labels, show_hist=False, colors=colors)
        fig.update_layout(
            xaxis=dict(
                    title = self.xaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
            yaxis=dict(
                    title = self.yaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
        )
        return fig
    

class Page_2_Visualize:
    def __init__(self, app, output_fig_id, output_fig_data_id, collapse_dropdown_id=None, chart_type=None, **kwargs):
        self.app = app
        self.output_fig_id = output_fig_id
        self.output_fig_data_id = output_fig_data_id
        self.collapse_dropdown_id = collapse_dropdown_id

        self.two_variable_calculation = two_variable_calculation
        self.differentiate_single_double_var = differentiate_single_double_var
        
        self.bar_color = kwargs['bar_color'] if 'bar_color' in kwargs else None
        self.line_color = kwargs['line_color'] if 'line_color' in kwargs else None
        self.group_color_palette = kwargs['group_color_palette'] if 'group_color_palette' in kwargs else None
        self.title = kwargs['title'] if 'title' in kwargs else None
        self.title = kwargs['title'] if 'title' in kwargs else None
        self.title_second = kwargs['title_second'] if 'title_second' in kwargs else None
        self.yaxis_title = kwargs['yaxis_title'] if 'yaxis_title' in kwargs else None
        self.yaxis_title_second = kwargs['yaxis_title_second'] if 'yaxis_title_second' in kwargs else None

        self.aggregate_cols_0 = kwargs['aggregate_cols_0'] if 'aggregate_cols_0' in kwargs else None
        self.aggregate_cols_1 = kwargs['aggregate_cols_1'] if 'aggregate_cols_1' in kwargs else None
        self.aggregate_fns_0 = kwargs['aggregate_fns_0'] if 'aggregate_fns_0' in kwargs else None
        self.aggregate_fns_1 = kwargs['aggregate_fns_1'] if 'aggregate_fns_1' in kwargs else None 

        self.two_var_operations = kwargs['two_var_operations'] if 'two_var_operations' in kwargs else None
        self.two_var_operations_logic = kwargs['two_var_operations_logic'] if 'two_var_operations_logic' in kwargs else None
        self.two_var_col_name = kwargs['two_var_col_name'] if 'two_var_col_name' in kwargs else None
        
        self.xcol = kwargs['dx'] if 'dx' in kwargs else None
        self.ycol = kwargs['dy'] if 'dy' in kwargs else None
        self.dcolor = kwargs['dcolor'] if 'dcolor' in kwargs else None
        self.subtitle = kwargs['subtitle'] if 'subtitle' in kwargs else None
        
        self.pie_regroup = kwargs['pie_regroup'] if 'pie_regroup' in kwargs else None
        self.pie_regroup_threshold = kwargs['pie_regroup_threshold'] if 'pie_regroup_threshold' in kwargs else None
        self.pie_sorting_list = kwargs['pie_sorting_list'] if 'pie_sorting_list' in kwargs else None

        self.year_options = kwargs['year_options'] if 'year_options' in kwargs else None
        
        self.chart_type = chart_type
        
        if self.chart_type == "combo":
            self.app.callback(
                Output(component_id = self.output_fig_id, component_property="figure"),
                [Input(component_id = self.output_fig_data_id, component_property="data"),
                 Input(component_id = "page_2_radios", component_property="value"),
                 Input(component_id = self.collapse_dropdown_id, component_property="value")]
            )(self.combo_plot_visualizer)
        
        elif self.chart_type == "pie": 
            self.app.callback(
                Output(component_id = self.output_fig_id, component_property="figure"),
                Input(component_id = self.output_fig_data_id, component_property="data"),
            )(self.pie_plot_visualizer)
            
        elif self.chart_type == "line": 
            self.app.callback(
                Output(component_id = self.output_fig_id, component_property="figure"),
                [Input(component_id = self.output_fig_data_id, component_property="data"),
                 Input(component_id = "page_2_radios", component_property="value"),
                 Input(component_id = self.collapse_dropdown_id, component_property="value")]
            )(self.line_plot_visualizer)

    def combo_plot_visualizer(self, df_callback, mode_input, dropdown_input):
        read_df = pd.read_json(df_callback, orient='split')
        
        if mode_input == 1:
            fig = go.Figure()
            fig = make_subplots(specs=[[{"secondary_y": True}]])
            
            plot_df_1, var_bar = self.differentiate_single_double_var(
                                    self.two_variable_calculation,
                                    read_df, 
                                    ['end_year'], 
                                    self.aggregate_cols_0, self.aggregate_fns_0, 
                                    self.two_var_operations, self.two_var_operations_logic, self.two_var_col_name
                                    )
            plot_df_2, var_line = self.differentiate_single_double_var(
                                    self.two_variable_calculation,
                                    read_df, 
                                    ['end_year'], 
                                    self.aggregate_cols_1, self.aggregate_fns_1, 
                                    self.two_var_operations, self.two_var_operations_logic, self.two_var_col_name
                                    )
            plot_df = plot_df_1.merge(plot_df_2, how="left", on="end_year")
            
            fig.add_trace( 
                go.Bar(x = plot_df['end_year'], y = plot_df[var_bar], text = plot_df[var_bar], 
                       marker_color = self.bar_color, textposition = "outside", name = var_bar,
                       hovertemplate = '%{x} %{y:.0f}', texttemplate = '%{y:.0f}')
                )
            
            fig.add_trace( 
                go.Scatter(x = plot_df['end_year'], y = plot_df[var_line], text = plot_df[var_line], 
                           marker_color = self.line_color, mode='lines+markers+text', name = var_line,
                           hovertemplate = '%{x} %{y:.1%}', texttemplate = '%{y:.1%}', textposition="bottom right"),
                secondary_y=True
                )
            
            fig.update_layout(title_text = '<b>' + self.title + '<b>',
                              legend=dict(
                                orientation="h",
                                yanchor="bottom",
                                y=1.02,
                                xanchor="right",
                                x=1
                                ))
            fig.update_xaxes(title_text = "Year")
            fig.update_yaxes(title_text = self.yaxis_title, secondary_y=False)
            fig.update_yaxes(title_text = self.yaxis_title_second, secondary_y=True)
            fig.update_yaxes(range = [0, plot_df[var_bar].max() * 1.1], secondary_y=False)
            fig.update_yaxes(range = [0, plot_df[var_line].max() * 1.1], secondary_y=True)
            fig.update_yaxes(tickformat = ".0%", secondary_y=True)
        
        else:
            if mode_input == 3:
                group_cols = ['end_month','end_year']
                xaxis_title = "Month"
            elif mode_input == 2:
                group_cols = ['end_quarter','end_year']
                xaxis_title = "Quarter"
                
            if dropdown_input == 0:
                agg_cols = self.aggregate_cols_0
                agg_fns = self.aggregate_fns_0
            elif dropdown_input == 1:
                agg_cols = self.aggregate_cols_1
                agg_fns = self.aggregate_fns_1
                
            plot_df, var = self.differentiate_single_double_var(
                                self.two_variable_calculation,
                                read_df, 
                                group_cols, 
                                agg_cols, agg_fns, 
                                self.two_var_operations, self.two_var_operations_logic, self.two_var_col_name
                                )
            
            fig = px.line(plot_df, x = group_cols[0], y = var, color = group_cols[1],
                          markers=True, color_discrete_sequence=px.colors.qualitative.Pastel,
                          category_orders={group_cols[1]: self.year_options})
            
            if dropdown_input == 1:
                fig.update_traces(hovertemplate = '%{y:.1%}')
                fig.update_yaxes(tickformat = ".0%")
            
            fig.update_layout(title_text = '<b>' + self.title + '<b>')
            fig.update_xaxes(title_text = xaxis_title)
            fig.update_yaxes(title_text = self.yaxis_title)
            fig.update_yaxes(range = [0, plot_df[var].max() * 1.1])
        
        return fig
    
    def line_plot_visualizer(self, df_callback, mode_input, dropdown_input):
        plot_df = pd.read_json(df_callback, orient='split')

        if mode_input == 3:
            group_cols = ['end_month','end_year']
            xaxis_title = "Month"
        elif mode_input == 2:
            group_cols = ['end_quarter','end_year']
            xaxis_title = "Quarter"
        elif mode_input == 1:
            group_cols = ['end_year']
            xaxis_title = "Year"
            
        if dropdown_input == 0:
            var = self.aggregate_cols_0
            agg_fn = self.aggregate_fns_0
            title = self.title
            yaxis_title = self.yaxis_title
        elif dropdown_input == 1:
            var = self.aggregate_cols_1
            agg_fn = self.aggregate_fns_1
            title = self.title_second
            yaxis_title = self.yaxis_title_second
            
        plot_df = plot_df.groupby(group_cols).agg({var: agg_fn}).reset_index()
        plot_df.columns = group_cols + [var]
        
        if len(group_cols) > 1:
            fig = px.line(plot_df, x = group_cols[0], y = var, color = group_cols[1],
                          markers=True, color_discrete_sequence=px.colors.qualitative.Pastel,
                          category_orders={group_cols[1]: self.year_options})
        else:
            fig = go.Figure()
            fig.add_trace( 
                go.Scatter(x = plot_df[group_cols[0]], y = plot_df[var], text = plot_df[var], 
                           marker_color = self.line_color, mode='lines+markers+text')
                )
            fig.update_traces(textposition="bottom right")
        
        fig.update_yaxes(range = [0, plot_df[var].max() * 1.1])
        
        fig.update_layout(title_text = '<b>' + title + '<b>')
        fig.update_xaxes(title_text = xaxis_title)
        fig.update_yaxes(title_text = yaxis_title)

        return fig
    
    def pie_plot_visualizer(self, df_callback):
        plot_df = pd.read_json(df_callback, orient='split')
        plot_df = plot_df.groupby([self.xcol]).agg({self.ycol: ['sum']}).reset_index()
        plot_df.columns = [self.xcol, self.ycol]
        
        if self.pie_regroup == True:
            plot_df[self.xcol][plot_df[self.ycol] < self.pie_regroup_threshold] = "Other"
            plot_df = plot_df.groupby([self.xcol]).agg({self.ycol: ['sum']}).reset_index()
            plot_df.columns = [self.xcol, self.ycol]
        
        fig = go.Figure()
        color_discrete_sequence = self.dcolor
        
        if self.pie_sorting_list != None:
            plot_df = plot_df.set_index(self.xcol)
            plot_df = plot_df.reindex(self.pie_sorting_list)
            plot_df = plot_df.reset_index()
            labels = list(plot_df[self.xcol])
            values = list(plot_df[self.ycol])
            fig.add_trace(go.Pie(labels=labels, values=values, 
                                 textinfo='label+value+percent', sort = False, 
                                 textposition='inside', 
                                 insidetextorientation='horizontal'))
        else:
            labels = list(plot_df[self.xcol])
            values = list(plot_df[self.ycol])
            fig.add_trace(go.Pie(labels=labels, values=values, 
                                 textinfo='label+value+percent', 
                                 textposition='inside', 
                                 insidetextorientation='horizontal'))
            
        fig.update_traces(hole=0.4, hoverinfo="label+value+percent", marker=dict(colors = color_discrete_sequence))
        fig.update_layout(
            annotations=[dict(text=self.subtitle, x=0.5, y=0.5, font_size=12, showarrow=False)],
            margin=dict(t=20, b=20, l=10, r=10)
        )
        return fig
    

class Page_3_Visualize:
    def __init__(self, app, output_fig_id=None, output_fig_data_id=None, chart_type=None, **kwargs):
        self.app = app
        self.chart_type = chart_type
        if self.chart_type == None:
            self.output_fig_id = None
            self.output_fig_data_id = None
        else:
            self.output_fig_id = output_fig_id
            self.output_fig_data_id = output_fig_data_id

        self.compute_lt = compute_lt
        
        self.discrete_colors = kwargs['discrete_colors'] if 'discrete_colors' in kwargs else None
        self.gradient_colors = kwargs["gradient_colors"] if "gradient_colors" in kwargs else None
        
        self.bins = kwargs["bins"] if "bins" in kwargs else None
        self.sunburst_threshold = kwargs["sunburst_threshold"] if "sunburst_threshold" in kwargs else None
        self.chord_attribute_df = kwargs["chord_attribute_df"] if "chord_attribute_df" in kwargs else None
        
        self.bar_title = kwargs['bar_title'] if 'bar_title' in kwargs else None
        self.sankey_title = kwargs['sankey_title'] if 'sankey_title' in kwargs else None
        self.heat_x_title = kwargs['heat_x_title'] if 'heat_x_title' in kwargs else None
        self.heat_y_title = kwargs['heat_y_title'] if 'heat_y_title' in kwargs else None
        self.sunburst_title = kwargs['sunburst_title'] if 'sunburst_title' in kwargs else None
        self.distplot_title = kwargs['distplot_title'] if 'distplot_title' in kwargs else None
        self.bar_color = kwargs['bar_color'] if 'bar_color' in kwargs else None
        self.bar_xaxis_title = kwargs['bar_xaxis_title'] if 'bar_xaxis_title' in kwargs else None
        self.bar_yaxis_title = kwargs['bar_yaxis_title'] if 'bar_yaxis_title' in kwargs else None
        
        self.sc_xcol = kwargs['sc_xcol'] if 'sc_xcol' in kwargs else None
        self.sc_ycol = kwargs['sc_ycol'] if 'sc_ycol' in kwargs else None
        self.sc_color_col = kwargs['sc_color_col'] if 'sc_color_col' in kwargs else None
        self.sc_size_col = kwargs['sc_size_col'] if 'sc_size_col' in kwargs else None
        self.sc_title = kwargs['sc_title'] if 'sc_title' in kwargs else None
        self.xaxis_title = kwargs['xaxis_title'] if 'xaxis_title' in kwargs else None
        self.yaxis_title = kwargs['yaxis_title'] if 'yaxis_title' in kwargs else None
        self.user_demog_df = kwargs['user_demog_df'] if 'user_demog_df' in kwargs else None
        
        if chart_type == "scatter":
            self.app.callback(
                Output(component_id=self.output_fig_id, component_property="figure"),
                Input(component_id=self.output_fig_data_id, component_property="data")
            )(self.update_scatter)

        else:
            self.app.callback(
                Output(component_id="sankey_diagram_treatments", component_property="figure"),
                Input(component_id="page_3_interactive_data", component_property="data")
            )(self.update_sankey)

            self.app.callback(
                Output(component_id="chord_diagram_service_plans", component_property="figure"),
                Input(component_id="page_3_interactive_data", component_property="data")
            )(self.update_heatmap)

            self.app.callback(
                Output(component_id="histogram_treatments_lead_time", component_property="figure"),
                Input(component_id="page_3_interactive_data", component_property="data")
            )(self.update_lead_time_boxplot)

            self.app.callback(
                Output(component_id="bar_total_num_treatments", component_property="figure"),
                Input(component_id="page_3_interactive_data", component_property="data")
            )(self.update_bar)

            self.app.callback(
                Output(component_id="sunburst_pain_pos", component_property="figure"),
                [Input(component_id="page_3_interactive_data", component_property="data"),
                Input(component_id="pain_pos_id", component_property="value")]
            )(self.update_sunburst)

    def update_sankey(self, df_callback):
        dat = pd.read_json(df_callback, orient='split')

        dat = dat.groupby(['referral_purpose','intake_arranged','final_treatment']).agg({"user_id": ["count"]}).reset_index()
        dat.columns = ['referral_purpose','intake_arranged','final_treatment','count']

        labels_t0 = list(set(dat['referral_purpose']))
        labels_t1 = list(set(dat['intake_arranged']))
        labels_t2 = list(set(dat['final_treatment']))
        labels = labels_t0 + labels_t1 + labels_t2

        colors_map = {labels[x]: self.discrete_colors[x] for x in range(len(list(set(labels))))}
        colors = [colors_map[x] for x in labels]

        source_list = []
        target_list = []
        value_list = []
        color_list = []
        for x in range(len(labels_t0)):
            for y in range(len(labels_t1)):
                source_list.append(x)
                target_list.append(len(labels_t0) + y)
                value_list.append(dat[(dat['referral_purpose'] == labels_t0[x]) & (dat['intake_arranged'] == labels_t1[y])]['count'].sum())
                color_list.append(colors_map[labels_t0[x]] if labels_t0[x] == labels_t1[y] else "Grey")
        for y in range(len(labels_t1)):
            for z in range(len(labels_t2)):
                source_list.append(len(labels_t0) + y)
                target_list.append(len(labels_t0) + len(labels_t1) + z)
                value_list.append(dat[(dat['intake_arranged'] == labels_t1[y]) & (dat['final_treatment'] == labels_t2[z])]['count'].sum())
                color_list.append(colors_map[labels_t1[y]] if labels_t1[y] == labels_t2[z] else "Grey")

        fig = go.Figure(
            data=[
                go.Sankey(
                    valueformat=".0f",
                    node = dict(
                    pad = 15,
                    thickness = 50,
                    line = dict(color = "black", width = 0.5),
                    label = labels,
                    color = colors,
                    ),
                    link = dict(
                    arrowlen = 15,
                    source = source_list,
                    target = target_list,
                    value = value_list,
                    color = color_list,
                    )
                )
            ]
        )
        fig.update_layout(title=dict(text=self.sankey_title, 
                                     font=dict(size=16)
                                     ),
                          font_size=15)
        return fig
    
    def update_heatmap(self, df_callback):
        dat = pd.read_json(df_callback, orient='split')
        dat = dat[['user_id']].merge(self.chord_attribute_df, how = "left", on = "user_id")
        dat2 = dat.groupby(['user_id']).agg({dat.columns[1]: ['first'], dat.columns[2]: ['last']}).reset_index()
        dat2.columns = ['user_id', dat.columns[1], dat.columns[2]]

        dat2 = pd.crosstab(dat2[dat.columns[1]], dat2[dat.columns[2]])
        idx = dat2.columns.union(dat2.index)
        dat2 = dat2.reindex(index=idx, columns=idx, fill_value=0)

        fig = px.imshow(dat2,
                        labels=dict(x=self.heat_x_title, 
                                    y=self.heat_y_title),
                        x=dat2.index,
                        y=dat2.columns,
                        color_continuous_scale=self.gradient_colors, origin='lower', text_auto=True, 
               )
        return fig
    
    def update_lead_time_boxplot(self, df_callback):
        dat = pd.read_json(df_callback, orient='split')

        dat['refer2first_lead_time'] = pd.Series(self.compute_lt(dat['referral_release_date'], dat['first_clinic_date']))
        dat['first2final_lead_time'] = pd.Series(self.compute_lt(dat['first_clinic_date'], dat['final_clinic_date']))
        hist_df = dat[['refer2first_lead_time','first2final_lead_time','hydro_lead_time']]
        
        fig = make_subplots(rows=3, cols=1)
        colors = [px.colors.qualitative.T10[0],
                  px.colors.qualitative.Set2[0],
                  px.colors.qualitative.Vivid[0]]

        for n in range(3):
            tem_hist = hist_df[hist_df.columns[n]][(hist_df[hist_df.columns[n]] >= -365) &
                                                   (hist_df[hist_df.columns[n]] <= 365)]
            box_fig = go.Box(x = tem_hist, 
                             quartilemethod="exclusive", 
                             name = hist_df.columns[n],
                             boxpoints = False, 
                             marker_color=colors[n])
            fig.append_trace(
                box_fig, row=n+1, col=1
                )

        fig.update_layout(title=dict(text=self.distplot_title, 
                                     font=dict(size=16)
                                     ))
        return fig

    def update_bar(self, df_callback):
        dat = pd.read_json(df_callback, orient='split')
        dat = dat.groupby(['num_physio_treatment']).agg({"user_id":["count"]}).reset_index()
        dat.columns = ['num_physio_treatment','count']

        fig = go.Figure()
        fig.add_trace(
            go.Bar(x = dat['num_physio_treatment'], y = dat["count"], text = dat["count"], marker_color = self.bar_color)
            )
        fig.update_traces(textposition = "outside", hovertemplate="%{x}: %{y}<extra></extra>")
        fig.update_layout(title_text = self.bar_title)
        fig.update_xaxes(title_text = self.bar_xaxis_title)
        fig.update_yaxes(title_text = self.bar_yaxis_title)
        fig.update_yaxes(range = [0, dat["count"].max() * 1.1])
        return fig
        
    def update_sunburst(self, df_callback, button_options):
        dat = pd.read_json(df_callback, orient='split')
        agg_dat = dat[button_options].sum(axis=0)
        agg_dat_df = agg_dat.reset_index()
        agg_dat_df.columns = ['pain_pos','count']

        body_main = {
            "trunk": ["back", "neck", "chest | rib", "shoulder", "hip | buttock | coccyx | pelvis | sacral", "trunk | thoracic"], 
            "lower limb": ["knee","leg","foot","thigh","calf","ankle | heel","toe"], 
            "upperlimb": ["arm","elbow","wrist","hand | fingers"],
            "others": ["joint","multiple","neuro"]
        }
        body_mains = agg_dat_df['pain_pos'].apply(lambda x: [i for i, v in body_main.items() if x in v][0])
        agg_dat_df['body_main'] = body_mains
        agg_dat_df = agg_dat_df[agg_dat_df['count'] > self.sunburst_threshold]

        fig = px.sunburst(agg_dat_df, path=['body_main','pain_pos'], values='count', color_discrete_sequence=self.discrete_colors)
        
        fig.update_layout(title=dict(text=self.sunburst_title, 
                                     font=dict(size=16)
                                     ),
                          margin=dict(t=25, b=25, l=0, r=0))
        return fig

    def update_scatter(self, df_callback):
        dat = pd.read_json(df_callback, orient='split')
        dat['first2final_lead_time'] = pd.Series(self.compute_lt(dat['first_clinic_date'], dat['final_clinic_date']))

        dat = dat.merge(self.user_demog_df, how = "left", on = "user_id")
        dat = dat[[self.sc_xcol, self.sc_ycol, self.sc_color_col, self.sc_size_col]]

        fig = px.scatter(dat , x=self.sc_xcol, y=self.sc_ycol, 
                         color=self.sc_color_col, size=self.sc_size_col,
                         color_discrete_sequence=px.colors.qualitative.Safe)
        fig.update_layout(
            title=self.sc_title,
            xaxis=dict(
                    title = self.xaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
            yaxis=dict(
                    title = self.yaxis_title,
                    titlefont_size=16,
                    tickfont_size=14,
                ),
            plot_bgcolor='rgba(0,0,0,0)'
        )
        fig.update_xaxes(showline=True, linewidth=1, linecolor='black', gridcolor='lightgrey')
        fig.update_yaxes(showline=True, linewidth=1, linecolor='black', gridcolor='lightgrey')
        return fig
    

class Page_4_Visualize:
    def __init__(self, app, geojson_data, **kwargs):
        self.app = app
        self.geojson_data = geojson_data
        self.discrete_colors = kwargs['discrete_colors'] if 'discrete_colors' in kwargs else None
        self.gradient_colors = kwargs["gradient_colors"] if "gradient_colors" in kwargs else None
        self.global_region_list = kwargs["global_region_list"] if "global_region_list" in kwargs else None

        self.app.callback(
            Output(component_id="map_plot", component_property="figure"),
            Input(component_id="page_4_interactive_data", component_property="data")
        )(self.choropleth_map)
    
    def choropleth_map(self, df_callback):
        dat = pd.read_json(df_callback, orient='split')
        dat = dat.groupby(['referral_district']).agg({'user_id': ['count']}).reset_index()
        dat.columns = ['referral_district','referral_count']

        if self.global_region_list != None:
            leftover = [x for x in self.global_region_list if x not in dat['referral_district'].values.tolist()]
            if len(leftover) > 0:
                dat_supp = pd.DataFrame(
                    {'referral_district': leftover,
                     'referral_count': [0] * len(leftover)}
                )
                dat = pd.concat([dat, dat_supp], axis=1).reset_index(drop=True)
        
        fig = go.Figure(
            data = go.Choropleth(
                        geojson=self.geojson_data,
                        z = dat['referral_count'],
                        locations = dat['referral_district'],
                        featureidkey="properties.ID",
                        locationmode = 'geojson-id',
                    ))
        fig.update_geos(fitbounds="locations",
                        showcountries=False,
                        showcoastlines=False,
                        showland=False,)
        fig.update_layout(margin={"r":0,"t":0,"l":0,"b":0},
                          height=800,
                          hoverlabel=dict(
                                    font=dict(
                                            family='sans-serif', 
                                            size=25)
                                    )
                        )
        return fig 
