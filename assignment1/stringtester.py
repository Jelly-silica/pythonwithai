class StringOperator:
    def tester(self, givenstring="Too short"):  
        if len(givenstring) < 10:
            print("Too short")
        else:
            print(givenstring)

if __name__ == "__main__":
    stringTester = StringOperator()
    stringTester.tester()  