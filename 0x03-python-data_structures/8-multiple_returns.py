#!/usr/bin/python3
def multiple_returns(sentence):
    output = []
    size = len(sentence)
    if size == 0:
        output.append(size)
        output.append("None")
    else:
        output.append(size)
        output.append(sentence[0])
    return (tuple(output))
