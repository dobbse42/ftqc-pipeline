
import abstract_representation
import qualtran

class Qualtran_Representation(abstract_representation.AbstractRepresentation):

  def __init__(self):
#    self.export_formats = ['text']
    pass

  def export_formats(self):
    return ['text']

  def export(self, data, format='text'):
    qualtran.drawing.show_bloq(data)
    return 'text'

  def print(self, data):
    self.export(data, format='text')
    return 0
