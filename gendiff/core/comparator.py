def compare(dict1: dict, dict2: dict) -> str:
    res = "{\n"
    values = list()
    keys = sorted(set(list(dict1.keys()) + list(dict2.keys())))
    for key in keys:
        if key in dict1 and key in dict2:
            if dict1[key] != dict2[key]:
                values.append("- {}: {}\n".format(key, dict1[key]))
                values.append("+ {}: {}\n".format(key, dict2[key]))
            else:
                values.append("  {}: {}\n".format(key, dict1[key]))
        elif key in dict1:
            values.append("- {}: {}\n".format(key, dict1[key]))
        else:
            values.append("+ {}: {}\n".format(key, dict2[key]))
    res += "  " + "  ".join(values)
    res += "}"
    return res
