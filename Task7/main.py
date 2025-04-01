tree = (
    {"GN", "ELM", 1988},
    {"GN", "ELM", 2003},
    {"GN", "ELM", 1974, 1972},
    {"GN", "ELM", 1974, 2015},
    {"GN", "REXX", 'YANG'},
    {"GN", "REXX", 'P4', 1988},
    {"GN", "REXX", 'P4', 2003},
    {"GN", "REXX", 'P4', 1974},
    {"TEXT"},
    {"PERL", "ELM"},
    {"PERL", "REXX"}
)


def main(data):
    s1 = set(data)
    for i, v in enumerate(tree):
        if not (v - s1):
            return i
    return -1
