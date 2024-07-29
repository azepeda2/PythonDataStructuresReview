class Sample:
    def __init__(self, value):
        self.value = value
    
    def getValue(self):
        return self.value

    def setValue(self, value):
        self.value = value

sampleOne = Sample(1)
sampleTwo = Sample(2)

print("SampleOne:", sampleOne.value)
print("SampleTwo:", sampleTwo.value)