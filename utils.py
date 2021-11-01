import numpy as np

from kneed import KneeLocator


def cos_similarity(v1, v2):
    n1 = np.linalg.norm(v1)
    n2 = np.linalg.norm(v2)
    return np.dot(v1, v2) / n1 / n2


def compare_word(input, model, vocab_vectors):
    input_vec = model.get_sentence_vector(input)
    return {w: cos_similarity(input_vec, vec) for w, vec in vocab_vectors.items()}


def find_elbow_point(sorted_dict):
    y = list(sorted_dict.values())
    x = range(1, len(y)+1)

    kn = KneeLocator(x, y, curve='convex', direction='decreasing')
    return list(sorted_dict.keys())[:kn.elbow]
