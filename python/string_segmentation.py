def can_segment_string(s, dictionary):
    segments = [(0, 0)]

    while len(segments):
        begin, end = segments.pop()
        i = begin
        j = end + 1

        while j < len(s):
            if s[i:j] in dictionary:
                segments.append((i, j))
                i = j
            j += 1

        if s[i:j] in dictionary:
            return True

    return False


if __name__ == "__main__":
    dictionary = dict()
    dictionary["apple"] = True
    dictionary["pear"] = True
    dictionary["pie"] = True
    print(can_segment_string("appl", dictionary))