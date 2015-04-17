import PySQLPool
from random import randint
import time
from datetime import datetime
import sys, MySQLdb


"""
Using PySQLPool(wrapper to MySQLDB Python library) in the below MySQL Wrapper class. 
Going with PySQLPool as it provides a MySQL thread pool along with being thread safe
and providing connection locking/management and cursor management.
PySQLPool Installation Details: https://github.com/nerdynick/PySQLPool
PySQLPool Documentation: http://packages.python.org/PySQLPool/
"""

class MySQLWraper:
    def __init__(self, db, host, acct):
        self.db = db
        self.host = host
        self.acct = acct
        self.connection = PySQLPool.getNewConnection(username=self.acct[0], password=self.acct[1], 
                                                     host=self.host, db=self.db)

    # Method to insert one or more records into an SQL Table
    # @param table, name of the table (string)
    # @param template, columns to insert to (comma seperated string)
    # @param values, values to insert (list(records) of list(one record) of strings(column))
    # @return None
    def insert(self, table, template, values, is_print=False):
        #Create appropriate number of (%s, %s) based on template
        val_list = [];
        for i in range(0, template.count(',')+1):
            val_list.append(' %s')
        val_string = ','.join(val_list)
        #Query String
        query_str = 'INSERT INTO ' + table +  template + 'VALUES (' + val_string + ' )'
        try:
            query = PySQLPool.getNewQuery(self.connection)
            query.executeMany(query_str, values)
            PySQLPool.commitPool()
        except MySQLdb.Error, e:
            print "Error(insert) %d: %s" % (e.args[0], e.args[1])
            sys.exit (1)
        if(is_print):
            print 'Last Insert ID:', query.lastInsertID

    # Method to execute select query from an SQL Table
    # @param table, name of the table (string)
    # @param select_fields, MySQL Select field format (comma seperated strings)
    # @param where, MySQL Where clause format (comma seperated strings)
    # @param group_by, MySQL Group By clause format (comma seperated strings)
    # @param group_by, MySQL Order By clause format (comma seperated strings)
    # @param group_by, MySQL Limit clause format (string)
    # @return query results
    def select(self, table, select_fields, where=None, group_by=None, order_by=None, limit=None, 
               is_print=False):
        query_str = 'SELECT ' + str(select_fields) + ' FROM ' + table
        if where is not None:
            query_str = query_str + ' WHERE ' + where
        if group_by is not None:
            query_str = query_str + ' GROUP BY ' + group_by
        if order_by is not None:
            query_str = query_str + ' ORDER BY ' + order_by 
        if limit is not None:
            query_str = query_str + ' LIMIT ' + limit
        #print query_str
        try:
            query = PySQLPool.getNewQuery(self.connection)
            query.Query(query_str)
        except MySQLdb.Error, e:
            print "Error(select) %d: %s" % (e.args[0], e.args[1])
            sys.exit (1)
        if(query.lastError):
            print query.lastError
        if(is_print):
            for row in query.record:
                print row
                #print 'Column Value:', row['real_server'], row['rtt_avg_per_sec']
        return query.record     

#Test Code
time_format = '%Y-%m-%d %H:%M:%S' #.%f
time.strftime(time_format)
n = 1000
SQL_db = MySQLWraper(db = 'hackathon_db', host = '10.24.143.7', acct = ['kp', 'kp'])
template = ' (real_server, rtt_avg_per_sec, pkt_type) '
values = []
for i in range(0,n):         #0 to n-1
    rs = randint(1, 10)      #1 and 10 Inclusive
    pkt_type = randint(1, 4) #1 and 4 Inclusive
    rtt_val = datetime.strptime('2009-03-15 16:31:15', time_format) #.654321
    value = [str(rs), str(rtt_val), str(pkt_type)]
    values.append(value)
#print values

SQL_db.insert(table='input_table_l4_aggregated', template=template, values=values)
SQL_db.select(table='input_table_l4_aggregated', select_fields='real_server, rtt_avg_per_sec', 
              is_print = True)
