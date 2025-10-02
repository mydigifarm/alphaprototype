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
# DESCRIPTION: Sets up routers and url patterns. 
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

from django.urls import path
from apps.Tlight.api.views import (
    light_cluster_all,
    light_cluster_latest,
    light_cluster_latest_count,
    light_cluster_date_range,
    light_cluster_date_specific,
    light_cluster_datetime_range,
    light_clusters_all,
    light_clusters_all_latest,
    light_clusters_all_latest_count,
    light_clusters_all_date_range,
    light_clusters_all_date_specific,
    light_clusters_all_datetime_range,
)

app_name = "Tlight"

urlpatterns = [  
    ############################################################################
    ########################### One or more clusters ###########################
    ############################################################################
    # Get all values for one or more clusters
    path('cluster/<cluster_no>', light_cluster_all),
    # Get the latest values for one or more clusters
    path('cluster/<cluster_no>/latest', light_cluster_latest),
    # Get a specific number of latest values for one or more clusters
    path('cluster/<cluster_no>/latest/<count>/', light_cluster_latest_count),
    # Get all the values for a specific date range for one or more clusters
    path('cluster/<cluster_no>/date/range', light_cluster_date_range),
    # Get all the values for a specific date for one or more clusters
    path('cluster/<cluster_no>/date/specific', light_cluster_date_specific),
    # Get all the values for a specific datetime range for one or more clusters
    path('cluster/<cluster_no>/datetime/range', light_cluster_datetime_range),


    ############################################################################
    ############################### All clusters ###############################
    ############################################################################
    # Get all values for all clusters
    path('clusters/all', light_clusters_all),
    # Get the latest value for all clusters
    path('clusters/all/latest', light_clusters_all_latest),
    # Get a specific number of latest values for for all clusters
    path('clusters/all/latest/<count>/', light_clusters_all_latest_count),
    # Get all the values for a specific date range for all clusters
    path('clusters/all/date/range', light_clusters_all_date_range),
    # Get all the values for a specific date for all clusters
    path('clusters/all/date/specific', light_clusters_all_date_specific),
    # Get all the values for a specific datetime range for all clusters
    path('clusters/all/datetime/range', light_clusters_all_datetime_range),
]

## *|*|*|*|* End Section 1 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
