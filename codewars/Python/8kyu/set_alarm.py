# set_alarm.py

# author: awakenedhaki

def set_alarm(employed: bool, vacation: bool) -> bool:
    '''
    Determine if alarm should be set.
    '''
    return (employed and not vacation)
