from tkinter import *

font_family = "Helvetica 15 bold"
red = "#B03737"
blue = "#1F2B8F"
white = "#FAFAFA"
explosive = "#C4C4C4"
american_grey = "#808080"


class CurrencyConverter:
    def __init__(self):
        csa = Tk()
        csa.title("Currency Converter")
        csa.configure(bg=explosive)

        Label(csa, font=font_family, bg=explosive, fg=american_grey,
              text="Amount to Convert").grid(row=1, column=1, sticky=W)

        Label(csa, font=font_family, bg=explosive, fg=american_grey,
              text="Conversion Rate").grid(row=2, column=1, sticky=W)

        Label(csa, font=font_family, bg=explosive, fg=american_grey,
              text="Converted Amount").grid(row=3, column=1, sticky=W)

        self.amounttoConvertVar = StringVar()
        Entry(csa, textvariable=self.amounttoConvertVar,
              justify=RIGHT).grid(row=1, column=2)

        self.conversionRateVar = StringVar()
        Entry(csa, textvariable=self.conversionRateVar,
              justify=RIGHT).grid(row=2, column=2)

        self.convertedAmountVar = StringVar()
        lbl_convertedAmount = Entry(
            csa, textvariable=self.convertedAmountVar, justify=RIGHT).grid(row=3, column=2, sticky=E)

        btnConvertedAmount = Button(csa, text="Convert", font=font_family, bg=blue,
                                    fg=white, command=self.ConvertedAmount).grid(row=4, column=2, sticky=E)

        btndelete_all = Button(csa, text="Clear", font=font_family, bg=red, fg=white,
                               command=self.delete_all).grid(row=4, column=6, padx=25, pady=25, sticky=E)

        csa.mainloop()

    def ConvertedAmount(self):
        amount = float(self.conversionRateVar.get())
        convertedAmountVar = float(self.amounttoConvertVar.get()) * amount
        self.convertedAmountVar.set(format(convertedAmountVar, "10.2f"))

    def delete_all(self):
        self.amounttoConvertVar.set("")
        self.conversionRateVar.set("")
        self.convertedAmountVar.set("")


CurrencyConverter()
