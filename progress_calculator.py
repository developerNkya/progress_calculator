import time
import matplotlib.pyplot as plt

def calculate_progress(num_goals_set, num_achievements_attained):
    duration = 3 

    # animation loader
    animation_chars = ['|', '/', '-', '\\']
    
    progress = num_achievements_attained - num_goals_set
    average_progress = (num_achievements_attained / num_goals_set) * 100

    # Animate progress calculation
    print("Calculating progress: ", end='', flush=True)
    start_time = time.time()
    while time.time() - start_time < duration:
        for char in animation_chars:
            print('\b' + char, end='', flush=True)
            time.sleep(0.1)
    print('\b', end='', flush=True)
    
    # Determine progress status
    if progress <= -1:
        return f"Sorry, you are lacking behind!\nAverage Progress: {average_progress:.2f}%"
    elif progress == 0:
        return f"Expectations reached\nAverage Progress: {average_progress:.2f}%"
    elif progress >= 1:
        return f"Keep it up\nAverage Progress: {average_progress:.2f}%"

# user prompts
field = input("Enter the field: ")
num_goals_set = int(input("Enter the number of goals set: "))
num_achievements_attained = int(input("Enter the number of achievements attained: "))

result = calculate_progress(num_goals_set, num_achievements_attained)

print("\nResult:\n", result)

# chart prompt
want_chart = input("Do you want to visualize the progress in a chart? (yes/no): ")

if want_chart.lower() == 'yes':
    categories = ['Goals Set', 'Achievements Attained']
    values = [num_goals_set, num_achievements_attained]

    plt.bar(categories, values)
    plt.xlabel('Categories')
    plt.ylabel('Values')
    plt.title('Progress Overview')
    plt.show()


    save_chart = input("Do you want to save the chart? (yes/no): ")
    if save_chart.lower() == 'yes':
        file_name = input("Enter the file name (with extension, e.g., chart.png): ")
        plt.savefig(file_name)
        print(f"Chart saved as '{file_name}'")
    else:
        print("Chart not saved.")
elif want_chart.lower() == 'no':
    print("Exiting.")
else:
    print("Invalid input.")
