import pandas as pd
import operator as op
import numpy as np
import matplotlib.pyplot as plt


class PlotGenerator(object):

    def __init__(self, filename):
        self.filename = filename

    def data_frame(self):
        return pd.read_csv(str(self.filename))

    # def __getitem__(self, item):
    #     return self.item

    def choose_plot_type(self):
        plot = input('Please select plot type: n\ histogram n\ bar chart n\ linear n\ pie chart:')
        if plot == 'histogram':
            return plt.hist(values, bins)
        elif plot == 'bar chart':
            return plt.bar(x_sequence, y_heights)
        elif plot == 'linear':
            return plt.plot(x_coordinate, y_coordinate)
        elif plot == 'pie chart':
            return plt.pie(wedge_size)
        else:
            return self.choose_plot_type()

    def choose_data_for_plot(self):
        columns = []
        i = 1
        q = 'y'
        while q == 'y':
            columns.append(input('Enter name of column_' + str(i) + ':'))
            q = input('do you want to add more columns? y/n:')
            if q == 'y':
                i+=1
            else:
                q = 'n'
        # print(columns)

    def input_comparision_sign(self, n):
        """
        takes in an input of a string- comparision sign
        establishes comparision sign
        :param n: int
        :return: string or boolean
        """
        sign = input('Please enter comparision sign ' + str(n) + ':')
        if sign == 'None':
            return True
        elif sign == "<" or sign == "<=" or sign == "=" or sign == ">" or sign == ">=":
            return sign
        else:
            print('Incorrect input. ')
            return self.input_comparision_sign(n)

    def input_threshold(self, n):
        """
        takes in an input of a float or integer
        establishes threshold value
        :param n: int
        :return: float or boolean
        """
        threshold = input('Please enter threshold ' + str(n) + ':')
        if threshold.startswith('0,'):
            threshold = threshold.replace('0,', '0.')
        if threshold == 'None':
            return True
        elif float(threshold) or int(threshold):
            return float(threshold)
        else:
            print('Incorrect input. ')
            return self.input_threshold(n)

    def comparing_data(self, a, sign, b):
        """
        takes in two values and comparision sign
        establishes comparision operator function
        :param sign: string
        :param a: float
        :param b: float
        :return: boolean
        """
        if sign == "<":
            return op.lt(a, b)
        elif sign == "<=":
            return op.le(a, b)
        elif sign == "=":
            return op.eq(a, b)
        elif sign == ">":
            return op.gt(a, b)
        elif sign == ">=":
            return op.ge(a, b)
        else:
            return True

    def establishing_number_of_thresholds_on_one_column(self):
        """
        takes in an input of a digit
        :return: int
        """
        n = input('Enter number of thresholds on one column: ')
        if n.isdigit():
            return int(n)
        else:
            print('Incorrect input.')
            return self.establishing_number_of_thresholds_on_one_column()

    # def establishing_sign(self, i):
    #     """
    #
    #     :return: string
    #     """
    #     sign = self.input_comparision_sign(i)
    #     return sign, threshold
    #
    # def establishing_sign_and_threshold(self, i):
    #     """
    #
    #     :return: tuple (string, float)
    #     """
    #     threshold = self.input_threshold(i)
    #     return threshold

    def identify_intervals_convergence(self, n):
        sign_dict = {}
        threshold_dict = {}
        i = 1
        while n != 0:
            sign_dict[i] = self.input_comparision_sign(i)
            threshold_dict[i] = self.input_threshold(i)
            n -= 1
            i += 1
        return

    def create_column_with_values_separated_by_threshold(self, column_name_1, column_name_2):
        """
        :param column_name_1: string
        :param column_name_2: string
        :return: list
        """

        # if self.establishing_number_of_thresholds_on_one_column() > 1:
        #     return self.identify_intervals_convergence(self.establishing_number_of_thresholds_on_one_column())

        sign_1 = self.input_comparision_sign(1)
        threshold_1 = self.input_threshold(1)
        sign_2 = self.input_comparision_sign(2)
        threshold_2 = self.input_threshold(2)
        attachment_time = []

        for i in range(len(self.data_frame().index)):
            if self.comparing_data(sign_1, self.data_frame().at[i, column_name_1], threshold_1) and self.comparing_data(sign_2, self.data_frame().at[i, column_name_1], threshold_2):
                attachment_time.append(self.data_frame().at[i, column_name_2])

        print(attachment_time)
        print(len(attachment_time))





    # def change_column_to_list(self, ):
    #
    # def prepare_plot(self):
    #



    



# prepareARgs()
# preparePlot(prepareList(data), args);
# preparePlot(prepareList(data1), args1);

