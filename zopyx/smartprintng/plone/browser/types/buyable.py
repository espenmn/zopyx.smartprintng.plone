from ..compatible import InitializeClass
from Products.Five.browser import BrowserView
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile

class BuyableView(BrowserView):
    """ View for bda plone shop, buyable.
        (testing how it works)
    """

    template = ViewPageTemplateFile('buyable.pt')

    def __call__(self, *args, **kw):
        return self.template(self.context)

InitializeClass(BuyableView)

