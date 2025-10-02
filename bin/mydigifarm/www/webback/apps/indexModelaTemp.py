# Copyright 2025 mydigifarm
# License mydigifarm
# Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
# The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
# Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
# mydigifarm.com
# EFFECTIVEDATE: 20250929
# VERSION: 1.0
# FILE: mydigifarm,1.0,production.py
# DESCRIPTION: Import for production. 
# LASTMODIFIED: 20250929

#! .py

## *|*|*|*|* Start Section 1 *|*|*|*|*
## Section 1 covers the basic setup of variables and library configurations. 
## *|*|*|*|* Section 1 *|*|*|*|*

#  No imports necessary.

## *|*|*|*|* End Section 1 *|*|*|*|*

## *|*|*|*|* Start Section 2 *|*|*|*|*
## Section 2 covers setting up classes and functions. 
## Most functions are created here and used in the next section. 
## *|*|*|*|* Section 2 *|*|*|*|*

class Tactivity(models.Model):
    tactivity_pk = models.AutoField(primary_key=True)
    tactivity_ts = models.CharField(unique=True, max_length=26)
    tactivity_note = models.CharField(max_length=255)
    tactivity_site_no = models.IntegerField()
    tactivity_cluster_no = models.CharField(max_length=25)
    tactivity_resource = models.CharField(max_length=25)
    tactivity_status = models.CharField(max_length=25)

    class Meta:
        managed = False
        db_table = 'tactivity'


class Tcluster(models.Model):
    tcluster_pk = models.AutoField(primary_key=True)
    tcluster_ts = models.CharField(unique=True, max_length=19)
    tcluster_csite_no = models.IntegerField()
    tcluster_cluster_no = models.CharField(max_length=25)
    tcluster_cluster_id = models.IntegerField()
    tcluster_cluster_name = models.CharField(max_length=18)
    tcluster_cluster_add = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tcluster'


class Tcontroller(models.Model):
    tcontroller_pk = models.AutoField(primary_key=True)
    tcontroller_ts = models.CharField(unique=True, max_length=19)
    tcontroller_no = models.IntegerField()
    tcontroller_id = models.CharField(max_length=19)
    tcontroller_name = models.CharField(max_length=19)
    tcontroller_add = models.IntegerField()
    tcontroller_type = models.CharField(max_length=19)
    tcontroller_pins = models.JSONField(blank=True, null=True)
    tcontroller_code = models.CharField(max_length=19)
    tcontroller_message = models.CharField(max_length=32)
    tcontroller_state = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tcontroller'


class Thumidity(models.Model):
    thumidity_pk = models.AutoField(primary_key=True)
    thumidity_ts = models.CharField(unique=True, max_length=19)
    thumidity_cluster_no = models.CharField(max_length=25)
    thumidity_humidity = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'thumidity'


class Tlight(models.Model):
    tlight_pk = models.AutoField(primary_key=True)
    tlight_ts = models.CharField(unique=True, max_length=19)
    tlight_cluster_no = models.CharField(max_length=25)
    tlight_light = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tlight'


class Tmoisture(models.Model):
    tmoisture_pk = models.AutoField(primary_key=True)
    tmoisture_ts = models.CharField(unique=True, max_length=19)
    tmoisture_cluster_no = models.CharField(max_length=25)
    tmoisture_saturation = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tmoisture'


class Tsensor(models.Model):
    tsensor_pk = models.AutoField(primary_key=True)
    tsensor_ts = models.CharField(unique=True, max_length=19)
    tsensor_no = models.IntegerField()
    tsensor_id = models.CharField(max_length=19)
    tsensor_name = models.CharField(max_length=19)
    tsensor_add = models.IntegerField()
    tsensor_type = models.CharField(max_length=19)
    tsensor_pins = models.JSONField(blank=True, null=True)
    tsensor_code = models.CharField(max_length=19)
    tsensor_message = models.CharField(max_length=32)
    tsensor_state = models.CharField(max_length=8)

    class Meta:
        managed = False
        db_table = 'tsensor'


class Tsite(models.Model):
    tsite_pk = models.AutoField(primary_key=True)
    tsite_ts = models.CharField(unique=True, max_length=19)
    tsite_site_no = models.IntegerField()
    tsite_site_id = models.CharField(max_length=25)
    tsite_site_name = models.CharField(max_length=25)
    tsite_site_add = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tsite'


class Tuptime(models.Model):
    tuptime_pk = models.AutoField(primary_key=True)
    tuptime_ts = models.CharField(unique=True, max_length=19)
    tuptime_note = models.CharField(max_length=7)

    class Meta:
        managed = False
        db_table = 'tuptime'


class Tzone(models.Model):
    tzone_pk = models.AutoField(primary_key=True)
    tzone_ts = models.CharField(unique=True, max_length=19)
    tzone_zone_no = models.IntegerField()
    # Field renamed to remove unsuitable characters.
    tzone_zone_name = models.CharField(
        db_column='tzone_zone name', max_length=18)
    tzone_zone_controller = models.CharField(max_length=3)
    # Field renamed to remove unsuitable characters.
    tzone_zone_add = models.IntegerField(db_column='tzone_zone add')

    class Meta:
        managed = False
        db_table = 'tzone'

## *|*|*|*|* End Section 2 *|*|*|*|*

# -10959
# Copyright 2025 mydigifarm
