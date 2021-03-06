##
# This file is part of Muon.
#
# Muon is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Muon is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Muon. If not, see <http://www.gnu.org/licenses/>.
##

import json
import os

class ConfigurationException(Exception):
    pass # meh

class Configuration:
    FILE = "~/.muon.json"
    def __init__(self):
        self.fpath = os.path.expanduser(self.FILE)

        if os.path.isfile(self.fpath):
            # file exists, lets read the data on it.
            self.config_file = open(self.fpath, "r")
            self.data = json.loads(self.config_file.read())
            self.config_file.close()
        
        else:
            self.config_file = open(self.fpath, "w") # w will create the file
            self.data = {}
            self.config_file.write(json.dumps(self.data))
            self.config_file.close()
        
        self.config_file = None # protection - palce holder    
        self.type = type(self.data)

    def __add__(self, value):
        if self.type in [list]:
            self.value.__add__(value)
        else:
            raise AttributeError
    
    def __contains__(self, key):
        """ dict.__contains__(key) -> True if dict has a key key, else False """
        return key in self.data

    def __delitem__(self, key):
        """ x.__delitem__(y) <==> del x[y] """
        del self.data[key]

    def __eq__(self, other):
        return other == self.data
    
    def __ge__(self, other):
        return self.data >= other
    
    def __getitem__(self, key):
        return self.data.__getitem__(key)
    
    def __gt__(self, other):
        return self.data > other

    def iadd(self, value):
        if self.type in [list]:
            self.data += value    
        else:
            raise AttributeError
    def imul(self, value):
        if self.type in [list]:
            self.data *= value
        else:
            raise AttributeError

    def __iter__():
        return self.data.__iter()

    def __le__(self, other):
        return self.data <= other
    
    def __len__(self):
        return len(self.data)
    
    def __lt__(self, other):
        return self.data < other

    def __mul__(self, other):
        if self.type in [lists]:
            return self.data * other
        else:
            raise AttributeError
    
    def __ne__(self, other):
        return self.data != other
    
    def __repr__(self):
        return repr(self.data)

    def __reversed__(self):
        if self.type in [list]:
            return self.data[::-1]
        else:
            raise AttributeError

    def __rmul__(self, other):
        if self.type in [list]:
            return n * self.data
        else:
            raise AttributeError

    def __setitems__(self, key, value):
        if type(value) in [list, dict]:
            value = ChildItem(value)
        self.data[key] = value
        self.save()
   
    def __sizeof__(self):
        # this isn't strictly right but *shrugs*
        return self.data.__sizeof__()

    def clear(self):
        if self.data in [dict]:
            return self.data.clear()
        else:
            raise AttributeError

    def copy(self):
        return self.data.copy()

    def count(self, value):
        if self.type in [self.ListType]:
            return self.data.count(value)
        else:
            raise AttributeError

    def fromkeys(self, other, value=None):
        if self.type in [dict]:
            return self.data.fromkeys(other, value)
        else:
            raise AttributeError
    
    def get(self, key, data=None):
        if self.type in [dict]:
            return self.data.get(key, data)
        else:
            raise AttributeError

    def index(self, value, start=0, stop=None):
        if self.type in [list]:
            return self.data.index(value, start, stop)
        else:
            raise AttributeError

    def insert(self, index, value):
        if self.type in [list]:
            return self.data.insert(index, value)
        else:
            raise AttributeError

    def items(self):
        if self.type in [dict]:
            return self.data.items()
        else:
            raise AttributeError

    def keys(self):
        if self.type in [dict]:
            return self.data.keys()
        else:
            raise AttributeError

    def pop(self, key, *d):
        return self.data.pop(key, d)

    def popitem(self, key, value):
        if self.type in [dicts]:
            return self.data.popitem(key, value)
        else:
            raise AttributeError

    def setdefault(self, key, default):
        if self.type in [dict]:
            return self.setdefault(key, default)
        else:
            raise AttributeError

    def update(self, e, **f):
        if self.type in [dict]:
            return self.data.update(e, f)
        else:
            raise AttributeError
    
    def values(self):
        if self.type in [dict]:
            return self.data.values()
        else:
            raise AttributeError

    def save(self):
        """ Saves the config file back """
        if not self.config_file:
            self.config_file = open(self.fpath, "w")
            self.config_file.write(
                            json.dumps(
                                self.data, 
                                sort_keys=True,
                                indent=4,
                                separators=(',', ': ')))

            self.config_file.close()
            self.config_file = None
        else:
            raise ConfigurationException()
    
class ChildItem(Configuration):
    
    def __init__(self, value, parent=None):
        self.data = value
        self.type = type(value)
        self.parent = parent

    def save(self):
        if None == parent:
            raise ConfigurationError("No parent on child")
        super(Configuration, self.parent).save()

# produce effectively a singleton
configuration = Configuration()
