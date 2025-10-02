// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,LineGraph.jsx

// DESCRIPTION: LineGraph component for displaying sensor data in a line chart.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import React, { useContext, useEffect, useState } from 'react'
import useLatest from '../../hooks/useLatest'
import GenerateSeriesData from './GenerateSeriesData'
import { Button, Typography, Container, Paper, Box } from '@mui/material';
import Chart from "react-apexcharts";
import { LineGraphOptions } from './LineGraphOptions';
import Loading from '../Loading/Loading';
import { AuthContext } from '../context/AuthContext';

export default function LineGraph({ table }) {
    const [series, setSeries] = useState()
    const [isReady, setIsReady] = useState(false)
    const [options, setOptions] = useState()
    const [isActive, setIsActive] = useState(false)

    const { baseApiUrl } = useContext(AuthContext)

    async function updateGraph(num, table, options) {
        setIsActive(!isActive)
        const updatedOptions = updatedChartOptions(table, options)
        setOptions(updatedOptions)
        const queryResults = await useLatest(baseApiUrl, table, num)
        const formated = await GenerateSeriesData(queryResults, table)
        setIsReady(true)        
        setSeries(formated)
    }

    function updatedChartOptions(table, options) {
        let yaxisName = table[0].toUpperCase() + table.slice(1)
        if (yaxisName == "Temperature") {
            yaxisName = `${yaxisName} C°`
        }
        return { ...options, yaxis: { title: { text: yaxisName } }}
    }

    useEffect(() => {
        updateGraph(48, table, LineGraphOptions)
    }, [])
    
// const ResuableButton = (props) => {
//    return (
//       <Button variant={props.buttonVariant} 
//               size={props.size} 
//               sx={{ backgroundColor: isActive ? "pink" : "primary"}}
//               onClick={props.onClick}
//       >
//       {props.buttonText}
//       </Button>
//     )
//    }

    return (
        <Paper elevation={1} square={false} sx={{ p:'1em'}}>
            <Container sx={{mb:3}}>
                <Button disableRipple 
                        variant="contained" 
                        size="small" 
                        color="primary"
                        onClick={() => {
                            updateGraph(4, table);
                        }}>
                    <Typography color="primary.buttonText" variant="button">1 Hour</Typography>
                </Button>
                <Button disableRipple 
                        variant="contained" 
                        size="small" 
                        color="primary"
                        onClick={() => { 
                            updateGraph(12, table);
                        }}>
                    <Typography color="primary.buttonText" variant="button">3 Hour</Typography>
                </Button>
                <Button disableRipple 
                        variant="contained" 
                        size="small" 
                        color="primary"
                        onClick={() => {
                            updateGraph(24, table);
                        }}> 
                    <Typography color="primary.buttonText" variant="button">6 Hour</Typography>
                </Button>
                <Button disableRipple 
                        variant="contained" 
                        size="small" 
                        color="primary"
                        onClick={() => {
                            updateGraph(48, table);
                        }}> 
                    <Typography color="primary.buttonText" variant="button">12 Hour</Typography>
                </Button>
            </Container>
            <Container>
                { isReady ? 
                <Chart
                    options={options}
                    series={series}
                    type="line"
                    /> : 
                    <Loading />}
            </Container>
        </Paper>
    )
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
