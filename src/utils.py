import yaml


def get_config_params():
    """Opens a yaml config file and loads it.

    Returns:
        Config dictioary
    """
    with open("./config.yaml", "r") as f:
        config = yaml.safe_load(f)
    return config
