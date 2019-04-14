from scipy import sparse
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
from datetime import datetime
import os


def m_usertorating(list_file):
    ratings_tmp = {}

    mov_r = {}
    for file in list_file:
        start_file_read = datetime.now()
        with open('C:/Users/amedge/Downloads/netflix-prize-data/{}'.format(file)) as test:
            for line in test:
                if line[-2] == ":":
                    j = int(line[0:len(line) - 2])
                    ratings_tmp = {}
                else:
                    ratings_tmp.update({int(line.split(",")[0]): int(line.split(",")[1])})
                    mov_r.update({j: ratings_tmp})
        end_file_read = datetime.now()
        print('done with {} file in {}'.format(file, (end_file_read - start_file_read)))
    print("For Movie: 3455 ---> {}".format(mov_r[3455]))
    return mov_r


if not os.path.isfile("all_data_sparse_matrix.npz"):
    print("Loading all data....")
    start_load = datetime.now()
    combined_data_df = pd.read_csv('C:/Users/amedge/Desktop/Project/netflix-prize-test/combined_data.csv', names=[
        'movie', 'user', 'rating', 'date'], sep=",")
    end_load = datetime.now()
    print("Loading complete in: {}".format(end_load - start_load))

    print("Creating Sparse Matrix....")
    start_sparse = datetime.now()
    training_sparse_matrix = sparse.csr_matrix((combined_data_df.rating.values, (combined_data_df.user.values,
                                                                                 combined_data_df.movie.values)), )
    end_sparse = datetime.now()
    print("Created sparse matrix in time: {}, The shape is: {}".format((end_sparse - start_sparse),
                                                                       training_sparse_matrix.shape))
    sparse.save_npz("all_data_sparse_matrix.npz", training_sparse_matrix)
    print("Saved Sparse Matrix!")
elif not os.path.isfile("movie_movie_similarity.npz"):
    print("Loading sparse matrix...")
    training_sparse_matrix = sparse.load_npz("all_data_sparse_matrix.npz")
    start_sim_calc = datetime.now()
    movie_movie_similarity = cosine_similarity(X=training_sparse_matrix.T, dense_output=False)
    end_sim_calc = datetime.now()

    sparse.save_npz("movie_movie_similarity.npz", movie_movie_similarity)
    print("Saved Movie Movie Similarity Matrix on the disk. Calculation Finished in: {}".format(
        end_sim_calc - start_sim_calc))

m_m_sim_matrix = sparse.load_npz("movie_movie_similarity.npz")
print("Movie Movie similarity matrix has a shape: {}".format(m_m_sim_matrix.shape))

start_dict_creation = datetime.now()
dictionary = m_usertorating(['combined_data_1.txt', 'combined_data_2.txt', 'combined_data_3.txt', 'combined_data_4.txt'])
end_dict_creation = datetime.now()
print("Time for creating entire dictionary: {}".format(end_dict_creation - start_dict_creation))

