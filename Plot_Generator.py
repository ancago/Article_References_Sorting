from fileinput import filename

import pandas as pd
import operator as op
import numpy as np
import matplotlib.pyplot as plt


class PlotGenerator:

    def __init__(self, filename):
        self.filename = filename


    def data_frame(self):
        return pd.read_csv(str(self.filename))


    def choose_plot_type(self):
        print('Please select plot type from the following: '
              '\n\n H = Histogram '
              '\n B = Bar chart '
              '\n L = Linear '
              '\n P = Pie chart\n')
        plot = input('Your plot type is: ')
        plot = plot.upper()
        # if plot == 'H':
        #     return Histogram.plotting_histogram(Histogram(self))
        # elif plot == 'B':
        #     return plt.bar(x_sequence, y_heights)
        # elif plot == 'L':
        #     return plt.plot(x_coordinate, y_coordinate)
        # elif plot == 'P':
        #     return plt.pie(wedge_size)
        # else:
        #     print('\nIncorrect input.')
        #     return self.choose_plot_type()


class DataForPlot(PlotGenerator):


    def choose_data_range(self):
        data = input('Do you want to put a threshold on column values? y/n:')
        if data == 'y':
            return self.select_data_by_threshold()
        elif data == 'n':
            return self.select_column_data()
        else:
            print('Incorrect input. ')
            return self.choose_data_range()


    def choose_column_name(self):
        column_name = input('Please type in column name: ')
        return column_name


    def select_column_data(self):
        return self.data_frame()[self.choose_column_name()].values


    def select_data_by_threshold(self):
        values_for_plot = []
        column_name = self.choose_column_name()
        comparision_sign = self.input_comparision_sign()
        threshold = self.input_threshold()
        for index in range(len(self.data_frame().index)):
            value = self.data_frame().at[index, column_name]
            comparision_function = {"<": op.lt(value, threshold),
                                    "<=": op.le(value, threshold),
                                    "=": op.eq(value, threshold),
                                    ">=": op.ge(value, threshold),
                                    ">": op.gt(value, threshold)}
            if comparision_function[comparision_sign] == True:
                values_for_plot.append(value)
            else:
                pass
        return values_for_plot


    def input_comparision_sign(self):
        comparision_signs = ["<", "<=", "=", ">=", ">"]
        print('\nValues will be compared with threshold as: value [sign] threshold')
        sign = input('Please enter comparision sign: ' )
        if sign in comparision_signs:
            return sign
        else:
            print('Incorrect input.')
            return self.input_comparision_sign()


    def input_threshold(self):
        threshold = input('Please enter threshold: ')
        if threshold.startswith('0,'):
            threshold = threshold.replace('0,', '0.')
        if threshold == 'None':
            return True
        elif float(threshold) or int(threshold):
            return float(threshold)
        else:
            print('Incorrect input. ')
            return self.input_threshold()




#     def establishing_number_of_thresholds_on_one_column(self):
#         """
#         takes in an input of a digit
#         :return: int
#         """
#         n = input('Enter number of thresholds on one column: ')
#         if n.isdigit():
#             return int(n)
#         else:
#             print('Incorrect input.')
#             return self.establishing_number_of_thresholds_on_one_column()



# class Histogram(PlotGenerator, PlotStyle):
#
#
#     def plotting_histogram(self):
#         plt.figure('histogram')
#         plt.hist(choosing_values(), choosing_bins(), PlotStyle.choose_plot_style(self))
#         plt.xlabel(Histogram.x_axis_labeling(self))
#         plt.ylabel(Histogram.y_axis_labeling(self))
#         plt.show()
#
#     def choosing_values(self):
#
#
#     def choosing_bins(self):



# class PlotStyle():
#
#     def choose_plot_style(self):
#         plot_style = input('Do you want to customize plot style? y/n: ')
#         if plot_style == 'n':
#             return regular_plot_style()
#         elif plot_style == 'y':
#             return customized_plot_style()
#         else:
#             print('Incorrect input.')
#             return choose_plot_style()
#
#     def regular_plot_style(self):
#         return None
#
#     def customized_plot_style(self):
#
#
#     def x_axis_labeling(self):
#         x_label = input('Type X axis label: ')
#         return x_label
#
#     def y_axis_labeling(self):
#         y_label = input('Type Y axis label: ')
#         return y_label