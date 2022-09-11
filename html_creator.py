file = open('roster.csv')

for line in file:
	line = line.split(',')
	rank = line[0]
	last_name = line[1]
	first_name = line[2]
	phone_number = line[3].strip()
	print(f'''<tr>
    <td>{rank}</td>
    <td>{last_name}</td>
    <td>{first_name}</td>
    <td>{phone_number}</td>
</tr>''')