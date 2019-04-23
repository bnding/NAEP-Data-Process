import pandas as pd

def readJurisdiction(file):

	# for x in range(len(xl.parse(0).columns))
	xl = pd.ExcelFile(file);
	national = [0]*(len(xl.parse(0).index));
	states = [0]*(len(xl.parse(1).index));
	districts = [0]*(len(xl.parse(2).index));
	statTypes = [0]*(len(xl.parse(3).index));

	for x in range(0,len(xl.parse(0))):
		code = xl.parse(0).iloc[x,0];
		label = xl.parse(0).iloc[x,1];
		national[x] = {'code': code, 'label': label};

	for x in range(0,len(xl.parse(1))):
		code = xl.parse(1).iloc[x,0];
		label = xl.parse(1).iloc[x,1];
		states[x] = {'code': code, 'label': label};

	for x in range(0,len(xl.parse(2))):
		code = xl.parse(2).iloc[x,0];
		label = xl.parse(2).iloc[x,1];
		districts[x] = {'code': code, 'label': label};

	for x in range(0,len(xl.parse(3))):
		code = xl.parse(3).iloc[x,0];
		label = xl.parse(3).iloc[x,1];
		statTypes[x] = {'code': code, 'label': label};

	return national;

#print(readJurisdiction("NAEP_Variables.xlsx"));

#keys are code and label. have single associative array with two keys {code: AP, label: At or Above Proficient}