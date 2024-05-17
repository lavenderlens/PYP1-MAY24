file_contents = """\
1234,smith     ,500.0
2345,jones     ,-150.0
3456,wilson    ,2000.0
4567,thompson  ,275.0
5678,davis     ,100
"""
# ETL transformations comprise much of the work done by string methods
# Extract, Transform, Load

accounts = {}

lines = file_contents.split("\n")
print(lines)
for line in lines:
    if line != "":
        parts = line.split(",")
        # print(parts[2])#testing
        acc_num = int(parts[0])
        acc_name = parts[1].strip().title()
        # print(acc_name)#testing
        acc_balance = float(parts[2])
        accounts.setdefault(acc_num, {
            "number" : acc_num,
            "name" : acc_name,
            "balance" : acc_balance,
        })
        # print(accounts)#testing

# exit for loop
for account in accounts:
    print(account)#default is to print dict KEYS ONLY
for account in accounts.values():
    print(account)#this is better

