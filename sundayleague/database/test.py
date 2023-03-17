from mysql_connection import MySqlConnection

# Instantiate connection object
db = MySqlConnection('localhost', 'SUNDAY_MANAGER_ADMIN', 'SUNDAY_MANAGER_ADMIN', 'sunday_manager')
db.connect()

# Create data
create_query = "INSERT INTO league (league_name, league_id) VALUES (%s, %s)"
create_values = ("Barretts Butchers Sunday Premier", 1)
db.create(create_query, create_values)

# Read data
read_query = "SELECT * FROM league"
result = db.read(read_query)
for row in result:
    print(row)

# Update data    
update_query = "UPDATE league SET league_name = %s WHERE league_id = %s"
update_values = ("Aroma Indian Takeaway Sunday Premier", 1)
db.update(update_query, update_values)

# Delete data
delete_query = "DELETE FROM league WHERE id = %s"
delete_values = (1,)
db.delete(delete_query, delete_values)