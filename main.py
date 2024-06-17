import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from tkinter import filedialog
import os
import load_data



default_dir = os.getcwd()
file_selection = filedialog.askopenfilename(initialdir=default_dir)

indirect_categories = ['HLDY', 'ENGM', 'MACC', 'PJM', 'PTVP']

df, project, indirect = load_data.data_loading(file_selection)

project_grouped = project.groupby('Project ID')['Total Cost'].sum()

graph_series_proj = project_grouped.loc[project_grouped > 5000]

s2_proj = pd.Series([project_grouped.loc[project_grouped <= 5000].sum()], index=['Other'])

final_proj = pd.concat([graph_series_proj, s2_proj])

print(final_proj)

patches, labels, pct_texts = plt.pie(x=final_proj, autopct=load_data.make_autopct(final_proj), labels=final_proj.index,
             radius=1.25, rotatelabels=True)
for label, pct_text in zip(labels, pct_texts):
    pct_text.set_rotation(label.get_rotation())

plt.show()


indirect_grouped = indirect.groupby('Indirect Code')['Total Cost'].sum()

graph_series_ind = indirect_grouped.loc[indirect_grouped.index.isin(indirect_categories)]

s2_ind = pd.Series(indirect_grouped.loc[~indirect_grouped.index.isin(indirect_categories)].sum(), index=['Other'])

final_ind = pd.concat([graph_series_ind, s2_ind])

print(indirect_grouped)

patches2, labels2, pct_texts2 = plt.pie(x=final_ind, autopct=load_data.make_autopct(final_ind),
                                        labels=final_ind.index, radius=1.25, rotatelabels=True)
for label, pct_text in zip(labels2, pct_texts2):
    pct_text.set_rotation(label.get_rotation())

plt.show()
