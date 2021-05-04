import pandas as pd
from pandas import DataFrame

fi_data = {
    "1Y":[0.67],
    "3Y":[0.982],
    "5Y":[1.311],
    "10Y":[1.791],
}

fi_data_df = DataFrame(fi_data)

fi_curve = {
    ["1Y",0.67],
    ["2Y",],
    ["3Y",0.982],
    ["3Y",],
    ["5Y",1.311],
    ["6Y",],
    ["7Y",],
    ["8Y",],
    ["9Y",],
    ["10Y",1.791],
}
print(fi_data_df)