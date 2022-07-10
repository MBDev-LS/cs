d = [
			{
				"dept": "Liaison Committee (Commons)",
				"position": "Member",
				"from_date": "2020-05-20",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Panel of Chairs",
				"position": "Member",
				"from_date": "2020-01-15",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Speaker's Committee for the Independent Parliamentary Standards Authority",
				"position": "Member",
				"from_date": "2020-01-16",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Members Estimate Committee",
				"position": "Member",
				"from_date": "2020-03-18",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Administration Committee",
				"position": "Chair",
				"from_date": "2020-03-18",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Administration Committee",
				"position": "Chair",
				"from_date": "2020-03-18",
				"to_date": "9999-12-31"
			},
			{
				"dept": "House of Commons Commission",
				"position": "Member",
				"from_date": "2020-03-18",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Administration Estimate Audit and Risk Assurance Committee",
				"position": "Member",
				"from_date": "2020-05-19",
				"to_date": "9999-12-31"
			},
			{
				"dept": "Members Estimate Audit Committee",
				"position": "Member",
				"from_date": "2020-05-19",
				"to_date": "9999-12-31"
			}
		]

isPayroll = False
for office in d:
	if 'Committee' not in office['dept'] and 'speaker' not in office['dept'].lower() and office['dept'] != 'Panel of Chairs': 
		print(office['dept'])
		isPayroll = True
		break

print(isPayroll)