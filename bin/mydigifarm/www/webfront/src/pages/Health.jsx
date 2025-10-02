// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,health.jsx

// DESCRIPTION: Health page for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import { Typography, Container, Box, Button  } from '@mui/material'
import React from 'react'
import { useState, useEffect } from 'react'
import axios from 'axios'
import CancelIcon from '@mui/icons-material/Cancel';
import CheckCircleIcon from '@mui/icons-material/CheckCircle';
import HourglassBottomIcon from '@mui/icons-material/HourglassBottom';

export default function Health() {
  const ipAddr = location.hostname

  const [ dbStatus, setDbStatus ] = useState(true);
  const [ clusterStatus, setClusterStatus ] = useState(true);
  const [ clusterResults, setClusterResults ] = useState([])
  const [ isPendingClusterResults, setIsPendingClusterResults ] = useState(false)
  const [ isPendingDbResults, setIsPendingDbResults ] = useState(false)
  const [ showClusterStatusResults, setShowClusterStatusResults, ] = useState(false);
  const [hostname, setHostName] = useState("")

  function toEpochTime(timestampStr) {
      // Replace dots in date part with dashes to make it ISO-compatible
      const isoStr = timestampStr.replace(/^(\d{4})\.(\d{2})\.(\d{2})/, '$1-$2-$3');
      
      // Create Date object
      const date = new Date(isoStr);

      // Return epoch time in milliseconds
      return date.getTime();
  }

  function isOlderThan15Minutes(epochTime) {
    const FIFTEEN_MINUTES_MS = 15 * 60 * 1000; // 900,000 milliseconds
    const now = Date.now(); // Current time in milliseconds

    return now - epochTime > FIFTEEN_MINUTES_MS;
  }

  function extractTimestampValues(data) {
    const result = [];
    const tsRegex = /_ts$/;

    data.forEach(sensorGroup => {
      sensorGroup.forEach(sensorEntry => {
        sensorEntry.data.forEach(reading => {
          for (const key in reading) {
            if (tsRegex.test(key)) {
              result.push(reading[key]);
            }
          }
        });
      });
    })

    return result;
  }

  async function getHostname() {
    await axios.get(
      `${import.meta.env.VITE_API_BASE_URL}/v1/api/users/hostname`)
      .then((response) => {
        setHostName(response.data.hostname)
        // setDbStatus(true)
        // setIsPendingDbResults(false)
      })
      .catch((error) => {
        // setDbStatus(false)
        console.log(error);
      });
  }

  async function checkDbStatus() {
    // Disable button
    setIsPendingDbResults(true)

    // This function executes very quick. The timeout creates false delay for user feedback.
    await timeout(3000);

      await axios.get(
            `${import.meta.env.VITE_API_BASE_URL}/v1/api/humidity/clusters/all/latest/1/`,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          )
            .then((response) => {
              setDbStatus(true)
              setIsPendingDbResults(false)
            })
            .catch((error) => {
              setDbStatus(false)
              console.log(error);
            });
  }

  function timeout(delay) {
      return new Promise( res => setTimeout(res, delay) );
  }

  async function checkClusterStatus() {
    // Disable button
    setIsPendingClusterResults(true)

    // Clear clusterResults
    setClusterResults([])

    // This function executes very quick. The timeout creates false delay for user feedback.
    await timeout(3000);

    // Set target URLs
    const urls = [`${import.meta.env.VITE_API_BASE_URL}/v1/api/humidity/clusters/all/latest/1/`,
                  `${import.meta.env.VITE_API_BASE_URL}/v1/api/light/clusters/all/latest/1/`,
                  `${import.meta.env.VITE_API_BASE_URL}/v1/api/temperature/clusters/all/latest/1/`,
                  `${import.meta.env.VITE_API_BASE_URL}/v1/api/moisture/clusters/all/latest/1/`]
    // Fetch data and set in state clusterResults
    await urls.map(url => {
        axios.get(
            url,
            {
              headers: {
                "Content-Type": "application/json",
              },
            }
          ).then((response) => {
            setClusterResults((prev) => 
              [...prev,
              response.data]
            )
            })
            .catch((error) => {
              console.log(error);
            });
      }
    )

    // Extract just the timestamp values for all results
    const data = extractTimestampValues(clusterResults)

    // Evaluate the timestamps. If just one is older than 15minutes, update the clusterStatus.
    // This indicates that there are values older than 15 minutes meaning new data is not
    // being written to the database

    data.forEach((element) => {
      if (isOlderThan15Minutes(toEpochTime(element))) {
        setClusterStatus(true)
        return 
      }
    })

    setIsPendingClusterResults(false)
  };

  // Run checks on load. Update if state changes.
  useEffect (() => {
      checkDbStatus()
      checkClusterStatus()
      getHostname()
  }, [])

    return (
      <Container sx={{mb:15, mt: 20}} maxWidth="md">
        <Typography variant='h3'>Health Check</Typography>
          <Box sx={{ display: 'grid', gridTemplateColumns: 'repeat(2, 50%)', rowGap: 1, mt:10}}>
              <Typography variant='h6' align='left'>IP Address</Typography>
              <Typography variant='h6' align='right' >{ipAddr}</Typography>

              <Typography variant='h6' align='left'>Hostname</Typography>
              <Typography variant='h6' align='right'>{hostname}</Typography>
          </Box>
          <Box sx={{ display: 'grid', gridTemplateColumns: '25% 25% 50%', rowGap: 1, marginTop: '.70em'}}>
            <Typography variant='h6' align='left'>Database Status</Typography>
            <Button disableRipple
                    disabled={isPendingDbResults}
                    color="secondary" 
                    variant="contained" 
                    disableElevation 
                    onClick={() => {checkDbStatus()}}
                    sx={{maxWidth: '1em', maxHeight: '2em', marginLeft: '1em'}}>
              <Typography color="primary.buttonText" variant="button">Test</Typography>
            </Button>
            <Box sx={{ display: 'grid', justifyContent: 'right'}}>
              { isPendingDbResults ? <HourglassBottomIcon sx={{color:"blue"}}/> :
                    dbStatus ? <CheckCircleIcon sx={{color:"green"}} />
                      : <CancelIcon sx={{color:"red"}} />}
            </Box>
            <Typography variant='h6' align='left'>Cluster Status</Typography>
            <Box sx={{ display: 'flex', justifyContent: 'left'}}>
              <Button disableRipple
                      disabled={isPendingClusterResults}
                      color="secondary" 
                      variant="contained" 
                      disableElevation 
                      onClick={() => {checkClusterStatus()}}
                      sx={{maxWidth: '1em', maxHeight: '2em',  marginLeft: '1em'}}>
                <Typography color="primary.buttonText" variant="button">Test</Typography>
              </Button>
              <Button disableRipple
                      disabled={clusterResults.length > 0 ? false : true}
                      color="secondary" 
                      variant="contained" 
                      disableElevation 
                      onClick={() => setShowClusterStatusResults((prev) => !prev)}
                      sx={{maxWidth: '1em', maxHeight: '2em', marginLeft: '1em'}}>
                <Typography color="primary.buttonText" variant="button">Show</Typography>
              </Button>
              </Box>
              <Box sx={{ display: 'grid', justifyContent: 'right'}}>
                {
                  isPendingClusterResults ? <HourglassBottomIcon sx={{color:"blue"}}/> :
                    clusterStatus ? <CancelIcon sx={{color:"red"}} />
                    : <CheckCircleIcon sx={{color:"green"}} /> }
              </Box>
          </Box>
            { showClusterStatusResults ?
            <Box sx={{marginTop: '3em', display: 'flex',textAlign:'left', maxHeight: '29em', overflow:'scroll', backgroundColor: '#eff1f1'}} >
              <pre > 
                  {JSON.stringify(clusterResults, null, 4)} 
              </pre>   
            </Box>: ""}
      </Container>
    )
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
