def to_human_dur(secons:int) -> str:
    hours = secons//3600
    ost = secons%3600
    min = ost//60
    sec = ost%60
    array_present = []
    if hours > 0:
        array_present.append("{} {}".format(hours, "hour" if (hours == 1) else "hours"))
    if min > 0:
        array_present.append("{}{} {}".format(", " if hours > 0 else "",min, "minute" if (min == 1) else "minutes"))
    if sec > 0:
        array_present.append("{}{} {}".format(" and " if min > 0 else "",sec,"second" if (sec == 1) else "seconds"))

    return "".join(array_present)
    


if __name__ == '__main__':
    assert to_human_dur(1) == '1 second'
    assert to_human_dur(62) == '1 minute and 2 seconds'
    assert to_human_dur(3600) == '1 hour'
    assert to_human_dur(3662) == '1 hour, 1 minute and 2 seconds'
    