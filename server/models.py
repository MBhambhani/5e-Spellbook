from app import db
from sqlalchemy.dialects.postgresql import JSON

class Spell(db.Model):
  __tablename__ = 'spells'

  id = db.Column(db.Integer, primary_key=True)
  name = db.Column(db.String())
  ritual = db.Column(db.Boolean())
  concentration = db.Column(db.Boolean())
  school = db.Column(db.String())
  casting_time = db.Column(db.String())
  components = db.Column(db.String())
  spell_range = db.Column(db.String())
  duration = db.Column(db.String())
  material = db.Column(db.String())
  desc = db.Column(db.Text())
  bard = db.Column(db.Boolean())
  cleric = db.Column(db.Boolean())
  druid = db.Column(db.Boolean())
  paladin = db.Column(db.Boolean())
  ranger = db.Column(db.Boolean())
  sorcerer = db.Column(db.Boolean())
  warlock = db.Column(db.Boolean())
  wizard = db.Column(db.Boolean())
  level = db.Column(db.Integer())

  def __int__(self, name, ritual, concentration, school, casting_time,
    components, spell_range, duration, material, desc, bard, cleric,
    druid, paladin, ranger, sorcerer, warlock, wizard, level):
    self.name = name
    self.ritual = ritual
    self.concentration = concentration
    self.school = school
    self.casting_time = casting_time
    self.components = components
    self.spell_range = spell_range
    self.duration = duration
    self.material = material
    self.desc = desc
    self.bard = bard
    self.cleric = cleric
    self.druid = druid
    self.paladin = paladin
    self.ranger = ranger
    self.sorcerer = sorcerer
    self.warlock = warlock
    self.wizard = wizard
    self.level = level
  
  def __repr__(self):
    return '<id {}>'.format(self.id)
  
  def serialize(self):
    return {
      'id': self.id,
      'name': self.name,
      'ritual': self.ritual,
      'concentration': self.concentration,
      'school': self.school,
      'casting_time': self.casting_time,
      'components': self.components,
      'spell_range': self.spell_range,
      'duration': self.duration,
      'material': self.material,
      'desc': self.desc,
      'bard': self.bard,
      'cleric': self.cleric,
      'druid': self.druid,
      'paladin': self.paladin,
      'ranger': self.ranger,
      'sorcerer': self.sorcerer,
      'warlock': self.warlock,
      'wizard': self.wizard,
      'level': self.level
    }