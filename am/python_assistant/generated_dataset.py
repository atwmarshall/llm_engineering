import random

# Sample flower types and colors
flower_types = ['sunflower', 'rose', 'daisy', 'tulip', 'lily', 'orchid']
colors = ['yellow', 'red', 'white', 'pink', 'purple', 'orange']

# Function to generate sample data
def generate_flower_data(num_records):
    data = []
    for _ in range(num_records):
        flower_present = random.choice([True, False])
        if flower_present:
            flower_data = {
                'flower': flower_present,
                'flower_type': random.choice(flower_types),
                'colour': random.choice(colors)
            }
        else:
            flower_data = {
                'flower': flower_present,
                'flower_type': 'n/a',
                'colour': 'n/a'
            }
        data.append(flower_data)
    return data

# Generate 100 records of sample data
sample_flower_data = generate_flower_data(100)

# Example output
for record in sample_flower_data[:10]:  # Displaying first 10 records
    print(record)

print(len(sample_flower_data))
