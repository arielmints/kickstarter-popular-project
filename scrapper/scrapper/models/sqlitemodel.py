from peewee import *
import datetime

db = SqliteDatabase('../../../db.sqlite3') # connecting to the sqlite db file in the upper directory of the django project

class top_projects_topprojects(Model):
    projects_json = TextField()
    date_updated = DateTimeField()

    class Meta:
        database = db
