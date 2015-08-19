# -*- coding: utf-8 -*-
from plone.app.robotframework.testing import REMOTE_LIBRARY_BUNDLE_FIXTURE
from plone.app.testing import applyProfile
from plone.app.testing import FunctionalTesting
from plone.app.testing import IntegrationTesting
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import PloneSandboxLayer
from plone.testing import z2

import d11.hermes


class D11HermesLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        self.loadZCML(package=d11.hermes)

    def setUpPloneSite(self, portal):
        applyProfile(portal, 'd11.hermes:default')


D11_HERMES_FIXTURE = D11HermesLayer()


D11_HERMES_INTEGRATION_TESTING = IntegrationTesting(
    bases=(D11_HERMES_FIXTURE,),
    name='D11HermesLayer:IntegrationTesting'
)


D11_HERMES_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(D11_HERMES_FIXTURE,),
    name='D11HermesLayer:FunctionalTesting'
)


D11_HERMES_ACCEPTANCE_TESTING = FunctionalTesting(
    bases=(
        D11_HERMES_FIXTURE,
        REMOTE_LIBRARY_BUNDLE_FIXTURE,
        z2.ZSERVER_FIXTURE
    ),
    name='D11HermesLayer:AcceptanceTesting'
)
