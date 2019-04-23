import ProcessNAEPVariables as var
import pandas as pd
import json

def var2JSON(jurisdiction):
	labels = var.readJurisdiction('NAEP_Variables.xlsx');
	xl = pd.ExcelFile('NAEP_Variables.xlsx');
	indexSheets = xl.sheet_names;
	order = [jurisdiction];
	juris = [];

	for x in range(0, len(order)):
		juris = juris + labels[order[x]];
	return json.dumps(juris);

json = var2JSON("Subject");
print(json);