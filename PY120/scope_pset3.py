class Cat:
    def get_name(self):
        try:
            return self.name
        except AttributeError:
            return 'Name not set!'

print(Cat().get_name()) # 'Name not set!'
