import csv
import psycopg2

dbname = 'wos_2018'
user = 'username'
password = 'password'
host = 'host'
port = 'port'

conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
cur = conn.cursor()

# create table
cur.execute("""
    CREATE TABLE IF NOT EXISTS cite_title_keyword_organ (
        uid VARCHAR,
        pubyear VARCHAR,
        organ_name VARCHAR,
        cit_ct INT
    )
""")
conn.commit()

organs = []
with open('path_to_your_csv.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        organs.append(row[0])  

# query and insert
for organ in organs:
    words = organ.split()  
    like_clauses_k = ' AND '.join([f"keyword ILIKE '%{word}%'" for word in words])
    like_clauses_t = ' AND '.join([f"title ILIKE '%{word}%'" for word in words])
    like_clauses_kp = ' AND '.join([f"keyword_plus ILIKE '%{word}%'" for word in words])
    sql_query = f"""
    WITH published_papers AS (
        SELECT uid, pubyear
        FROM wos_summary
        WHERE pubyear::integer >= 2018 and pubyear::integer <= 2022
    ),
    organ_match AS (
        SELECT wk.uid
        FROM wos_keywords wk
        WHERE {like_clauses_k}
        union
        SELECT wt.uid
        FROM wos_titles wt
        WHERE {like_clauses_t} and wt.title_type = 'item'
        union
        SELECT wkp.uid
        FROM wos_keywords_plus wkp
        WHERE {like_clauses_kp}
    ),
    cited_papers AS (
        SELECT ref_id, COUNT(DISTINCT uid) AS cit_ct
        FROM wos_references
        GROUP BY ref_id
        HAVING COUNT(DISTINCT uid) >= 10
    )
    SELECT pp.uid, pp.pubyear, '{organ}' AS organ_name, cp.cit_ct
    FROM published_papers pp
    JOIN organ_match om ON pp.uid = om.uid
    JOIN cited_papers cp ON pp.uid = cp.ref_id;
    """
    try:
        cur.execute(sql_query)
        rows = cur.fetchall()
        for row in rows:
            insert_query = "INSERT INTO cite_title_keyword_organ (uid, pubyear, organ_name, cit_ct) VALUES (%s, %s, %s, %s)"
            cur.execute(insert_query, row)
        conn.commit()
    except Exception as e:
        print(f"An error occurred while processing '{organ}': {e}")
        conn.rollback()

# close database
cur.close()
conn.close()
