import os

# Printing the Environment Variables
print('environment')
print(os.environ)
print('-----')

# Listing Files in the Current Directory
print(os.listdir('.'))
print('-----')

# Reading from ingest_output.txt and writing to enrich_output.txt
with open("enrich_output.txt", "w") as out:
    with open("ingest_output.txt", "r") as f:
        for line in f:
            print(line)
            out.write('enrich: ' + line)
