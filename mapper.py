import pandas as pd
import ItemDetails


def make_map(filepath):
    df = pd.read_excel(filepath)
    mapping = {}
    weight_row = int(df.loc[1][0].split(" ")[2]) + 6
    for i in range(4, 10000):
        if type(df.loc[i][1]) is float:
            break
        q = df.loc[i][9]
        for j in range(11, 1000000):
            if df.loc[i][j] == 1:
                we = df.loc[weight_row][j]
                wi = df.loc[1 + weight_row][j]
                l = df.loc[2 + weight_row][j]
                h = df.loc[3 + weight_row][j]
                detail = ItemDetails.ItemDetails(q, we, wi, l, h)
                mapping[df.loc[i][1]] = detail
                break
    return mapping
