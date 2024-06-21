import numpy as np


def parse(dataset: np.ndarray, onset: list[int], name: str, measurement: str,
          x_axis: tuple[str, str, list[any]]) -> dict:
    parsed_dict = {"name": name.split(' ')[0].lower(),
                   "longname": name,
                   "n_obs": dataset.size,
                   "n_dim": 1}

    if onset is not None:
        parsed_dict["demo"] = {'true_CPs': onset}

    parsed_dict["time"] = {
        "type": x_axis[0],
        "format": x_axis[1],
        "index": list(range(len(x_axis[2]))),
        "raw": x_axis[2]
    }
    parsed_dict["series"] = {
        "label": measurement,
        "type": "int",
        "raw": list(dataset)

    }

    return parsed_dict
