def selection_sort_movies_by_global_rating(movies):
    n = len(movies)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if movies[j].getGlobalRating() > movies[max_idx].getGlobalRating():
                max_idx = j
        if max_idx != i:
            movies[i], movies[max_idx] = movies[max_idx], movies[i]
    return movies

def selection_sort_by_rating_then_global(movies):
    n = len(movies)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            rating_j = movies[j][1]
            rating_max = movies[max_idx][1]

            global_j = movies[j][0].getGlobalRating()
            global_max = movies[max_idx][0].getGlobalRating()

            if (rating_j > rating_max) or (rating_j == rating_max and global_j > global_max):
                max_idx = j

        if max_idx != i:
            movies[i], movies[max_idx] = movies[max_idx], movies[i]
    return(movies)