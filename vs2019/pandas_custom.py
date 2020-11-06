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

def pd_slice_col_by_idx(table, col_idx):
    if type(col_idx) == int:
        col_idx = [col_idx]

    ans = table.iloc[:, col_idx]

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


# Iterate Dataframe with a given user-defined function
#
# df: pandas.Dataframe      Dataframe
# func: function            User-defined function
# rtn: bool                 If this argument is true, this function will pipe 
#   the return values of the user-defined function.
# accumulate: bool          If user-defined function values will be accumulated,
#   this argument must be set to True.
# type: type                Type of the accumulated value. If accumulate setting is 
#   True, the type of the value must be given through this argument.
#
# return:   


def dataframe_iterator(df, func, rtn=True, accumulate=False, type=None):
    """Iterate Dataframe with a given user-defined function.
    
    Arguments
    --------
        df: pandas.Dataframe    
            Dataframe
        func: function          
            User-defined function
        rtn: bool               
            If this argument is true, this function will pipe 
            the return values of the user-defined function.
        accumulate: bool        
            If user-defined function values will be accumulated,
            this argument must be set to True.
        type: type              
            Type of the accumulated value. If accumulate setting is True, 
            the type of the value must be given through this argument.
    """

    if func == None:
        return None

    if rtn == True:

        if accumulate == True:
            if type == int:
                ans_func_list = 0
            elif type == str:
                ans_funct_list = ""
            elif type ==  None:
                return

            ans_funct_list += func(index, row)

        else:
            ans_func_list = []

            for index, row in df.iterrows():
                ans_func = func(index, row)
                ans_func_list.append(ans_func)

        return ans_func_list

    else:
        for index, row in df.iterrows():
            func(index, row)
