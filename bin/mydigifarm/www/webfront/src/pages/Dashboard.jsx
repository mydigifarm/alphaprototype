// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,dashboard.jsx

// DESCRIPTION: Dashboard page for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import React from 'react'
import LineGraph from '../components/LineGraph/LineGraph';
import { Container, Stack, Grid2, Typography } from '@mui/material';
import { Link } from 'react-router-dom';
import { Link as MUI_Link } from '@mui/material';

export default function Dashboard() {
  return (
    <>
      <Grid2 container spacing={6} sx={{ mt: 20 }}>
        <Grid2 size={6}>
          <Link to="/temperature" style={{ textDecoration: 'none' }}>
            <MUI_Link variant="h4" color="primary" underline="hover">Temperature</MUI_Link>
          </Link>
          <LineGraph table="temperature" />
        </Grid2>
        <Grid2 size={6}>
          <Link to="/humidity" style={{ textDecoration: 'none' }}>
            <MUI_Link variant="h4" color="primary" underline="hover">Humidity</MUI_Link>
          </Link>
          <LineGraph table="humidity" />
        </Grid2>
        <Grid2 size={6}>
          <Link to="/light" style={{ textDecoration: 'none' }}>
            <MUI_Link variant="h4" color="primary" underline="hover">Light</MUI_Link>
          </Link>
          <LineGraph table="light" />
        </Grid2>
        <Grid2 size={6}>
          <Link to="/moisture" style={{ textDecoration: 'none' }}>
            <MUI_Link variant="h4" color="primary" underline="hover">Moisture</MUI_Link>
          </Link>
          <LineGraph table="moisture" />
        </Grid2>
      </Grid2>
    </>

  )
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
