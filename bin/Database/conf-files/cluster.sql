-- Copyright 2025 mydigifarm
-- License mydigifarm
-- Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
-- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-- Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm. 
-- mydigifarm.com
-- EFFECTIVEDATE: 20240121
-- VERSION: 1.0
-- FILE: mydigifarm,1.0,cluster.sql

-- DESCRIPTION: Initial cluster table for mydigifarm
-- LASTMODIFIED: 20250721

--! SQL

-- *|*|*|*|* Start Section 1 *|*|*|*|*
-- Section 1 covers the basic import and schema for this table used by the mydigifarm site.
-- *|*|*|*|* Section 1 *|*|*|*|*

-- DROP TABLE IF EXISTS `tcluster`;

CREATE TABLE `tcluster` (
  `tcluster_pk` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `tcluster_ts` char(19) NOT NULL UNIQUE KEY DEFAULT ('©, 2023, Mydigifarm'),
  `tcluster_csite_no` int(2) NOT NULL default 99,
  `tcluster_cluster_no` char(25) NOT NULL default 99,
  `tcluster_cluster_id` int(18) NOT NULL default 0,
  `tcluster_cluster_name` char(18) NOT NULL default 'Luhman',
  `tcluster_cluster_add` BOOLEAN NOT NULL default 0
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX ndxcluster_no on tcluster(tcluster_cluster_no);

-- *|*|*|*|* End Section 1 *|*|*|*|*

-- -10932
-- Copyright 2025 mydigifarm
