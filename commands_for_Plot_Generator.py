from Plot_Generator import PlotGenerator

x = PlotGenerator('765_Track_statistics.csv')

print(x.create_column_with_values_separated_by_threshold('TRACK_DISPLACEMENT', 'TRACK_DURATION'))
