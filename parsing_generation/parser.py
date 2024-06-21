import numpy as np


def parse(dataset: np.ndarray, onset: list[int], name: str, measurement: str,
          x_axis: tuple[str, str, list[any]]) -> dict[str, any]:
    """
        Returns the dataset parsed into a dict to be turned into json.

        Parameters:
           dataset (ndarray): the dataset to be parsed.
           onset (list[int]): the onsets of the dataset if known for demo purposes.
           name (str): the name of the dataset.
           measurement (str): the measurement of the dataset.
           x_axis (tuple[str, str, list[any]]): information on the X axis of the dataset.
            In order Type (str), Format (str), Raw_Values (list[any])

        Returns:
            parsed_dict (dict[str, any): The parsed dict to be turned into json.
        """

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
        "type": "float",
        "raw": [x.item() for x in dataset]

    }

    return parsed_dict
