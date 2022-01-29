#!/usr/bin/python

import paramiko
import pymysql
import os
import sys
import datetime

## Define
port_n=[9010,9020,9030]


## file save
def f_save(s_data):
  out = open('/Users/juki/Documents/Project_pf/select_data.txt','a')
  print(s_data,file=out)

## file delete
def f_delete():
  os.system('rm /Users/juki/Documents/Project_pf/select_data.txt')


## Upsert SQL
def SQL_upsert():
  conn = pymysql.connect(host='localhost', user='root', password='rjdqb12!@', db='s_check', charset='utf8')
  curs = conn.cursor(pymysql.cursors.DictCursor)

## define data
  for i in range (1,4):
    sid = i
    did = os.popen("cat /Users/juki/Documents/Project_pf/select_data.txt |sed -n '%ip' |sed s/{//g |sed s/}//g |sed s/,//g |awk '{print $2}'"%(i)).read().replace('\n',"")
    host_n = os.popen("cat /Users/juki/Documents/Project_pf/select_data.txt |sed -n '%ip' |sed s/{//g |sed s/}//g |sed s/,//g |awk '{print $4}'"%(i)).read().replace('\n',"")
    cpu = os.popen("cat /Users/juki/Documents/Project_pf/select_data.txt |sed -n '%ip' |sed s/{//g |sed s/}//g |sed s/,//g |awk '{print $6}'"%(i)).read().replace('\n',"")
    mem = os.popen("cat /Users/juki/Documents/Project_pf/select_data.txt |sed -n '%ip' |sed s/{//g |sed s/}//g |sed s/,//g |awk '{print $8}'"%(i)).read().replace('\n',"")
    date_s = os.popen("cat /Users/juki/Documents/Project_pf/select_data.txt |sed -n '%ip' |sed s/{//g |sed s/}//g |awk '{print $10, $11, $12, $13, $14, $15}' |sed s/datetime\.//g"%(i)).read().replace('\n',"")

    date_s = date_s.replace(')',"")
    date_s = date_s.replace(' ',"").split(',')
    Y = date_s[0]
    m = date_s[1]
    d = date_s[2]
    H = date_s[3]
    M = date_s[4]
    S = date_s[5]
    date_s = "%s-%s-%s %s:%s:%s"%(Y,m,d,H,M,S)

## INSERT OLD
    sql = "INSERT IGNORE INTO db_old_state (_id, sid, host_name, cpu, mem, date) VALUES (%s, %s, %s, %s, %s, %s)"
    curs.execute(sql, [did, sid, host_n, cpu, mem, date_s])

## UPDATE NEW
    sql = "UPDATE db_new_state SET _id = %s, sid = %s, cpu = %s, mem = %s, date = %s WHERE host_name = %s"
    curs.execute(sql, [did, sid, cpu, mem, date_s, host_n])

  conn.commit()
  conn.close()
    


## Select and Insert SQL
def SQL_select(d_port):
  conn = pymysql.connect(host='localhost',port=d_port, user='juki', password='rjdqb12!@', db='s_check', charset='utf8')
  curs = conn.cursor(pymysql.cursors.DictCursor)

## get hostname
  sql = "SELECT * FROM `new_state` ORDER BY _id DESC LIMIT 1"
  curs.execute(sql)

  row = curs.fetchone()
  f_save(row)

  conn.close()


## main
def main():
  for i,data in enumerate(port_n):
    d_port = data
    SQL_select(d_port)
  SQL_upsert()


  f_delete()


if __name__ == '__main__':
  main()
