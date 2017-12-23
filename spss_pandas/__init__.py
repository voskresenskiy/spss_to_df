from rpy2.robjects import r, pandas2ri
from rpy2.robjects.packages import importr

foreign = importr('foreign')

def sav_to_pandas(fn):
    r_df = foreign.read_spss(fn,
                            use_value_labels = True,
                            to_data_frame = True)
    py_df = pandas2ri.ri2py(r_df)
    return py_df