"""
Authentication backend for warehouse packers.
"""

from django.contrib.auth.backends import ModelBackend

from packer_auth import packer


class PackerBackend(ModelBackend):

    def authenticate(self, **kwargs):
        return packer.authenticate(**kwargs)
