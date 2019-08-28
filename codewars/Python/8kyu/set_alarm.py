# set_alarm.py

__author__ = "awakenedhaki"

def set_alarm(employed: bool, vacation: bool) -> bool:
    """
    Determine whether to set an alarm
    :param employed: bool
    :param vacation: bool
    :return: bool
    """
    return (employed and not vacation)
