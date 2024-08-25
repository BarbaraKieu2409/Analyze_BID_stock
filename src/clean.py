import pandas as pd
import numpy as np

from datetime import datetime

# convert date dtype to datetime


def clean(df):
    df["ngày"] = pd.to_datetime(df["ngày"], dayfirst=True, errors="coerce")

    # fix string ở thay đổi
    # thay_đổi = str(thay_đổi)
    cleaned_str = (
        df["thay_đổi"]
        .str.replace("\n▲", "")
        .str.replace("\n■■", "")
        .str.replace("\n▼", "")
    )
    # cleaned_str = thay_đổi.replace(',', '').replace('+', '').replace('■■', '').strip()
    df["thay_đổi"] = pd.to_numeric(cleaned_str)

    # convert dtypes
    # convert column from object to float

    df["đóng_cửa"] = df["đóng_cửa"].str.replace(",", "").astype(float)
    df["phần_trăm"] = df["phần_trăm"].str.replace(",", "").astype(float)
    df["Mở_cửa"] = df["Mở_cửa"].str.replace(",", "").astype(float)
    df["Cao_nhất"] = df["Cao_nhất"].str.replace(",", "").astype(float)
    df["Thấp_nhất"] = df["Thấp_nhất"].str.replace(",", "").astype(float)
    df["Tổng_KLGD"] = df["Tổng_KLGD"].str.replace(",", "").astype(float)
    df["Tổng_GTGD"] = df["Tổng_GTGD"].str.replace(",", "").astype(float)

    # filter day
    end = datetime.now()
    start = datetime(end.year - 5, end.month, end.day)

    df[df["ngày"] > f"{start.year}-{start.month}-{start.day}"]

    return df
