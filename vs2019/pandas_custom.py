import pandas as pd

def pd_filter_by_col_value(table, col_idx, value, operator="=="):
    ans = None
    if operator == "==":
        ans = table.loc[table.iloc[:,col_idx] == value]
    elif operator == "<=":
        ans = table.loc[table.iloc[:,col_idx] <= value]
    elif operator == ">=":
        ans = table.loc[table.iloc[:,col_idx] >= value]
    elif operator == "<":
        ans = table.loc[table.iloc[:,col_idx] < value]
    elif operator == ">":
        ans = table.loc[table.iloc[:,col_idx] > value]
    elif operator == "!=":
        ans = table.loc[table.iloc[:,col_idx] != value]


    return ans

# Sort by given columns
#
def pd_sort_by(table, idx_array):
    columns_t = table.columns
    array_t = []
    for idx in idx_array:
        array_t.append(columns_t[idx])
    table_sorted = table.sort_values(by=array_t)

    return table_sorted