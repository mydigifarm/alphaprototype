// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,MenuDrawer.jsx

// DESCRIPTION: MenuDrawer component for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import * as React from 'react';
import Box from '@mui/material/Box';
import Drawer from '@mui/material/Drawer';
import List from '@mui/material/List';
import Divider from '@mui/material/Divider';
import ListItem from '@mui/material/ListItem';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import { IconButton, Typography } from '@mui/material'
import MenuIcon from '@mui/icons-material/Menu';
import DashboardIcon from '@mui/icons-material/Dashboard';
import WavesIcon from '@mui/icons-material/Waves';
import LightModeIcon from '@mui/icons-material/LightMode';
import ThermostatIcon from '@mui/icons-material/Thermostat';
import HealthAndSafetyIcon from '@mui/icons-material/HealthAndSafety';
import PlayCircleFilledWhiteIcon from '@mui/icons-material/PlayCircleFilledWhite';
import ArticleIcon from '@mui/icons-material/Article';
import BuildCircleIcon from '@mui/icons-material/BuildCircle';
import WaterDropIcon from '@mui/icons-material/WaterDrop';
import { Link } from 'react-router-dom';

export default function MenuDrawer() {
  const [open, setOpen] = React.useState(false);

  const toggleDrawer = (newOpen) => () => {
    setOpen(newOpen);
  };

  const PrimaryMenuBarItems = [
    {
      text: "Dashboard",
      icon: <DashboardIcon />,
      path: "/dashboard",
    },
    {
      text: "Humidity",
      icon: <WaterDropIcon />,
      path: "/humidity",
    },
    {
      text: "Moisture",
      icon: <WavesIcon />,
      path: "/moisture",
    },
    {
      text: "Light",
      icon: <LightModeIcon />,
      path: "/light",
    },
    {
      text: "Temperature",
      icon: <ThermostatIcon />,
      path: "/temperature",
    },
    {
      text: "Health Check",
      icon: <HealthAndSafetyIcon />,
      path: "/health",
    }
  ]
  const SecondaryMenuBarItems = [
    {
      text: "Get Started",
      icon: <PlayCircleFilledWhiteIcon />,
      path: "https://mydigifarm.atlassian.net/wiki/spaces/ML/pages/44957697/Getting+started+with+mydigifarm",
    },
    {
      text: "News",
      icon: <ArticleIcon />,
      path: "http://mydigifarm.com/",
    },
    {
      text: "Guides",
      icon: <BuildCircleIcon />,
      path: "https://mydigifarm.atlassian.net/wiki/spaces/ML/pages/43384833/User+Guides",
    }
  ]

  const DrawerList = (
    <Box sx={{ width: 250 }} role="presentation" onClick={toggleDrawer(false)}>
      <Link to="/" style={{ textDecoration: 'none' }}>
        <img src="/src/assets/mydigifarm_logo_transparent.png" style={{
          width: "9em", marginLeft: '20%', marginTop: '10%'
        }} />
      </Link>
      <Divider />
      <List>
        {PrimaryMenuBarItems.map((item) => (
          <Link to={item.path} style={{ textDecoration: 'none' }} key={item.text}>
            <ListItem key={item.text} disablePadding>
              <ListItemButton sx={{
                '&:hover': {
                  backgroundColor: 'primary.main',
                  color: 'primary.contrastText',
                }
              }}>
                <ListItemIcon>
                  {item.icon}
                </ListItemIcon>
                <Typography color="primary.contrastText">
                  <ListItemText primary={item.text} />
                </Typography>
              </ListItemButton>
            </ListItem>
          </Link>
        ))}
      </List>
      <Divider />
      <List>
        {SecondaryMenuBarItems.map((item) => (
          <ListItem key={item.text} disablePadding>
            <ListItemButton href={item.path} target="_blank" sx={{
              '&:hover': {
                backgroundColor: 'primary.main',
                color: 'primary.contrastText',
              }
            }}>
              <ListItemIcon>
                {item.icon}
              </ListItemIcon>
              <ListItemText primary={item.text} />
            </ListItemButton>
          </ListItem>
        ))}
      </List>
    </Box>
  );

  return (
    <div>
      <IconButton onClick={toggleDrawer(true)}>
        <MenuIcon sx={{ color: "white" }} />
      </IconButton>
      <Drawer open={open} onClose={toggleDrawer(false)}>
        {DrawerList}
      </Drawer>
    </div>
  );
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
