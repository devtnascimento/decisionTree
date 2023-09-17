import random

# Define the attribute names
attributes = ['request_frequency', 'volume', 'throughput', 'price']

n_lines = 200

# Define the database suggestions for all combinations
model = {
    ("low", "low", "low", "low"): "SQLite",
    ("low", "low", "low", "moderate"): "Apache_Arrow",
    ("low", "low", "low", "high"): "Amazon_Aurora",
    ("low", "low", "high", "low"): "SQLite",
    ("low", "low", "high", "moderate"): "Redis",
    ("high", "low", "high", "low"): "Redis",
    ("low", "low", "high", "high"): "Amazon_Aurora",
    ("high", "low", "high", "high"): "Amazon_Aurora",
    ("high", "high", "low", "low"): "InfluxDB",
    ("high", "low", "low", "low"): "InfluxDB",
    ("high", "high", "low", "moderate"): "CockroachDB",
    ("high", "high", "high", "low"): "CockroachDB",
    ("high", "low", "low", "high"): "CockroachDB",
    ("high", "high", "low", "high"): "Google_Cloud_Spanner",
    ("high", "high", "high", "high"): "Google_Cloud_Spanner",
    ("low", "high", "high", "high"): "Google_Cloud_Spanner",
    ("low", "low", "low", "low"): "SQLite",
    ("low", "low", "low", "moderate"): "Apache_Arrow",
    ("low", "high", "high", "low"): "Apache_Arrow",
    ("low", "high", "low", "low"): "Apache_Arrow",
    ("low", "low", "low", "high"): "SQLite",
    ("low", "low", "high", "low"): "SQLite",
    ("low", "low", "high", "moderate"): "Redis",
    ("low", "low", "high", "high"): "Amazon_Aurora",
    ("low", "high", "low", "high"): "Amazon_Aurora",
    ("high", "high", "low", "low"): "InfluxDB",
    ("high", "high", "low", "moderate"): "CockroachDB",
    ("high", "high", "low", "high"): "Google_Cloud_Spanner",
}

# Generate 50 lines of random attribute values within [0, 1]
data_lines = []
for _ in range(n_lines):
    line = [random.uniform(0, 1) for _ in range(len(attributes))]
    data_lines.append(line)

# Determine suggestions based on the threshold of 0.5
suggestions = []
for line in data_lines:
    suggestion = []
    key_list = []

    # Determine 'request_frequency'
    key_list.append('high' if line[0] >= 0.5 else 'low')

    # Determine 'volume'
    key_list.append('high' if line[1] >= 0.5 else 'low')

    # Determine 'throughput'
    key_list.append('high' if line[2] >= 0.5 else 'low')

    # Determine 'price'
    key_list.append('high' if line[3] >= 0.5 else 'low')

    # Map the entire set of attribute values to the suggestion
    suggestion_key = tuple(key_list)
    model_suggestion = model[suggestion_key]
    suggestion.append(model_suggestion)

    suggestions.append(suggestion)

# print(suggestions)

# Print the generated data and suggestions
for i in range(50):
    print(','.join([str(round(val, 3)) for val in data_lines[i]]) + ',' + ','.join(suggestions[i]))


# Define the attribute names
arff_attr = [
    '@attribute request_frequency numeric',
    '@attribute volume numeric',
    '@attribute throughput numeric',
    '@attribute price numeric',
    '@attribute suggestion {SQLite, Apache_Arrow, Amazon_Aurora, Redis, CockroachDB, Google_Cloud_Spanner, InfluxDB}'
]

# Save the ARFF data to a file
with open('database_suggestions.arff', 'w') as arff_file:
    arff_file.write('@relation Database_Suggestions\n\n')
    arff_file.write('\n'.join(arff_attr))
    arff_file.write('\n\n@data\n')
    for i in range(n_lines):
        arff_file.write(','.join([str(round(val, 3)) for val in data_lines[i]]) + ',' + ','.join(suggestions[i]) + '\n')

print("ARFF file 'database_suggestions.arff' has been generated.")

