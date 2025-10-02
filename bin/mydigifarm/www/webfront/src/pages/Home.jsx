// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,Home.jsx

// DESCRIPTION: Home page for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import * as React from 'react';
import Grid from '@mui/material/Grid2';
import Card from '@mui/material/Card';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import CardActionArea from '@mui/material/CardActionArea';
import Container from '@mui/material/Container';
import { Link } from 'react-router-dom'
import DashboardIcon from '@mui/icons-material/Dashboard';
import WavesIcon from '@mui/icons-material/Waves';
import LightModeIcon from '@mui/icons-material/LightMode';
import ThermostatIcon from '@mui/icons-material/Thermostat';
import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';
import PlayCircleFilledWhiteIcon from '@mui/icons-material/PlayCircleFilledWhite';
import ArticleIcon from '@mui/icons-material/Article';
import BuildCircleIcon from '@mui/icons-material/BuildCircle';
import WaterDropIcon from '@mui/icons-material/WaterDrop';

const Root = () => {

  const items = [
      {
        title: "Dashboard",
        text: "See all your sites and clusters.",
        path: "/dashboard",
        image: <DashboardIcon fontSize="large" sx={{color:"#6349AB"}}/>
      },
      {
        title: "Humidity",
        text: "Latest humidity values and graphs.",
        path: "/humidity",
        image: <WaterDropIcon sx={{color:"#88D1E3"}}fontSize="large" />
      },
      {
        title: "Temperature",
        text: "Latest temperature values and graphs.",
        path: "/temperature",
        image: <ThermostatIcon sx={{color:"#D12626"}} fontSize="large"/>
      },
      {
        title: "Moisture",
        text: "Latest moisture values and graphs.",
        path: "/moisture",
        image: <WavesIcon sx={{color:"#3BA0FF"}} fontSize="large" />
      },
      {
        title: "Light",
        text: "Latest light values and graphs.",
        path: "/light",
        image: <LightModeIcon sx={{color:"#FFC13B"}} fontSize="large"/>
      },
      {
        title: "Health Check",
        text: "View the health status of the system.",
        path: "/health",
        image: <HealthAndSafetyIcon sx={{color:"#F488F7"}} fontSize="large"/>
      },
      {
        title: "Get Started",
        text: "Check out our getting started guide.",
        path: "https://mydigifarm.atlassian.net/wiki/spaces/ML/pages/44957697/Getting+started+with+mydigifarm",
        target: "blank",
        image: <PlayCircleFilledWhiteIcon sx={{color:"#2CD126"}} fontSize="large"/>
      },
      {
        title: "News",
        text: "Catch up on the latest news.",
        path: "http://mydigifarm.com/",
        target: "blank",
        image: <ArticleIcon sx={{color:"#919191"}} fontSize="large"/>
      },
      {
        title: "Guides",
        text: "Explore our full guides and documentation.",
        path: "https://mydigifarm.atlassian.net/wiki/spaces/ML/pages/43384833/User+Guides",
        target: "blank",
        image: <BuildCircleIcon sx={{color:"#FF8000"}} fontSize="large"/>
      },
    ]

  return (
    <Container sx={{margin: '7em auto 5em auto'}}>
       <Grid container spacing={{ sm: 1, md: 1 }} sx={{justifyContent: "center", alignItems: "center"}}>
        {items.map((item, index) => (
          <Grid key={index} >
            <Card variant="outlined" sx={{ width: 200, height: 150 }}>
                <CardActionArea>
                  <Link to={item.path} style={{ textDecoration: 'none' }} target={item.target}>
                    <CardContent>
                      {item.image}
                      <Typography gutterBottom variant="h5" component="div" color="primary.contrastText">
                          {item.title}
                      </Typography>
                      <Typography variant="body2" color="primary.contrastText">
                          {item.text}
                      </Typography>
                    </CardContent>
                  </Link>
                </CardActionArea>
            </Card>
          </Grid>
        ))}
      </Grid>
      </Container>
  )
}

export default Root

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
