import psycopg2
import sys

def find_words(min_length, max_length):
  conn = psycopg2.connect(database="tcount", user="postgres", password="siddiqi", host="localhost", port="5432")
  cur = conn.cursor()
  cur.execute("select * from tweetwordcount where count >= " + str(min_length) + " and count <= " + str(max_length) + " order by count")
  records = cur.fetchall()
  conn.commit()
  conn.close()
  return records

if __name__ == '__main__':
  if len(sys.argv) > 1:
    min_length, max_length = sys.argv[1].split(',')
    print find_words(min_length, max_length)
  else:
    print "Please provide input in the form of: python histogram.py 3,5"
