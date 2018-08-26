


def read_file(filename):
    f = open(filename,"r")
    threshold = f.read().split(sep = " ")
    threshold_int = [int(s) for s in threshold]
    #print(threshold_int)
    return threshold_int