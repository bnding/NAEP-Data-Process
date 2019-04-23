import pandas as pd

def readJurisdiction(file):
	xl = pd.ExcelFile(file);
	indexSheets = len(xl.sheet_names);
	jurisDict = dict();

	for y in range(0,indexSheets):
		tempSheet = [0] * len(xl.parse(y).index);

		for x in range(0,len(xl.parse(y))):
			code = str(xl.parse(y).ix[x,0]);

			if(str(xl.parse(y).ix[x,2]) != 'nan'):
				label = str(xl.parse(y).ix[x,2]);
			else:
				label = str(xl.parse(y).ix[x,1]);

			tempSheet[x] = {'code': code, 'label': label};
		jurisDict.update({xl.sheet_names[y] : tempSheet for z in range(0,len(tempSheet))});

	return jurisDict;
var = readJurisdiction('NAEP_Variables.xlsx');
print(var)