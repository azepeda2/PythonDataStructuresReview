"""
Now that you can use a constructor, modify your Printer class so you can
pass the brand, model and paper capacity. Create an instance for each
of the following models:

   Brand       Model       Capacity
   HP          7955e       125 sheets
   Brother     HL-L2310D   250 sheets
   Canon       G4270       100 sheets

Add a print_document() instance method that receives a string and prints
it out. The printout should include the brand and model of the printer.
"""

class Printer:
    def __init__(self, brand, model, capacity):
        self.Brand = brand
        self.Model = model
        self.Capacity = capacity
    def notifu_low_ink(self):
        print("Ink is low")

    def notify_low_paper(self):
        print("Paper is low")

    def print_document(self, str):
        print(str)
        print(f"Brand: {self.Brand} Model: {self.Model}")

printer = Printer("Brother", "2360dw", 50)
printer.notify_low_paper()
printer.notifu_low_ink()
printer.print_document("Lorem ipsum")