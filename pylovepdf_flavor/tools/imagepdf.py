from pylovepdf_flavor.task import Task


class Imagepdf(Task):

    def __init__(self, public_key, verify_ssl, proxies):

        self.orientation = 'portrait'
        self.margin = 0
        self.pagesize = 'fit'
        self.merge_after = True

        self.tool = 'imagepdf'
        super(Imagepdf, self).__init__(public_key, True, verify_ssl, proxies)

    @property
    def allowed_properties(self):

        return 'orientation', 'margin', 'pagesize', 'merge_after'

    @property
    def pagesize_values(self):
        return 'fit', 'A4', 'letter'

    def process(self):

        payload = super(Imagepdf, self).process()
        payload = self.as_dict(payload, self.allowed_properties)

        return payload






