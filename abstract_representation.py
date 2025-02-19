import abc

class AbstractRepresentation(abc.ABC):

  @property
  @abc.abstractmethod
  def export_formats(self):
    """List of the formats which data in this representation can be exported in.
    """

  @abc.abstractmethod
  def export(self, data, format = 'text') -> str:
#   assert(format in self.export_formats) # I would like to force this assert statement to be in the implemented function. Not sure how to do this yet.
    """Exports the data in the format specified.

    Params:
      data: data to be exported. Should be in the representation corresponding to this Representation class (validation?).
      format: desired format of the exported data (plaintext file by default).

    Returns:
      filename of exported data.
    """

  @abc.abstractmethod
  def print(self, data):
    """Prints the data to stdout in a human-readable representation if possible, as plaintext export if not.

    Params:
      data: data to be printed.

    Returns:
      none.
    """
