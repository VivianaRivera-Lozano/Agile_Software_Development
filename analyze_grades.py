import pandas as pd 

def calculate_stats(file_name):
    data = pd.read_csv(file_name)
    avg = data["Score"].mean()
    return avg

if __name__ == "__main__":
    avg = calculate_stats("grades.csv")
    print(f"The average grade is {avg}")