from typing import Union

my_list: list[Union[str, int]] = [1, 2, "abc", "tomato"]

my_dict: dict[str, Union[str, int]] = {"name": "lyle", "age": 31}


def func(data: Union[int, str]) -> Union[int, str]:
    pass
