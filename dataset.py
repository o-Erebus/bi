import csv
import random
from faker import Faker

# Initialize Faker for realistic fake data
fake = Faker()

# Number of rows to generate
num_rows = 120  # you can change to any number >100

# Output CSV filename
output_file = 'synthetic_data.csv'

# Define column headers
headers = ['Employee_ID', 'Name', 'Age', 'Department', 'Salary', 'Join_Date']

# Define possible departments
departments = ['Sales', 'Marketing', 'HR', 'Finance', 'IT', 'Operations']

# Open CSV file for writing
with open(output_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(headers)  # write header row
    
    for emp_id in range(1, num_rows + 1):
        name = fake.name()
        age = random.randint(22, 60)
        department = random.choice(departments)
        salary = round(random.uniform(30000, 120000), 2)
        join_date = fake.date_between(start_date='-10y', end_date='today')
        
        # Write the row
        writer.writerow([emp_id, name, age, department, salary, join_date])

print(f"CSV file '{output_file}' with {num_rows} rows generated successfully.")