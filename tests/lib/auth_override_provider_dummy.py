

def create_auth_override_provider(auth_module, index_urls):
    class DummyAuthOverrideProvider(auth_module.AuthBase):
        def __init__(self, index_urls):
            self.multi_domain_basic_auth = auth_module.MultiDomainBasicAuth(
                    index_urls=index_urls)


        @property
        def index_urls(self):
            return self.multi_domain_basic_auth.index_urls


        @index_urls.setter
        def set_index_urls(self, index_urls):
            self.multi_domain_basic_auth.index_urls = index_urls


        def __call__(self, r):
            return self.multi_domain_basic_auth(r)


    return DummyAuthOverrideProvider(index_urls=index_urls)
