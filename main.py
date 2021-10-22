import pytest
import requests

url_ddg = "https://api.duckduckgo.com/?q=presidents+of+the+united+states&format=json"
presidents = [" Washington", " Adams", " Jefferson", " Madison", " Monroe", " Adams", " Jackson", " Buren",
              " Harrison", " Tyler", " Polk", " Taylor", " Fillmore", " Pierce", " Buchanan", " Lincoln",
              " Johnson", " Grant", " Hayes", " Garfield", " Arthur", " Cleveland", " Harrison", " Cleveland",
              " McKinley", " Roosevelt", " Taft", " Wilson", " Harding", " Coolidge", " Hoover", " Roosevelt",
              " Truman", " Eisenhower", " Kennedy", " Johnson", " Nixon", " Ford", " Carter", " Reagan", " Bush",
              " Clinton", " Obama", " Trump", " Biden"]


def test_ddg0():
    resp = requests.get(url_ddg + "/?q=DuckDuckGo&format=json")
    rsp_data = resp.json()
    for x in presidents: 
        assert x in str(rsp_data)
