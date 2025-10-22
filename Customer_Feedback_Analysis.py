def calculate_positive_percentage(ratings):
    if len(ratings) == 0:
        return 0  
    positive_count = sum(1 for r in ratings if r >= 4)
    percentage = (positive_count / len(ratings)) * 100
    return percentage
n = int(input("Enter number of customer ratings: "))
if n == 0:
    print("No ratings available.")
else:
    ratings = []
    for i in range(n):
        rating = int(input(f"Enter rating {i+1} (1-5): "))
        ratings.append(rating)
    result = calculate_positive_percentage(ratings)
    print(f"Positive Feedback: {result:.1f}%")
