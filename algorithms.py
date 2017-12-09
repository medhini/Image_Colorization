import numpy as np
import pyflann as pf


def ann_index(A_pyramid, Ap_pyramid, level = 5):
    A_feature = compute_features(A_pyramid)
    Ap_feature = compute_features(Ap_pyramid)

    flann = [pf.FLANN() for _ in xrange(level)]
    flann_params = [list([]) for _ in xrange(level)]
    s = [list([]) for _ in xrange(level)]
    s_size = [list([]) for _ in xrange(level)]

    for l in range(level):
        print('Building index for level %d / %d' % (l, level))
        
        s_tmp = []
        s_tmp.append(np.hstack([A_feature[l], Ap_feature[l]]))

        s[l] = np.vstack(s_tmp)
        s_size[l] = s[i].shape

        flann_params[l] = flann[l].build_index(s[l], algorithm'kdtree')
    return flann, flann_params, s, s_size



def best_approximate_match(flann, params, BBp_feature):
    result, dists = flann.nn_index(BBp_feature, 1, checks=params['checks'])
    return result[0]