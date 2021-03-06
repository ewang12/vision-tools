# IBM_PROLOG_BEGIN_TAG
#
# Copyright 2019,2020 IBM International Business Machines Corp.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#           http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or
#  implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
#
#  IBM_PROLOG_END_TAG


class Files:

    def __init__(self, server):
        self.server = server

    def report(self, dsid, **kwargs):
        """ Get a list of all files in the indicated dataset that meet the
        indicated criteria.

        :param dsid -- UUID of dataset containing files
        :param kwargs -- query parameters for `/datasets/{model_id/files`"""

        uri = f"/datasets/{dsid}/files"
        return self.server.get(uri, params=kwargs)

    def upload(self, dsid, file_paths):
        """ Uploads files to the indicated dataset.

        :param dsid -- UUID of target dataset
        :param file_paths -- list of files to upload"""

        files = []
        for filepath in file_paths:
            files.append(('files', open(filepath, 'rb')))

        uri = f"/datasets/{dsid}/files"
        return self.server.post(uri, files=files)

    def action(self, dsid, file_id, **kwargs):
        """ performs the requested action on the given file

        :param dsid -- UUID of the targeted dataset
        :param file_id -- UUID of the targeted file
        :param kwargs -- fields for the payload
                        'action=' is required. Other named parameters
                        depend upon the action requested.
                        see '/datasets/{model_id}/files/{file_id}/action`
                        documentation for details"""

        uri = f"/datasets/{dsid}/files/{file_id}/action"
        return self.server.get(uri, json=kwargs)

    def delete(self, dsid, file_id):
        """ Delete the indicated file from the indicated dataset

        :param dsid -- UUID of the targeted dataset
        :param file_id -- UUID of the targeted file"""

        uri = f"/datasets/{dsid}/files/{file_id}"
        return self.server.delete(uri)

    def show(self, dsid, file_id):
        """ Get details of the indicated file

        :param dsid -- UUID of the targeted dataset
        :param file_id -- UUID of the targeted file"""

        uri = f"/datasets/{dsid}/files/{file_id}"
        return self.server.get(uri)
