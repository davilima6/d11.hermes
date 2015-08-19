# -*- coding: utf-8 -*-
"""Setup tests for this package."""
from d11.hermes.testing import D11_HERMES_INTEGRATION_TESTING  # noqa
from plone import api

import unittest


class TestSetup(unittest.TestCase):
    """Test that d11.hermes is properly installed."""

    layer = D11_HERMES_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')

    def test_product_installed(self):
        """Test if d11.hermes is installed with portal_quickinstaller."""
        self.assertTrue(self.installer.isProductInstalled('d11.hermes'))

    def test_browserlayer(self):
        """Test that ID11HermesLayer is registered."""
        from d11.hermes.interfaces import ID11HermesLayer
        from plone.browserlayer import utils
        self.assertIn(ID11HermesLayer, utils.registered_layers())


class TestUninstall(unittest.TestCase):

    layer = D11_HERMES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['d11.hermes'])

    def test_product_uninstalled(self):
        """Test if d11.hermes is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('d11.hermes'))
