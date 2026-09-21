workers = [{
    "name" :  input("Enter worker's name: "),
    "employee_id" : input("Enter worker's employee ID: "),
    "hourly_wage" : float(input("Enter worker's hourly wage: "))
}]

paycheck = workers[0]["hourly_wage"] * 40

withholding = paycheck * 0.2
net_pay = paycheck - withholding

with open("paychecks.txt", "w") as paychecks_file:
    quit = input("Enter 'q' to quit or any other key to continue: ")
    while quit.lower() != "q":
        workers.append({
            "name" :  input("Enter worker's name: "),
            "employee_id" : input("Enter worker's employee ID: "),
            "hourly_wage" : float(input("Enter worker's hourly wage: "))
        })
        quit = input("Enter 'q' to quit or any other key to continue: ")

    for worker in workers:
        for key, value in workers.items():
            paychecks_file.write(f"{key}: {value}\n")
            