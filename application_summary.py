import csv

with open("applications.csv", newline="", encoding="utf-8-sig") as file:
    applications = csv.DictReader(file)

    total = 0                         # New: start the counter
    applied = 0
    interview = 0
    rejected = 0
    
    for application in applications:
        #print(application["status"])
        total = total + 1             # New: count this application
        if application["status"] == "Applied":
                    applied = applied + 1
        if application["status"] == "Interview":
                    interview = interview + 1
        if application["status"] == "Rejected":
                    rejected = rejected + 1

    print("Total applications:", total)  # New: print the final count
    print("Applied:", applied)
    print("Interview:", interview)
    print("Rejected:", rejected)
    
    