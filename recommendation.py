
users = {
    "Rahul": {
        "KGF": 5,
        "Pushpa": 4,
        "Bahubali": 5
    },

    "Anu": {
        "KGF": 5,
        "Pushpa": 5,
        "Avatar": 4
    },

    "Ravi": {
        "Bahubali": 5,
        "Interstellar": 4,
        "Avatar": 5
    }
}

print("=== Movie Recommendation System ===")

name = input("Enter user name (Rahul/Anu/Ravi): ")

if name in users:

    watched = users[name]

    recommendations = []

    for other_user in users:

        if other_user != name:

            for movie in users[other_user]:

                if movie not in watched:

                    recommendations.append(movie)

    recommendations = list(set(recommendations))

    print("\nRecommended Movies:")
    
    for movie in recommendations:
        print("-", movie)

else:
    print("User not found")
