from .errors import InvalidMeasureError, InvalidValueError, UncompletableMeasuresError


def converter(val, st_unit, end_unit):
    units = {
        'mm': 'length',
        'cm': 'length',
        'm': 'length',
        'km': 'length',

        'g': 'mass',
        'kg': 'mass',

        'c': 'temperature',
        'f': 'temperature',
        'k': 'temperature'
    }

    st_unit = st_unit.lower()
    end_unit = end_unit.lower()

    if val < 0 and st_unit not in ('c', 'f', 'k'):
        raise InvalidValueError()

    if st_unit not in units or end_unit not in units:
        raise InvalidMeasureError()

    if st_unit == end_unit:
            return float(val)

    if units[st_unit] != units[end_unit]:
        raise UncompletableMeasuresError()

    if units[st_unit] == 'length':
        mid_val = val
        if st_unit == 'mm':
            mid_val = 0.001 * val
        elif st_unit == 'cm':
            mid_val = 0.01 * val
        elif st_unit == 'km':
            mid_val = 1000 * val

        if end_unit == 'mm':
            return mid_val * 1000
        elif end_unit == 'cm':
            return mid_val * 100
        elif end_unit == 'km':
            return mid_val * 0.001
        return mid_val

    elif units[st_unit] == 'mass':
        if st_unit == 'g' and end_unit == 'kg':
            return 0.001 * val
        elif st_unit == 'kg' and end_unit == 'g':
            return val * 1000
        return val

    else:
        if st_unit == 'c':
            mid_val = val
        elif st_unit == 'f':
            mid_val = (val - 32) * 5 / 9
        else:
            mid_val = val - 273.15

        if mid_val < -273.15:
            raise InvalidValueError()

        if end_unit == 'c':
            return float(mid_val)
        elif end_unit == 'f':
            return float(mid_val * 9 / 5 + 32)
        else:
            return float(mid_val + 273.15)
    
    



