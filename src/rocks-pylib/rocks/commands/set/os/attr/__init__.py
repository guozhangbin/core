# $Id: __init__.py,v 1.11 2012/11/27 00:48:30 phil Exp $
#
# @Copyright@
# 
# 				Rocks(r)
# 		         www.rocksclusters.org
# 		         version 6.2 (SideWinder)
# 		         version 7.0 (Manzanita)
# 
# Copyright (c) 2000 - 2017 The Regents of the University of California.
# All rights reserved.	
# 
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are
# met:
# 
# 1. Redistributions of source code must retain the above copyright
# notice, this list of conditions and the following disclaimer.
# 
# 2. Redistributions in binary form must reproduce the above copyright
# notice unmodified and in its entirety, this list of conditions and the
# following disclaimer in the documentation and/or other materials provided 
# with the distribution.
# 
# 3. All advertising and press materials, printed or electronic, mentioning
# features or use of this software must display the following acknowledgement: 
# 
# 	"This product includes software developed by the Rocks(r)
# 	Cluster Group at the San Diego Supercomputer Center at the
# 	University of California, San Diego and its contributors."
# 
# 4. Except as permitted for the purposes of acknowledgment in paragraph 3,
# neither the name or logo of this software nor the names of its
# authors may be used to endorse or promote products derived from this
# software without specific prior written permission.  The name of the
# software includes the following terms, and any derivatives thereof:
# "Rocks", "Rocks Clusters", and "Avalanche Installer".  For licensing of 
# the associated name, interested parties should contact Technology 
# Transfer & Intellectual Property Services, University of California, 
# San Diego, 9500 Gilman Drive, Mail Code 0910, La Jolla, CA 92093-0910, 
# Ph: (858) 534-5815, FAX: (858) 534-7345, E-MAIL:invent@ucsd.edu
# 
# THIS SOFTWARE IS PROVIDED BY THE REGENTS AND CONTRIBUTORS ``AS IS''
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO,
# THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR
# PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE REGENTS OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR
# BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY,
# WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE
# OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN
# IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
# 
# @Copyright@
#
# $Log: __init__.py,v $
# Revision 1.11  2012/11/27 00:48:30  phil
# Copyright Storm for Emerald Boa
#
# Revision 1.10  2012/05/06 05:48:36  phil
# Copyright Storm for Mamba
#
# Revision 1.9  2011/08/24 19:09:48  anoop
# Need quotes around values
#
# Revision 1.8  2011/07/23 02:30:39  phil
# Viper Copyright
#
# Revision 1.7  2011/05/10 18:35:02  anoop
# mysql does not like it if you don't quote values
#
# Revision 1.6  2011/05/10 05:12:47  anoop
# Move shadow attributes out of attributes tables.
# Seperate secure attributes table for all attributes
# that we want to hide. These attributes will never
# be passed through kickstart.
#
# Revision 1.5  2010/09/07 23:53:02  bruno
# star power for gb
#
# Revision 1.4  2010/07/31 01:02:03  bruno
# first stab at putting in 'shadow' values in the database that non-root
# and non-apache users can't read
#
# Revision 1.3  2009/05/01 19:07:04  mjk
# chimi con queso
#
# Revision 1.2  2009/02/10 20:11:20  mjk
# os attr stuff for anoop
#


import os
import stat
import time
import sys
import string
import rocks.commands

class Command(rocks.commands.set.os.command):
	"""
	Sets an attribute to an os and sets the associated values 

	<arg type='string' name='os'>
	Name of os
	</arg>
	
	<arg type='string' name='attr'>
	Name of the attribute
	</arg>

	<arg type='string' name='value'>
	Value of the attribute
	</arg>
	
	<param type='string' name='attr'>
	same as attr argument
	</param>

	<param type='string' name='value'>
	same as value argument
	</param>

	<example cmd='set os attr linux sge False'>
	Sets the sge attribution to False for linux nodes
	</example>

	"""

	def run(self, params, args):

		(args, attr, value) = self.fillPositionalArgs(('attr', 'value'))
		oses = self.getOSNames(args)
		
		if not attr:
			self.abort('missing attribute name')
		if not value:
			self.about('missing value of attribute')

		for os in oses:
			self.newdb.setCategoryAttr('os', os, attr, value)
			

