def selection_sort_movies_by_rating(movies):
    n = len(movies)
    for i in range(n):
        max_idx = i
        for j in range(i + 1, n):
            if movies[j].getGlobalRating() > movies[max_idx].getGlobalRating():
                max_idx = j
        if max_idx != i:
            movies[i], movies[max_idx] = movies[max_idx], movies[i]
    return movies