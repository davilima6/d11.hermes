# -*- coding: utf-8 -*-
from d11.hermes.testing import D11_HERMES_INTEGRATION_TESTING  # noqa
from plone import api
from plone.browserlayer.utils import registered_layers
import unittest

JS = [
    '++resource++d11.hermes/main.js'
]

CSS = [
    '++resource++d11.hermes/main.css'
]


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

    def test_jsregistry(self):
        resource_ids = self.portal.portal_javascripts.getResourceIds()
        for id in JS:
            self.assertIn(id, resource_ids, '{0} not installed'.format(id))

    def test_resources_available(self):
        resources = CSS + JS
        for id in resources:
            res = self.portal.restrictedTraverse(id)
            self.assertTrue(res)


class TestUninstall(unittest.TestCase):

    layer = D11_HERMES_INTEGRATION_TESTING

    def setUp(self):
        self.portal = self.layer['portal']
        self.installer = api.portal.get_tool('portal_quickinstaller')
        self.installer.uninstallProducts(['d11.hermes'])

    def test_product_uninstalled(self):
        """Test if d11.hermes is cleanly uninstalled."""
        self.assertFalse(self.installer.isProductInstalled('d11.hermes'))

    def test_addon_layer_removed(self):
        layers = [l.getName() for l in registered_layers()]
        self.assertNotIn('ID11HermesLayer', layers)

    def test_jsregistry_removed(self):
        resource_ids = self.portal.portal_javascripts.getResourceIds()
        for id in JS:
            self.assertNotIn(id, resource_ids, '{0} not removed'.format(id))

    def test_cssregistry_removed(self):
        resource_ids = self.portal.portal_css.getResourceIds()
        for id in CSS:
            self.assertNotIn(id, resource_ids, '{0} not removed'.format(id))
