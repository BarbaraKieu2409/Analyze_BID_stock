import requests
from bs4 import BeautifulSoup
import pandas as pd


def get_stock_data(code):
    url = f"https://vinacorp.vn/trade-history/{code}"
    response = requests.get(url)

    if response.status_code != 200:
        raise Exception(f"failed to fetch data for code {code}")

    soup = BeautifulSoup(response.content, "html.parser")
    table = soup.find("table", id="myTable2")

    if not table:
        raise Exception(f"Table not found for code {code}")
    rows = table.find_all("tr")

    data = []
    for row in rows:
        columns = row.find_all("td")
        if columns:
            ngày = columns[0].text.strip()
            đóng_cửa = columns[1].text.strip()
            thay_đổi = columns[2].text.strip()
            phần_trăm = columns[3].text.strip()
            Mở_cửa = columns[4].text.strip()
            Cao_nhất = columns[5].text.strip()
            Thấp_nhất = columns[6].text.strip()
            Tổng_KLGD = columns[7].text.strip()
            Tổng_GTGD = columns[8].text.strip()

            data.append(
                {
                    "ngày": ngày,
                    "đóng_cửa": đóng_cửa,
                    "thay_đổi": thay_đổi,
                    "phần_trăm": phần_trăm,
                    "Mở_cửa": Mở_cửa,
                    "Cao_nhất": Cao_nhất,
                    "Thấp_nhất": Thấp_nhất,
                    "Tổng_KLGD": Tổng_KLGD,
                    "Tổng_GTGD": Tổng_GTGD,
                }
            )

    df = pd.DataFrame(data)
    return df


# # Ví dụ sử dụng:
# code = "BID"
# df = get_stock_data(code)
# print(df)
