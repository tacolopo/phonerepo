file = open('roster.csv')

lst = []

for line in file:
	line = line.split(',')
	rank = line[0]
	last_name = line[1]
	first_name = line[2]
	phone_number = line[3].strip()
	lst.append(f'\t<tr>\n\t\t<td>{rank}</td>\n\t\t<td>{last_name}</td>\n\t\t<td>{first_name}</td>\n\t\t<td>{phone_number}</td>\n\t</tr>')


print('''<!DOCTYPE html>
<html>
<head>
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/css/bootstrap.min.css">
  <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
  <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.4.1/js/bootstrap.min.js"></script>
</head>
<body>

<div class="container">
  <h2>VMU-2 Phone Roster</h2>
  <div class="table-responsive">          
  <table class="table">
    <thead>
      <tr>
        <th>Rank</th>
        <th>Last</th>
        <th>First</th>
        <th>Number</th>
      </tr>
    </thead>
    <tbody>''')
for item in lst:
	print(item)
print('''\t</tbody>
  </table>
  </div>
</div>

</body>
</html>''')
