import xlrd
#import pandas
#from sklearn import tree
loc = ("TestingBook.xlsx")
wb = xlrd.open_workbook(loc)
sheet = wb.sheet_by_index(0)

#print (sheet.cell_value(0,0)) #reads in A1
#print(sheet.ncols) 
#print(sheet.nrows) 
for i in range(sheet.ncols): 
	print(sheet.cell_value(0, i)) 