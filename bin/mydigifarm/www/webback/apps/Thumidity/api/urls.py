# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250929
# VERSION: 1.0
# FILE: mydigifarm,1.0,urls.py
# DESCRIPTION: URLs used for upload. 
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

from django.urls import path
from apps.Thumidity.api.views import (
    humidity_cluster_all,
    humidity_cluster_latest,
    humidity_cluster_latest_count,
    humidity_cluster_date_range,
    humidity_cluster_date_specific,
    humidity_cluster_datetime_range,
    humidity_clusters_all,
    humidity_clusters_all_latest,
    humidity_clusters_all_latest_count,
    humidity_clusters_all_date_range,
    humidity_clusters_all_date_specific,
    humidity_clusters_all_datetime_range,
)

app_name = "Thumidity"

urlpatterns = [  
    ############################################################################
    ########################### One or more clusters ###########################
    ############################################################################
    # Get all values for one or more clusters
    path('cluster/<cluster_no>', humidity_cluster_all),
    # Get the latest values for one or more clusters
    path('cluster/<cluster_no>/latest', humidity_cluster_latest),
    # Get a specific number of latest values for one or more clusters
    path('cluster/<cluster_no>/latest/<count>/', humidity_cluster_latest_count),
    # Get all the values for a specific date range for one or more clusters
    path('cluster/<cluster_no>/date/range', humidity_cluster_date_range),
    # Get all the values for a specific date for one or more clusters
    path('cluster/<cluster_no>/date/specific', humidity_cluster_date_specific),
    # Get all the values for a specific datetime range for one or more clusters
    path('cluster/<cluster_no>/datetime/range', humidity_cluster_datetime_range),


    ############################################################################
    ############################### All clusters ###############################
    ############################################################################
    # Get all values for all clusters
    path('clusters/all', humidity_clusters_all),
    # Get the latest value for all clusters
    path('clusters/all/latest', humidity_clusters_all_latest),
    # Get a specific number of latest values for for all clusters
    path('clusters/all/latest/<count>/', humidity_clusters_all_latest_count),
    # Get all the values for a specific date range for all clusters
    path('clusters/all/date/range', humidity_clusters_all_date_range),
    # Get all the values for a specific date for all clusters
    path('clusters/all/date/specific', humidity_clusters_all_date_specific),
    # Get all the values for a specific datetime range for all clusters
    path('clusters/all/datetime/range', humidity_clusters_all_datetime_range),
]

## *|*|*|*|* End Section 1 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
