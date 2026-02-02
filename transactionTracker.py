def after_transaction(balance,transaction):
    if transaction > 0:
        return balance + transaction
    else:
        if balance >= abs(transaction):
            return balance + transaction
        else:
            return balance
        
    
print(after_transaction(300,-400))