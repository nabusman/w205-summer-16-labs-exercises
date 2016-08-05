import psycopg2
import sys

def return_counts(word=None):
  conn = psycopg2.connect(database="tcount", user="postgres", password="siddiqi", host="localhost", port="5432")
  cur = conn.cursor()
  if word == None:
    cur.execute("select * from tweetwordcount order by word")
    records = cur.fetchall()
    result = records
  else:
    cur.execute("select * from tweetwordcount where word='" + word + "'")
    records = cur.fetchall()
    result = records[0][1]
  conn.commit()
  conn.close()
  return result

if __name__ == '__main__':
  if len(sys.argv) > 1:
    print return_counts(sys.argv[1])
  else:
    print return_counts()
