from tkinter import filedialog
import os
import load_data
import pandas as pd

default_dir = os.getcwd()
file_selection = filedialog.askopenfilename(initialdir=default_dir)

combined, project, indirect = load_data.data_loading(file_selection)

project_grouped = project.groupby('Project ID')['Hours'].sum()
indirect_grouped = indirect.groupby('Indirect Code')['Hours'].sum()

project_grouped.to_csv('project_grouped.csv')
indirect_grouped.to_csv('indirect_grouped.csv')
