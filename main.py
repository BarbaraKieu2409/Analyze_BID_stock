import os
from src.crawler import *
from src.clean import clean


def main():

    # check data folder is exist
    if not os.path.exists("dataset"):
        os.mkdir("dataset")

    code = "BID"
    df = get_stock_data(code)
    df = clean(df)

    # TODO
    # filter.df
    df_filtered = df.head(1312)

    df_filtered.to_csv(f"dataset/{code}.csv", index=False)


if __name__ == "__main__":
    main()
