

class Algorithm():

  def __init__(self, data, rep):
    self.representation = rep() # A Representation object which MUST match the actual representation the data is stored in (maybe have validation?).
    self.data = data # The algorithm itself. This can take the form of a file or an object, but it must be consistent with the representation (i.e. self.representation.req_type == self.data.type())

  """Prints the data to stdout in a human-readable representation if possible, as plaintext export if not. User facing version of Representation.print().
  """
  def print(self):
    self.representation.print(self.data)
    print('in algo.print')

  """Exports the data in the format sepcified. User facing version of Representation.export().

  Params:
    format: desired format of the exported data (plaintext file by default).

  Returns:
    filename of exported data.
  """
  def export(self, format='text'):
    return self.representation.export(self.data, format)
