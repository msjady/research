
def get_threshold(X,Y,pic_num_1f,t_path):

    [t1_a,t2_a,t3_a,t4_a,t5_a] = read_file(t_path)

    n2a_a = t1_a - 1
    n2d_a = t2_a + pic_num_1f - 1
    n2f_a = t3_a + pic_num_1f * 2 -1
    n2h_a = t4_a + pic_num_1f * 3 -1
    n2s_a = t5_a + pic_num_1f * 4 -1

    Threshold = [X[n2a_a],X[n2d_a],X[n2f_a],X[n2h_a],X[n2s_a]],[Y[n2a_a],Y[n2d_a],Y[n2f_a],Y[n2h_a],Y[n2s_a]]]

    return(Threshold)

