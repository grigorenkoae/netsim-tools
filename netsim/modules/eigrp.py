#
# IS-IS transformation module
#
from box import Box

from . import _Module

class EIGRP(_Module):

  def node_post_transform(self, node: Box, topology: Box) -> None:
    self.set_af_flag(node,node.eigrp)
