def load_student_records(file_path):
    records = []
    with open(file_path, 'r') as f:
        for line in f:
            name, score = line.strip().split(',')
            records.append((name, int(score)))
    return records

def compute_average_score(records):
    return sum(score for _, score in records) / len(records)

def get_extreme_scores(records):
    highest = max(records, key=lambda student: student[1])[1]
    lowest = min(records, key=lambda student: student[1])[1]
    top_students = [student for student in records if student[1] == highest]
    bottom_students = [student for student in records if student[1] == lowest]
    return top_students, bottom_students

def categorize_students(records, average):
    above_avg = [student for student in records if student[1] > average]
    below_avg = [student for student in records if student[1] <= average]
    return above_avg, below_avg

def bubble_sort_students(records):
    sorted_list = records[:]
    n = len(sorted_list)
    for i in range(n):
        for j in range(0, n - i - 1):
            if sorted_list[j][1] > sorted_list[j + 1][1]:
                sorted_list[j], sorted_list[j + 1] = sorted_list[j + 1], sorted_list[j]
    return sorted_list

def insertion_sort_students(records):
    sorted_list = records[:]
    for i in range(1, len(sorted_list)):
        current_student = sorted_list[i]
        j = i - 1
        while j >= 0 and current_student[1] < sorted_list[j][1]:
            sorted_list[j + 1] = sorted_list[j]
            j -= 1
        sorted_list[j + 1] = current_student
    return sorted_list

def find_students_with_score(records, score):
    return [student for student in records if student[1] == score]

def iterative_binary_search(records, score):
    left, right = 0, len(records) - 1
    found_students = []
    while left <= right:
        mid = (left + right) // 2
        if records[mid][1] == score:
            # Search to the left
            i = mid
            while i >= 0 and records[i][1] == score:
                found_students.append(records[i])
                i -= 1
            # Search to the right
            i = mid + 1
            while i < len(records) and records[i][1] == score:
                found_students.append(records[i])
                i += 1
            return found_students
        elif records[mid][1] < score:
            left = mid + 1
        else:
            right = mid - 1
    return found_students

def save_results_to_file(file_path, avg, top, bottom, above_avg, below_avg, bubble_sorted, insertion_sorted, linear_results, binary_results):
    with open(file_path, 'w') as f:
        f.write(f"Average Score: {avg:.2f}\n\n")

        f.write("Top Scoring Students:\n")
        f.write("Name\tScore\n")
        for student in top:
            f.write(f"{student[0]}\t{student[1]}\n")
        f.write("\n")

        f.write("Lowest Scoring Students:\n")
        f.write("Name\tScore\n")
        for student in bottom:
            f.write(f"{student[0]}\t{student[1]}\n")
        f.write("\n")

        f.write("Students Above Average:\n")
        f.write("Name\tScore\n")
        for student in above_avg:
            f.write(f"{student[0]}\t{student[1]}\n")
        f.write("\n")

        f.write("Students Below Average:\n")
        f.write("Name\tScore\n")
        for student in below_avg:
            f.write(f"{student[0]}\t{student[1]}\n")
        f.write("\n")

        f.write("Bubble Sorted Students:\n")
        f.write("Name\tScore\n")
        for student in bubble_sorted:
            f.write(f"{student[0]}\t{student[1]}\n")
        f.write("\n")

        f.write("Insertion Sorted Students:\n")
        f.write("Name\tScore\n")
        for student in insertion_sorted:
            f.write(f"{student[0]}\t{student[1]}\n")
        f.write("\n")

        f.write("Linear Search Results:\n")
        f.write("Name\tScore\n")
        if linear_results:
            for student in linear_results:
                f.write(f"{student[0]}\t{student[1]}\n")
        else:
            f.write("No students found with that score.\n")
        f.write("\n")

        f.write("Binary Search Results:\n")
        f.write("Name\tScore\n")
        if binary_results:
            for student in binary_results:
                f.write(f"{student[0]}\t{student[1]}\n")
        else:
            f.write("No students found with that score.\n")

# Main routine
if __name__ == "__main__":
    student_records = load_student_records("02230304.txt")
    average_score = compute_average_score(student_records)
    top_students, bottom_students = get_extreme_scores(student_records)
    above_avg_students, below_avg_students = categorize_students(student_records, average_score)
    bubble_sorted_students = bubble_sort_students(student_records)
    insertion_sorted_students = insertion_sort_students(student_records)

    search_score = int(input("\nEnter the score you want to search for: "))
    linear_search_results = find_students_with_score(student_records, search_score)
    binary_search_results = iterative_binary_search(insertion_sorted_students, search_score)

    save_results_to_file("output.txt", average_score, top_students, bottom_students,
                          above_avg_students, below_avg_students, bubble_sorted_students,
                          insertion_sorted_students, linear_search_results, binary_search_results)

