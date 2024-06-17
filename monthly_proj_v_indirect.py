import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import filedialog
import os
import load_data

default_dir = os.getcwd()
file_selection = filedialog.askopenfilename(initialdir=default_dir)
month_mapping = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
mapping = {mon: i for i, mon in enumerate(month_mapping)}

combined, project, indirect = load_data.data_loading(file_selection)

combined['Date'] = pd.to_datetime(combined['Clock In Date'], format='%m/%d/%Y')
combined['Month'] = combined['Date'].dt.strftime('%b')
combined['Hours'] = combined['Labor Hrs'].abs()

combined_grouped = combined.groupby(['Month', 'Labor Type'])['Total Cost'].sum().reset_index()

# combined_grouped['Hours %'] = combined_grouped['Overall Cost Total'] / combined_grouped.groupby('Month')['Overall Cost Total'].transform('sum')

print(combined_grouped)

key = combined_grouped['Month'].map(mapping)

sorted_df = combined_grouped.iloc[key.argsort()]

ax = sns.barplot(data=sorted_df, x='Month', y='Total Cost', hue='Labor Type')
# ax.set()
plt.show()
