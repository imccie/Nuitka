#     Copyright 2012, Kay Hayen, mailto:kayhayen@gmx.de
#
#     Python tests originally created or extracted from other peoples work. The
#     parts were too small to be protected.
#
#     Licensed under the Apache License, Version 2.0 (the "License");
#     you may not use this file except in compliance with the License.
#     You may obtain a copy of the License at
#
#        http://www.apache.org/licenses/LICENSE-2.0
#
#     Unless required by applicable law or agreed to in writing, software
#     distributed under the License is distributed on an "AS IS" BASIS,
#     WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#     See the License for the specific language governing permissions and
#     limitations under the License.
#

x = 0

class MyContextManager:
    def __enter__( self ):
        global x
        x += 1

        print "Entered context manager", x

        return x

    def __exit__( self, exc_type, exc_value, traceback ):
        print exc_type, exc_value, traceback

        return False

with MyContextManager() as x:
    print "x has become", x

try:
    with MyContextManager() as x:
        print "x has become", x

        raise Exception( "Lalala" )
        print x
except Exception, e:
    print e

class NonContextManager1:
    def __enter__( self ):
        return self

class NonContextManager2:
    def __exit__( self ):
        return self

try:
    with NonContextManager1() as x:
        print x
except Exception, e:
    print e

try:
    with NonContextManager2() as x:
        print x
except Exception, e:
    print e

class NotAtAllContextManager:
    pass

try:
    with NotAtAllContextManager() as x:
        print x
except Exception, e:
    print e
