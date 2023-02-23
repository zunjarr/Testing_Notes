import pandas as pd


def read_data():
    try:
        df_csv = pd.read_csv('C:\\Users\\dorugzu\\practice_project\\test_data\\test_data.csv', )
        df = pd.DataFrame(df_csv)
        return df
    except Exception as e:
        print(e)
