"""
USMRT SDK
"""

import requests


class USMART:
    auth = None

    def __init__(self, auth=None):
        if auth is not None:
            if "keyId" not in auth:
                raise Exception("Auth requires keyId")
            if "keySecret" not in auth:
                raise Exception("Auth requires keySecret")

        self.auth = auth

    def request(self, organisation, resource, revision=None):
        url = self.buildURL(organisation, resource, revision)
        
        headers = None
        if self.auth:
            headers = {
                "api-key-id": self.auth.keyId,
                "api-key-secret": self.auth.keySecret
            }
        return requests.get(
            url,
            headers=headers
        )

    def buildURL(self, organisation, resource, revision=None):
        revisionString = revision + "/" if revision else "latest/"
        return "https://api.usmart.io/org/" + organisation + "/" + resource + "/" +\
            revisionString + "urql?limit(10)";
