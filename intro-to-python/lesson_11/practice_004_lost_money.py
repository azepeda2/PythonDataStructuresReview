# This dictionary shows the bills each person has in their wallet and how many.
wallets = {
   'tom': {
       5: 2,  #Tom has two $5
       10: 1, # He also has one $10
   },
   'kelly': {
       1: 5
   },
   'joseph': {
       100: 1
   }
}

# Iterate over the wallets and check if each wallet has the 100.
# When you find the 100, print the name of the person that has it.

for name, wallet in wallets.items():
    if 100 in wallet.keys():
        if wallet[100] > 0:
            print(f"{name} has {wallet[100]} $100 bills")