import cirq
import abstract_representation

class Cirq_Representation(abstract_representation.AbstractRepresentation):

  def __init__(self):
#    self.export_formats = ['text']
    pass

  def export_formats(self):
    return ['text']

  def export(self, data, format='text'):
    cirq.contrib.svg.SVGCircuit(data)
    return 'text'

  def print(self, data):
    self.export(data, format='text')
    return 0
