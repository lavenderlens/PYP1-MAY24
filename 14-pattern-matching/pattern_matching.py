file_contents = """
1234 Credit:
David Smith,500.0
2345 Debit:
Sarah Jones,-150.0
3456 Credit:
Tom Wilson,2000.0
4567 Savings:
Jane Thompson,275.0
5678 Debit:
Simon Davis,100.0
"""

import re

accounts = {}

pattern = '(\d{4}).+\n.+\s(.+),(.+)'
matches = re.findall(pattern, file_contents)
for num, name, bal in matches:
    print(num, name, bal)
print(matches)#testing
for tpl in matches:
        acc_num = int(tpl[0])
        acc_name = tpl[1]
        acc_balance = float(tpl[2])
        accounts.setdefault(acc_num, {
            "number" : acc_num,
            "name" : acc_name,
            "balance" : acc_balance,
        })

for account in accounts.values():
      print(account)