
def valid_bracket(text):
    correct = True
    stack_trace = []
    array_open = ("(", "{", "<", "[")
    array_close = ( ")", "}", ">", "]")
    value_check = "(){}<>[]"
    for x in text:
        if x in value_check:
            if x in array_open:
                stack_trace.append(x)
            else:
                last_value = stack_trace.pop()
                if x != array_close[array_open.index(last_value)]:
                    correct = False
                    break
    return correct


if __name__ == '__main__':
    assert valid_bracket("(some_data)")
    assert valid_bracket("() [ww]1{}<>")
    assert valid_bracket("< [ ( { })]>")
    assert not valid_bracket("(]")
    assert not valid_bracket("([9)]")