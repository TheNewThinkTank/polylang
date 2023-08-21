from pydantic import BaseModel, validator
# import yaml


class Word(BaseModel):

    part_of_speech: str
    definition: str
    example: str

    @validator('part_of_speech')
    def part_of_speech_case_insensitive(cls, v):
        return v.lower()

    class Config:
        allow_population_by_field_definition = True


"""
# Load YAML data from a file
with open("user.yaml", "r") as f:
    data = yaml.safe_load(f)

# Create a list of User objects from the YAML data
users = []
for item in data:
    user = Word.parse_obj(item)
    users.append(user)

# Sort the list of User objects alphabetically by name
users.sort(key=lambda x: x.name)

# Check for duplicate keys or values in the list of User objects
names = set()
ages = set()
for user in users:
    if user.name in names:
        print(f"Warning: Duplicate name found - {user.name}")
    else:
        names.add(user.name)
    if user.age in ages:
        print(f"Warning: Duplicate age found - {user.age}")
    else:
        ages.add(user.age)

# Print the sorted list of User objects
for user in users:
    print(user.name, user.age)
"""
