# 🎬📚 Recommendation System (Movies & Books)

A simple **Python-based Recommendation System** that suggests **movies or books** based on the user’s selected **category**.  
This project uses **Pandas** and a CSV dataset to generate recommendations through the terminal.

---

### Sample Data:
```csv
title,category,type
Inception,Action,Movie
Avengers,Action,Movie
Titanic,Romance,Movie
Harry Potter,Fantasy,Book
Atomic Habits,Self-Help,Book
Sherlock Holmes,Mystery,Book
```

---

##  Features

-  Category-based recommendations  
-  Supports **Movies & Books**  
-  Simple and beginner-friendly  
-  Uses Pandas for filtering  
-  Clean terminal output  
-  Easy to extend with more data  

---

##  Available Categories

- Action  
- Romance  
- Animation  
- Science  
- Fantasy  
- Self-Help  
- Mystery  

---

##  How the Program Works

1. Loads the dataset using Pandas  
2. Converts text to lowercase for matching  
3. Displays available categories  
4. Takes user input:
   - Category
   - Movie or Book
5. Filters data  
6. Displays recommendations  

---

##  How to Run the Project

### Step 1: Install Pandas
```bash
pip install pandas
```

### Step 2: Run the Program
```bash
python recommender.py
```

---

##  Sample Output

```
🎬📚 MOVIE & BOOK RECOMMENDATION SYSTEM

Available Categories:

🔹 Action
   ➤ Movies with fights, heroes, and excitement.

Enter a category from the above list: fantasy
Do you want Movies or Books? book

 Recommended Books in Fantasy category:

1. Harry Potter
2. The Hobbit
3. Percy Jackson
```

---

## 🛠 Technologies Used

- Python 
- Pandas 
- CSV Dataset
- Command Line Interface

---

##  Future Enhancements

- Add rating-based recommendations
- Build GUI using Tkinter
- Convert to Web App using Flask
- Add user login system
- Increase dataset size

---

##  Author

**Vemula Sai Vaishnavi**  

