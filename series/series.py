def slices(series, length):
    if length > 0 and len(series) >= length:
        result = []
        start = 0
        end = length
        while(end <= len(series)):
            result.append(series[start:end])
            start += 1
            end += 1
        return result
    else:
        raise ValueError("Impossible to find series of length %d in sequence of length %d" % (
            length, len(series)))
