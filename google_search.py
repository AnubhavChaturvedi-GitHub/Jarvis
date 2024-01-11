from googlesearch import search


def google_search(query, num_results=5):
    try:
        results = list(search(query, num_results=num_results, stop=num_results, pause=2))
        return results
    except Exception as e:
        print("Error:", e)
        return []


if __name__ == "__main__":
    query = input("Enter your Google search query: ")

    search_results = google_search(query)

    if search_results:
        print("\nSearch Results:")
        for idx, result in enumerate(search_results, start=1):
            print(f"{idx}. {result}")
    else:
        print("No search results.")
