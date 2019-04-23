import ProcessNAEPVariables as var
import pandas as pd

jurisdiction = var.readJurisdiction('NAEP_Variables.xlsx');
xl = pd.ExcelFile('NAEP_Variables.xlsx');
indexSheets = xl.sheet_names;
#print(xl.sheet_names);
print(jurisdiction);
div = "";

for y in range(0,len(indexSheets)):
	div = '';
	f = open(str(indexSheets[y])+'.txt', 'w');

	for x in range(0,len(jurisdiction[indexSheets[y]])):
		div = div + ('<div>' + jurisdiction[indexSheets[y]][x]['label'] + '</div>\n');
	f.write(div);
f.close();