def balancedBrackets(string):
    st = []
    for bracket in string:
        if bracket not  in "([{}])":
            continue
        if bracket in "([{":
            st.append(bracket)
        else:
            if not st:
                return False
            open_bracket = st.pop()
            if  not ((open_bracket == '(' and bracket == ')') \
                    or (open_bracket == '{' and bracket == '}') \
                    or (open_bracket == '[' and bracket == ']')):
                return False

    return not st


print(balancedBrackets("([])(){}(())()()"))
