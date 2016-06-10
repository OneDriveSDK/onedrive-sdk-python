# -*- coding: utf-8 -*- 
'''
# Copyright (c) 2015 Microsoft Corporation
# 
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
# 
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
# 
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
# 
#  This file was generated and any changes will be overwritten.
'''

from __future__ import unicode_literals
from ..collection_base import CollectionRequestBase, CollectionResponseBase, CollectionPageBase
from ..request_builder_base import RequestBuilderBase
from ..model.permission import Permission
import json

class PermissionsCollectionRequest(CollectionRequestBase):

    def __init__(self, request_url, client, options):
        """Initialize the PermissionsCollectionRequest
        
        Args:
            request_url (str): The url to perform the PermissionsCollectionRequest
                on
            client (:class:`OneDriveClient<onedrivesdk.request.one_drive_client.OneDriveClient>`):
                The client which will be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request
        """
        super(PermissionsCollectionRequest, self).__init__(request_url, client, options)

    def get(self):
        """Gets the PermissionsCollectionPage

        Returns: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The PermissionsCollectionPage
        """
        self.method = "GET"
        collection_response = PermissionsCollectionResponse(json.loads(self.send().content))
        return self._page_from_response(collection_response)


class PermissionsCollectionRequestBuilder(RequestBuilderBase):

    def __getitem__(self, key):
        """Get the PermissionRequestBuilder with the specified key
        
        Args:
            key (str): The key to get a PermissionRequestBuilder for
        
        Returns: 
            :class:`PermissionRequestBuilder<onedrivesdk.request.permission_request_builder.PermissionRequestBuilder>`:
                A PermissionRequestBuilder for that key
        """
        return PermissionRequestBuilder(self.append_to_request_url(str(key)), self._client)

    def request(self, expand=None, select=None, top=None, order_by=None, options=None):
        """Builds the PermissionsCollectionRequest
        
        Args:
            expand (str): Default None, comma-seperated list of relationships
                to expand in the response.
            select (str): Default None, comma-seperated list of properties to
                include in the response.
            top (int): Default None, the number of items to return in a result.
            order_by (str): Default None, comma-seperated list of properties
                that are used to sort the order of items in the response.
            options (list of :class:`Option<onedrivesdk.options.Option>`):
                A list of options to pass into the request. Defaults to None.

        Returns:
            :class:`PermissionsCollectionRequest<onedrivesdk.request.permissions_collection.PermissionsCollectionRequest>`:
                The PermissionsCollectionRequest
        """
        req = PermissionsCollectionRequest(self._request_url, self._client, options)
        req._set_query_options(expand=expand, select=select, top=top, order_by=order_by)
        return req

    def get(self):
        """Gets the PermissionsCollectionPage

        Returns: 
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The PermissionsCollectionPage
        """
        return self.request().get()



class PermissionsCollectionResponse(CollectionResponseBase):

    @property
    def collection_page(self):
        """The collection page stored in the response JSON
        
        Returns:
            :class:`PermissionsCollectionPage<onedrivesdk.request.permissions_collection.PermissionsCollectionPage>`:
                The collection page
        """
        if self._collection_page:
            self._collection_page._prop_list = self._prop_dict["value"]
        else:
            self._collection_page = PermissionsCollectionPage(self._prop_dict["value"])

        return self._collection_page


class PermissionsCollectionPage(CollectionPageBase):

    def __getitem__(self, index):
        """Get the Permission at the index specified
        
        Args:
            index (int): The index of the item to get from the PermissionsCollectionPage

        Returns:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The Permission at the index
        """
        return Permission(self._prop_list[index])

    def permissions(self):
        """Get a generator of Permission within the PermissionsCollectionPage
        
        Yields:
            :class:`Permission<onedrivesdk.model.permission.Permission>`:
                The next Permission in the collection
        """
        for item in self._prop_list:
            yield Permission(item)

    def _init_next_page_request(self, next_page_link, client, options):
        """Initialize the next page request for the PermissionsCollectionPage
        
        Args:
            next_page_link (str): The URL for the next page request
                to be sent to
            client (:class:`OneDriveClient<onedrivesdk.model.one_drive_client.OneDriveClient>`:
                The client to be used for the request
            options (list of :class:`Option<onedrivesdk.options.Option>`:
                A list of options
        """
        self._next_page_request = PermissionsCollectionRequest(next_page_link, client, options)


from ..request.permission_request_builder import PermissionRequestBuilder
