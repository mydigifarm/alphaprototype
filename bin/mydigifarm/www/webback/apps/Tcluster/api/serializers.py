# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250929
# VERSION: 1.0
# FILE: mydigifarm,1.0,serializers.py
# DESCRIPTION: Sets up the file serializer.
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

from rest_framework import serializers
from apps.Tcluster.models import Tcluster

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

class TclusterSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tcluster
        fields = ['tcluster_pk', 'tcluster_ts', 'tcluster_csite_no',
                  'tcluster_cluster_no', 'tcluster_cluster_id', 'tcluster_cluster_name', 'tcluster_cluster_add',]

    def save(self):
        cluster = Tcluster(
            tcluster_ts=self.validated_data['tcluster_ts'],
            tcluster_csite_no=self.validated_data['tcluster_csite_no'],
            tcluster_cluster_no=self.validated_data['tcluster_cluster_no'],
            tcluster_cluster_id=self.validated_data['tcluster_cluster_id'],
            tcluster_cluster_name=self.validated_data['tcluster_cluster_name'],
            tcluster_cluster_add=self.validated_data['tcluster_cluster_add'],
        )

        cluster.save()

        return cluster

## *|*|*|*|* End Section 2 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
