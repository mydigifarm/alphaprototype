// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,humidity.jsx

// DESCRIPTION: Humidity page for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import { Table, TableBody, TableCell, TableContainer, TableHead, TableRow, Paper, Container, Typography } from '@mui/material';
import Grid from '@mui/material/Grid2';
import useLatest from '../hooks/useLatest';
import LineGraph from '../components/LineGraph/LineGraph';
import { useEffect, useState } from 'react';

export default function Humidity() {

  const [tableLatest, setTableLatest] = useState([]);

  const headers = ["Cluster", "Units", "Datetime"]
  const table = "humidity"

  useEffect(() => {
    async function getTableData() {
      const result = await useLatest(import.meta.env.VITE_API_BASE_URL, table, 1)
      setTableLatest(result)
    }
    getTableData()
  }, [])

  return (
    <Grid container direction="column" alignItems="center" justifyContent="center" sx={{ mb: 15, mt: 15 }}>
      <Typography variant="h3">Humidity</Typography>
      <Paper elevation={3} sx={{ width: '100%', overflow: 'hidden', mt: 5, maxWidth: 400 }}>
        <TableContainer sx={{ maxHeight: 300 }}>
          <Table size="small" aria-label="humidity table" stickyHeader >
            <TableHead>
              <TableRow>
                {headers.map((item) => {
                  return <TableCell align="center" key={item}>{item}</TableCell>
                })}
              </TableRow>
            </TableHead>
            <TableBody>
              {tableLatest.map((row) => (
                <TableRow
                  key={row.data[0].thumidity_cluster_no}
                  sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                >
                  <TableCell align="center" scope="row">
                    {row.data[0].thumidity_cluster_no}
                  </TableCell>
                  <TableCell align="center" >{row.data[0].thumidity_humidity}</TableCell>
                  <TableCell align="center" >{row.data[0].thumidity_ts}</TableCell>
                </TableRow>
              ))}
            </TableBody>
          </Table>
        </TableContainer>
      </Paper>
      <Container sx={{ mt: 6 }}>
        <LineGraph table={table} />
      </Container>
    </Grid>

  );
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
