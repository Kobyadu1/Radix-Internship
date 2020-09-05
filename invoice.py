class Invoice:

    def __init__(self,value,number,cent):
        self.value = value
        self.number = number
        self.cent = cent

    def __str__(self):
        return str([self.number,float(self.value/100)])

