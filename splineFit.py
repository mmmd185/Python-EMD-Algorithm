from scipy import interpolate
def splinefit (dataset,indices,length,kis=3):
    #converting data into MATRICES 

    # creating y vector
    y = dataset
    x = indices
    xnew=list(range(1,length+1))
    print(len(xnew))
    
    tck = interpolate.splrep(x, y, k=kis)   #uncomment for spline interpolation
    ynew = interpolate.splev(xnew, tck, der=0) #uncomment it for cubic interpol


    #ynew = interpolate.interp1d(x, y, kind='cubic', bounds_error=0,fill_value=None)(xnew)
    #plt.figure()
    #plt.plot(xnew, ynew, 'r')
    #plt.show(block=False)

    
    return ynew
