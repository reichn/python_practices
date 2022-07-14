import xlwings as xw

wb = xw.Book("new.xlsx")
sheet = wb.sheets["Sheet1"]
sheet.range("A1").value = [["Hi 1", "Hi 2", "Hi 3"], [10.0, 20.0, 30.0]]
print(sheet.range("A1").expand().value)
