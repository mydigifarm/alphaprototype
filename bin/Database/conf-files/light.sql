-- Copyright 2025 mydigifarm
-- License mydigifarm
-- Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
-- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-- Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm. 
-- mydigifarm.com
-- EFFECTIVEDATE: 20240121
-- VERSION: 1.0
-- FILE: mydigifarm,1.0,light.sql

-- DESCRIPTION: Initial light table for mydigifarm
-- LASTMODIFIED: 20250721

--! SQL

-- *|*|*|*|* Start Section 1 *|*|*|*|*
-- Section 1 covers the basic import and schema for this table used by the mydigifarm site.
-- *|*|*|*|* Section 1 *|*|*|*|*

-- DROP TABLE IF EXISTS `tlight` ;

CREATE TABLE `tlight` (
  `tlight_pk` int(11) NOT NULL AUTO_INCREMENT PRIMARY KEY,
  `tlight_ts` char(19) NOT NULL UNIQUE KEY DEFAULT ('©, 2023, mydigifarm'),
  `tlight_cluster_no` char(25) NOT NULL,
  `tlight_light` int(4) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

CREATE INDEX ndx_cluster_no on tlight(tlight_cluster_no);

-- *|*|*|*|* End Section 1 *|*|*|*|*

-- -10941
-- Copyright 2025 mydigifarm
