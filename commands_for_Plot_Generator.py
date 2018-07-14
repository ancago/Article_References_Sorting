import pandas as pd

from Plot_Generator import *

x = PlotGenerator('765_Track_statistics.csv')

y = DataForPlot('765_Track_statistics.csv')

# # x.__init__('765_Track_statistics.csv')

# x = x.data_frame()

# print(x.shape)

# print(type(x))

# print(x.create_column_with_values_separated_by_threshold('TRACK_DISPLACEMENT', 'TRACK_DURATION'))

# print(x.establishing_sign_and_threshold(1))

# print(x.establishing_number_of_thresholds_on_one_column())

# print(sign_and_threshold_list.append(x.establishing_sign_and_threshold(2)))

# print(x.identify_intervals_convergence(2))

# print(x[x['TRACK_DISPLACEMENT'].between(0.5, 5)])



# y = pd.read_csv('data.csv')
#
# print(y[y['Column_3'].between(12,34)])
#
# print(x.choose_data_for_plot())

# print(x.choose_plot_type())

# print(x.select_data_by_threshold(2, 4))

print(y.choose_data_range())

