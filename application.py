class myApp():
    accounts = {}
    
    def reset(self):
        self.accounts = {}
        
    def balance(self, account_id):
        #TODO: Check if account_id is valid (not None)

        if account_id in self.accounts:
            return str(self.accounts[account_id])
        
        return None
    
    def deposit(self, account_id, amount):
        #TODO: Check if account_id is valid (not None)

        if account_id in self.accounts:
            self.accounts[account_id] += amount
        else:
            self.accounts[account_id] = amount

        return {
            "destination": {
                "id": account_id,
                "balance": self.accounts[account_id]
            }
        }
    
    def withdraw(self, account_id, amount):
        if account_id not in self.accounts:
            return None

        #TODO: Check if account has necessary amount
        self.accounts[account_id] -= amount

        return {
            "origin": {
                "id": account_id,
                "balance": self.accounts[account_id]
            }
        }
        
    def transfer(self, origin, destination, amount):
        # TODO: Use transaction
        origin = self.withdraw(account_id=origin, amount=amount)
        destination = self.deposit(account_id=destination, amount=amount)

        if origin is None or destination is None:
            return None

        response = {
            "origin": origin["origin"],
            "destination": destination["destination"]
        }
        return response
        
    def event(self, data):
        origin = data.get('origin', None)
        destination = data.get('destination', None)

        match data.pop('type', None):
            case 'deposit':
                return self.deposit(account_id=destination, amount=data['amount'])
            case 'withdraw':
                return self.withdraw(account_id=origin, amount=data['amount'])
            case 'transfer':
                return self.transfer(**data)
            case _:
                return None
