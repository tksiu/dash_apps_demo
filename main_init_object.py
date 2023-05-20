from dataloader import *
from compute_functions import Page_Main_Compute
from graph_functions import Page_Main_Visualize

#### Page Main (Home) objects

compute_main = Page_Main_Compute(d0_user, d1_class, d2_phys)
preload_aggregate_users_yr = compute_main.aggregate_users_yr.reset_index()
preload_aggregate_users_yr.columns = ['entry_year','new_admitted_users']
preload_aggregate_users_qr = compute_main.aggregate_users_qr.reset_index()
preload_aggregate_users_qr.columns = ['entry_year','entry_quarter','new_admitted_users']
preload_aggregate_users_mn = compute_main.aggregate_users_mn.reset_index()
preload_aggregate_users_mn.columns = ['entry_year','entry_month','new_admitted_users']

graphics_main = Page_Main_Visualize(
    df = preload_aggregate_users_yr, 
    xcol = "entry_year", 
    ycol = "new_admitted_users", 
    dcolor = 'lightsalmon', 
    title = "Total New Admitted Users by Year",
    xaxis_title = "Entry Year", yaxis_title = "No. of New Users"
    )
graph_vis_main_a2_year = graphics_main.static_bar_visualizer_year()

graph_vis_main_a2_quarter = Page_Main_Visualize(
    df = preload_aggregate_users_qr, 
    xcol = "entry_quarter", 
    ycol = "new_admitted_users", 
    filter_col = "entry_year",
    dcolor = 'lightsalmon', 
    title = "Total New Admitted Users by Quarter",
    xaxis_title = "Entry Quarter", yaxis_title = "No. of New Users"
    )
graph_vis_main_a2_quarter = graph_vis_main_a2_quarter.static_line_visualizer_compare()

graph_vis_main_a2_month = Page_Main_Visualize(
    df = preload_aggregate_users_mn, 
    xcol = "entry_month", 
    ycol = "new_admitted_users", 
    filter_col = "entry_year",
    dcolor = 'lightsalmon', 
    title = "Total New Admitted Users by Month",
    xaxis_title = "Entry Month", yaxis_title = "No. of New Users"
    )
graph_vis_main_a2_month = graph_vis_main_a2_month.static_line_visualizer_compare()

card_vis_main_a1 = graphics_main.card_visualizer(compute_main.new_entry[0], compute_main.new_entry[1])
card_vis_main_a2 = graphics_main.card_visualizer(compute_main.new_contact_consent[0] * 100, compute_main.new_contact_consent[1])
card_vis_main_b1 = graphics_main.card_visualizer(compute_main.total_class[0], compute_main.total_class[1])
card_vis_main_b2 = graphics_main.card_visualizer(compute_main.total_class_sess[0], compute_main.total_class_sess[1])
card_vis_main_b3 = graphics_main.card_visualizer(compute_main.total_class_mins[0] / 60.0, compute_main.total_class_mins[1])
card_vis_main_b4 = graphics_main.card_visualizer(compute_main.total_class_registry[0], compute_main.total_class_registry[1])
card_vis_main_c1 = graphics_main.card_visualizer(compute_main.total_physio_intakes[0], compute_main.total_physio_intakes[1])
card_vis_main_c2 = graphics_main.card_visualizer(compute_main.total_physio_intakes_with_pre_ax[0], compute_main.total_physio_intakes_with_pre_ax[1])
card_vis_main_c3 = graphics_main.card_visualizer(compute_main.total_physio_discharges[0], compute_main.total_physio_discharges[1])
card_vis_main_c4 = graphics_main.card_visualizer(compute_main.total_physio_dc_follow[0], compute_main.total_physio_dc_follow[1])

