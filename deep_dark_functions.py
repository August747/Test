from typing import Union, Optional
import lists


def millimeters_to_inches(x: Union[float, int]) -> float:
    """На основе этих данных https://allcalc.ru/converter/millimetry-dyuymy
    осуществляется конвертация. 1 inch = 25.4 mm"""
    inch = x / 25.4
    return inch


def area_of_the_paper(x: Union[list, tuple]) -> str:
    z = millimeters_to_inches(x[1]) * millimeters_to_inches(x[2])
    c = f'Paper {x[0]} has area {z} square inches'
    return c


temp_lambda = list(map(area_of_the_paper, Lists.paper_list))

temp_lambda = list(
    map(lambda x: f'Paper {x[0]} has area {millimeters_to_inches(x[1]) * millimeters_to_inches(x[2])} square inches',
        Lists.paper_list))


def filter_temp(x: str) -> bool:
    return 'A' in x


aaaa = filter(filter_temp, temp_lambda)
