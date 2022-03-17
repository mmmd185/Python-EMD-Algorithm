def get_maxima (series):
    Maximas=[]
    #Evaluating from second to the second last point 
    loopSeries=1
    while loopSeries<=series_length-2:
        if ( (current_set[loopSeries] > current_set[loopSeries-1]) and
        (current_set[loopSeries] > current_set[loopSeries+1])  ):
            Maximas.append(current_set[loopSeries])
        loopSeries+=1
    return Maximas

def get_maximaIndices (series):
    Maxima_indices=[]
    #Evaluating from second to the second last point 
    loopSeries=1
    while loopSeries<=series_length-2:
        if ( (current_set[loopSeries] > current_set[loopSeries-1]) and
        (current_set[loopSeries] > current_set[loopSeries+1])  ):
            Maxima_indices.append(loopSeries)
        loopSeries+=1
    return Maxima_indices


def get_minima (series):
    Minimas=[]
    #Evaluating from second to the second last point 
    loopSeries=1
    while loopSeries<=series_length-2:
        if ( (current_set[loopSeries] < current_set[loopSeries-1]) and
        (current_set[loopSeries] < current_set[loopSeries+1])  ):
            Minimas.append(current_set[loopSeries])
        loopSeries+=1
    return Minimas


def get_minimaIndices (series):
    Minima_indices=[]
    #Evaluating from second to the second last point 
    loopSeries=1
    while loopSeries<=series_length-2:
        if ( (current_set[loopSeries] < current_set[loopSeries-1]) and
        (current_set[loopSeries] < current_set[loopSeries+1])  ):
            Minima_indices.append(loopSeries)
        loopSeries+=1
    return Minima_indices






    



