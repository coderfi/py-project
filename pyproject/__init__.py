from __future__ import absolute_import
import pkg_resources

pkg_resources.declare_namespace(__name__)

try:
    __version__ = pkg_resources.get_distribution('pyproject').version
except:
    __version__ = '0.0'
