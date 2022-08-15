from extensions import db

status = ("DEACTIVE", "ACTIVE")

class Sample(db.Document):
  dateUpload = db.DateField()
  dateCreate = db.DateField()

  @classmethod
  def output(cls):
    return {
      "id": str(cls.pk),
      "dateUpload": cls.dateUpload
    }
