import api


def main()
    keyword = 'Python' # test input for api, change as you need or have it be a user input parameter.
    results - api.find_movie_by_title(keyword)

    print(f'There are {len(results)} movies found.')
    for r in results:
        print(f"{r.title} with code {r.imdb_code} has score {r.imdb_score}")