import pandas as pd
import operator as op
import numpy as np
import matplotlib.pyplot as plt

df1 = pd.read_csv('765_Track_statistics.csv')


class PlotGenerator(object):

    def __init__(self, filename):
        self.filename = filename

    def __str__(self):
        return str(self.filename)

    def data_frame(self):
        df1 = pd.read_csv(self.__str__())
        return df1

    def input_comparision_sign(self, n):
        sign = input('Please enter comparision sign ' + str(n) + ':')
        if sign == "<" or sign == "<=" or sign == "=" or sign == ">" or sign == ">=":
            return sign
        else:
            print('Incorrect input. ')
            return self.input_comparision_sign(n)

    def input_threshold(self, n):
        threshold = input('Please enter threshold ' + str(n) + ':')
        if float(threshold):
            return float(threshold)
        elif threshold == 'None':
            return True
        else:
            print('Incorrect input. ')
            return self.input_threshold(n)

    def comparing_data(self, sign, a, b):
        if sign == "<":
            print('done')
            return op.lt(a, b)
        elif sign == "<=":
            return op.le(a, b)
        elif sign == "=":
            return op.eq(a, b)
        elif sign == ">":
            return op.gt(a, b)
        elif sign == ">=":
            return op.ge(a, b)

    def create_column_with_values_separated_by_threshold(self, column_name_1, column_name_2):
        """
        :param column_name_1: string
        :param column_name_2: string
        :return: list
        """
        sign_1 = self.input_comparision_sign(1)
        threshold_1 = self.input_threshold(1)
        sign_2 = self.input_comparision_sign(2)
        threshold_2 = self.input_threshold(2)
        attachment_time = []

        for i in range(len(df1.index)):
            if self.comparing_data(sign_1, df1.at[i, column_name_1], threshold_1) and self.comparing_data(sign_2, df1.at[i, column_name_1], threshold_2):
                attachment_time.append(df1.at[i, column_name_2])
                print(attachment_time)


    # def change_column_to_list(self, ):
    #
    # def prepare_plot(self):
    #



# prepareARgs()
# preparePlot(prepareList(data), args);
# preparePlot(prepareList(data1), args1);