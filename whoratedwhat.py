from datetime import datetime

FILE_PATH = "C:/Users/amedge/Downloads/netflix-prize-data/{}"


# sorted_similarities = []
# movie_user_mapping = {}
# ideal_k = 20
# threshold = 70


def find_if_rated(similar_movies_matrix, movie_user_mapping, ideal_k, threshold):
    predictions = []
    actual = []

    with open(FILE_PATH.format("wrw_binary.txt")) as wrw_preds:
        lines = wrw_preds.read().splitlines()
        actual.append(lines)

    print("Working on Who Rated What? ....")
    start_program = datetime.now()

    with open(FILE_PATH.format("who_rated_what_2006.txt")) as who_rated_what:
        for line in who_rated_what:
            match_count = 0
            movie_id = line.strip().split(",")[1]
            user_id = line.strip().split(",")[0]

            similar_movies_for_movie_id = similar_movies_matrix[movie_id].toarray().ravel()
            sorted_similar_movies = similar_movies_for_movie_id.argsort()[::-1][1:]
            # print("Sorted Similarities: {}".format(sorted(similar_movies_for_movie_id, reverse=True)))
            # print("Sorted Similar Movies: {}".format(sorted_similar_movies))
            similar_movies = sorted_similar_movies[1:ideal_k + 1]
            for movie in similar_movies:
                # print("Mapping : {}".format(movie_user_mapping[movie]))
                if int(user_id) in list(movie_user_mapping[movie].keys()):
                    match_count += 1
            if ((match_count / ideal_k) * 100) >= threshold:
                predictions.append("1")
                # print("Match count: {}, Value: {}".format(match_count, ((match_count / ideal_k) * 100)))
                # print("User: {} will rate the movie {} ----> 1".format(user_id, movie_id))
            else:
                predictions.append("0")
                # print("Match count: {}, Value: {}".format(match_count, ((match_count / ideal_k) * 100)))
                # print("User: {} won't rate the movie {} ----> 0".format(user_id, movie_id))
    end_program = datetime.now()
    print("Mission Accomplished in {}".format(end_program - start_program))
