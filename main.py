import pandas as pd
import yaml

# Load the YAML file
with open('windows-index.yaml', 'r',encoding="utf-8") as file:
    data = yaml.safe_load(file)

# Create an empty DataFrame
df = pd.DataFrame(columns=['Tactic', 'Technique', 'Attack Command'])

# Iterate over the data
for tactic, values in data.items():
    for key, value in values.items():
        technique = value['technique']['name']
        for test in value.get('atomic_tests', []):
            command = test.get('executor', {}).get('command', '')
            new_row = pd.DataFrame({'Tactic': [tactic], 'Technique': [technique], 'Attack Command': [command]})
            df = pd.concat([df, new_row], ignore_index=True)

# Print the DataFrame
print(df)
