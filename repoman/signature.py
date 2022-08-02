#!/usr/bin/env python
#
# Copyright 2014 Tuenti Technologies S.L.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import getpass
import socket


class Signature(dict):
    @property
    def user(self):
        return self['user'] if 'user' in self else getpass.getuser()

    @property
    def email(self):
        if 'email' in self:
            return self['email']
        return f"{self.user}@{socket.gethostname()}"

    @property
    def author(self):
        return self['author'] if 'author' in self else self.user

    @property
    def author_email(self):
        return self['author_email'] if 'author_email' in self else self.email

    def __str__(self):
        return f"{self.user} <{self.email}>"
