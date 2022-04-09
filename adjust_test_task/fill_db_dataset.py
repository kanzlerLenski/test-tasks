import pandas as pd
from app import db, Dataset

# path to the data for db
PATH = 'data/dataset.csv'


# takes data from the file and inserts it into the db row by row
def fill_db(path):

    df = pd.read_csv(path, encoding='utf-8')

    for i in range(len(df)):
        row = Dataset(date=pd.to_datetime(df['date'][i]).date(),
                      channel=df['channel'][i],
                      country=df['country'][i],
                      os=df['os'][i],
                      impressions=int(df['impressions'][i]),
                      clicks=int(df['clicks'][i]),
                      installs=int(df['installs'][i]),
                      spend=float(df['spend'][i]),
                      revenue=float(df['revenue'][i]),
                      cpi=round(float(df['spend'][i]) / int(df['installs'][i]), 3))
        db.session.add(row)

    db.session.commit()


# create db
db.create_all()

# export data in db
fill_db(PATH)
