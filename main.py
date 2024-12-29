import medical_data_visualizer
from unittest import main

# Test your function by calling it here
medical_data_visualizer.draw_cat_plot()
medical_data_visualizer.draw_heat_map()

# Run unit tests automatically
main(module='test_module', exit=False)

'''import pandas as pd
import matplotlib.pyplot as plt
from medical_data_visualizer import draw_cat_plot, draw_heat_map, create_cat_plot_data, create_heatmap_data


df = pd.read_csv("C:/Users/SAM-Tech/Desktop/freecode camp/medical_data_visualizer/medical_examination.csv")

df_cat = create_cat_plot_data(df)
df_heat = create_heatmap_data(df)


cat_fig = draw_cat_plot(df_cat)
cat_fig.show()


heatmap_fig = draw_heat_map(df_heat)
heatmap_fig.show()'''


