# Define a function to check if a particular allocation is valid or not
def is_valid(allocation, slot, section, classroom):
  # Check if the classroom has already been allocated for the given time slot
  if allocation[slot][classroom] != -1:
    return False

  # Check if the section has already been allocated a classroom for the given time slot
  for c in range(num_classrooms):
    if allocation[slot][c] == section:
      return False

  # Check if the same classroom has been allocated to more than one section within the same time slot
  for s in range(num_slots):
    if allocation[s][classroom] == section and s != slot:
      return False

  # If none of the above conditions are met, the allocation is valid
  return True

# Define a recursive function to find a valid allocation
def allocate_classrooms(allocation, slot, sections):
  # Base case: If all sections have been allocated a classroom, return True
  if len(sections) == 0:
    return True

  # Try allocating a classroom to the current section
  for classroom in range(num_classrooms):
    # Check if the current allocation is valid
    if is_valid(allocation, slot, sections[0], classroom):
      # Allocate the classroom to the current section
      allocation[slot][classroom] = sections[0]

      # Recursively try to allocate classrooms to the remaining sections
      if allocate_classrooms(allocation, slot + 1, sections[1:]):
        return True

      # If the allocation is not successful, backtrack and try a different classroom
      allocation[slot][classroom] = -1

  # If no valid allocation is found, return False
  return False

# Define the main function
def main():
  # Initialize the allocation matrix with all entries set to -1
  allocation = [[-1 for _ in range(num_classrooms)] for _ in range(num_slots)]

  # Call the recursive function to find a valid allocation
  if allocate_classrooms(allocation, 0, sections):
    # Print the timetable
    print("Time Table:")
    print("------------")
    for i, row in enumerate(allocation):
      print(f"Time slot {i + 1}:")
      for j, section in enumerate(row):
        print(f"Classroom {j + 1}: Section {section}, Subject: {subjects[section]}")
  else:
    print("No valid allocation found.")

# Prompt the user to input the number of sections and classrooms
num_sections = int(input("Enter the number of sections: "))
num_classrooms = int(input("Enter the number of classrooms: "))

# Initialize the list of sections and subjects
sections = [i for i in range(num_sections)]
subjects = ["Math", "Physics", "Chemistry", "Biology", "Computer Science"]

# Prompt the user to input the number of time slots
num_slots = int(input("Enter the number of time slots: "))

# Call the main function
main()