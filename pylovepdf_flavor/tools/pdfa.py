from pylovepdf_flavor.task import Task


class PdfA(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.tool = 'pdfa'
        self.conformance = 'pdfa-2b'

        super(PdfA, self).__init__(public_key, True, verify_ssl, proxies)

    @property
    def allowed_properties(self):
        return 'conformance',

    @property
    def conformance_values(self):
        return 'pdfa-1b', 'pdfa-1a', 'pdfa-2b', 'pdfa-2u', 'pdfa-2a', 'pdfa-3b', 'pdfa-3u', 'pdfa-3a'

    def process(self):
        payload = super(PdfA, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload




