-- Copyright 2025 mydigifarm
-- License mydigifarm
-- Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
-- The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
-- THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
-- Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm. 
-- mydigifarm.com
-- EFFECTIVEDATE: 20240121
-- VERSION: 1.0
-- FILE: mydigifarm,1.0,uniqueid.sql

-- DESCRIPTION: Initial uniqueid table for mydigifarm
-- LASTMODIFIED: 20250722

--! SQL

-- *|*|*|*|* Start Section 1 *|*|*|*|*
-- Section 1 covers the basic import and schema for this table used by the mydigifarm site.
-- *|*|*|*|* Section 1 *|*|*|*|*

-- DROP TABLE IF EXISTS `uniqueid` ;

CREATE TABLE `uniqueid` (
  `uniqueid_id` int(11) NOT NULL,
  `uniqueid_ts` timestamp NOT NULL,
  `uniqueid_unique_id` int(18) NOT NULL,
  `uniqueid_pseudo_id` int(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


ALTER TABLE `uniqueid`
  ADD PRIMARY KEY (`uniqueid_id`),
  ADD UNIQUE KEY `uniqueid_ts` (`uniqueid_ts`);

ALTER TABLE `uniqueid`
  MODIFY `uniqueid_id` int(11) NOT NULL AUTO_INCREMENT;

-- *|*|*|*|* End Section 1 *|*|*|*|*

-- -10950
-- Copyright 2025 mydigifarm
