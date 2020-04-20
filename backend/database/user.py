from main import db
from dataclasses import dataclass
from datetime import datetime


@dataclass
class User(db.Model):
    __tablename__ = 'user'
    id: str = db.Column(db.String, primary_key=True, autoincrement=False)
    target_weight: float = db.Column(db.Float, nullable=False)
    dob: datetime = db.Column(db.DateTime, nullable=False)
    city: str = db.Column(db.String)
    state: str = db.Column(db.String)

    def insert(self):
        """
        insert()
            inserts a new model into a database
            the model must have a unique name
            the model must have a unique id or null id
            EXAMPLE
                user = User(id=user_id, target_weight=120.3, dob=Date())
                user.insert()
        """
        try:
            db.session.add(self)
            db.session.commit()
        except Exception as e:
            print(e)
            db.session.rollback()
            raise
        finally:
            db.session.close()

    def delete(self):
        """
        delete()
            deletes a new model into a database
            the model must exist in the database
            EXAMPLE
                user = User(id=user_id, target_weight=120.3, dob=Date())
                user.delete()
        """
        db.session.delete(self)
        db.session.commit()
        db.session.close()

    def update(self):
        """
        update()
            updates a new model into a database
            the model must exist in the database
            EXAMPLE
                user = User(id=user_id, target_weight=120.3, dob=Date())
                user.target_weight = 200.5
                user.update()
        """
        try:
            db.session.commit()
        except:
            db.session.rollback()
            raise
        finally:
            db.session.close()
