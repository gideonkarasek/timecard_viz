import pandas as pd


def data_loading(file_selection):
    column_names = {'LaborDtl_LaborType1': 'Labor Type', 'LaborDtl_IndirectCode1': 'Indirect Code',
                    'LaborDtl_ProjectID1': 'Project ID', 'EmpBasic_FirstName': 'Name', 'EmpBasic_LastName': 'Last Name',
                    'LaborDtl_LaborHrs': 'Hours', 'Calculated_TotalCost': 'Total Cost',
                    'Textbox79': 'Hours Subtotal', 'Textbox80': 'Cost Subtotal', 'Textbox62': 'P/I Hours Subtotal',
                    'Textbox63': 'P/I Cost Subtotal', 'Textbox29': 'Overall Hours Total',
                    'Textbox70': 'Overall Cost Total', 'TotalCost': 'Total Cost'}

    df = pd.read_csv(file_selection)

    df.rename(columns=column_names, inplace=True)

    project = df.loc[df['Labor Type'] == 'P']
    indirect = df.loc[df['Labor Type'] == 'I']

    project.reset_index(drop=True, inplace=True)
    indirect.reset_index(drop=True, inplace=True)

    return df, project, indirect


def make_autopct(values):
    def my_autopct(pct):
        total = sum(values)
        val = int(round(pct*total/100.0))
        return '{p:.2f}%  (${v:d})'.format(p=pct,v=val)
    return my_autopct
