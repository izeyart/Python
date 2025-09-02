class Transaction:
    def __init__(self,amount, note):
        self.amount = amount
        self.note = note
        
class FeeAccount:
    def __init__(self, student):
        self.student = student
        self.transactions = []

    def charge (self, amount, note = "Tuition"):
        self.transactions.append(Transaction(amount, note))
    
    def pay(self, amount, note = "Payment"):
        self.transactions.append(Transaction(amount, note))

    def balance(self):
        return sum(t.amount for t in self.transactions)
