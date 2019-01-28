#!/usr/bin/python
#This script can print all the data from database and can be used as a getter
import psycopg2
import psycopg2.extras
import sys
import rospy 
 
def main():
	# Connect to an existing database
	conn = psycopg2.connect("dbname = testdb user = willow password = willow")

	# Open a cursor to perform database operations
	cur = conn.cursor()

	# Query the database and obtain data as Python objects
	query = "SELECT * FROM lidarData;"
	cur.execute(query)
	row = cur.fetchall()
	#for rows in row:
		#print "   ", rows[0]
	print row[-1]

	# Make the changes to the database persistent
	conn.commit()

	# Close communication with the database
	cur.close()
	conn.close()
	return row

if __name__ == "__main__":
	main()