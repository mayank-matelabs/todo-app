from flask_appbuilder import Model
from sqlalchemy import Column, Integer, String, ForeignKey, Date

class Todo(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(150), nullable=False)
    description = Column(String(150), nullable=True)
    due_date = Column(Date, index=True)

    def __repr__(self):
        return self.name