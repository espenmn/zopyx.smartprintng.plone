################################################################
# zopyx.smartprintng.plone
# (C) 2011,  ZOPYX Limited & Co. KG, D-72070 Tuebingen, Germany
################################################################

import os

from ..compatible import InitializeClass
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from zopyx.smartprintng.plone.browser.pdf import PDFView

cwd = os.path.dirname(os.path.abspath(__file__))

# Integration with the PFG script adapter requires a script like this:

# view = context.restrictedTraverse('@@asPFGPDF')
# pdf =  view()
# R = context.REQUEST.RESPONSE
# R.setHeader('content-type', 'application/pdf')
# R.setHeader('content-length', len(pdf))
# R.setHeader('content-disposition', 'attachment; filename=output.pdf')
# R.write(pdf)


class PDFView(PDFView):
    """ Integration with PloneFormGen script adapter """

    template = ViewPageTemplateFile('resources_bc/pdf_template.pt')
    transformations = ('makeImagesLocal',
                      )

InitializeClass(PDFView)
