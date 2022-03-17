
def monotonic(x):
    dx= np.diff(x)
    return np.all(dx <= 0) or np.all(dx >= 0)

    '''return check diff are negative or check diff are positive
    return ()'''

 