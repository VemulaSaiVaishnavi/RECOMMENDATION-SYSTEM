import pandas as pd

data = pd.read_csv("Task4/dataset.csv")
data["category"] = data["category"].str.lower()          #covert to lowercase for comparison
data["type"] = data["type"].str.lower()

category_info = {
    "action": "Movies with fights, heroes, and excitement.",
    "romance": "Love stories and emotional relationships.",
    "animation": "Fun animated stories for all ages.",
    "science": "Science and space related stories.",
    "fantasy": "Magic, imagination, and adventures.",
    "self-help": "Books that improve life and mindset.",
    "mystery": "Suspense and detective stories."
}

print("\n🎬📚 MOVIE & BOOK RECOMMENDATION SYSTEM\n")

print(" Available Categories:\n")
for cat, desc in category_info.items():
    print(f"🔹 {cat.title()}")
    print(f"   ➤ {desc}\n")

user_category = input(" Enter a category from the above given categories: ").strip().lower()

if user_category not in category_info:
    print("\n❌ Invalid category selected.")
    exit()

user_type = input("\n Do you want Movies or Books?? ").strip().lower()

user_type = input("\n Do you want Movies or Books? ").strip().lower()

if user_type in ["movie", "movies"]:
    user_type = "movie"
elif user_type in ["book", "books"]:
    user_type = "book"
else:
    print("\n❌ Please enter either Movie or Book")
    exit()


results = data[
    (data["category"] == user_category) &
    (data["type"] == user_type)
]

print(f"\n✅ Recommended {user_type}s in {user_category} category:\n")

if results.empty:
    print("⚠ No items found for this selection.")
else:
    for i, row in enumerate(results["title"], start=1):
        print(f"{i}. {row}")
