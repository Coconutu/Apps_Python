x='program'
def exterior():
    x='local'
    def interior():
        nonlocal x
        x='nonlocal'
        print(x)
    interior()
    print(x)
exterior()
print(x)
