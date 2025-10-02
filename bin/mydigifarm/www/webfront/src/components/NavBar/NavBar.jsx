// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,NavBar.jsx

// DESCRIPTION: NavBar component for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import React, { useContext } from 'react'
import { AppBar, IconButton, Toolbar, Stack } from '@mui/material'
import BrightnessMediumIcon from '@mui/icons-material/BrightnessMedium'
import { ColorModeContext } from '../context/custom-theme-provider';
import MenuDrawer from '../MenuDrawer/MenuDrawer';
import { Outlet, Link } from 'react-router-dom';
import LoginIcon from '@mui/icons-material/Login';
import { AuthContext } from '../context/AuthContext.jsx';
import headerImage from '../../assets/plantwidegreen.png'
import HomeIcon from '@mui/icons-material/Home';
import AIDrawer from '../AIDrawer/AIDrawer.jsx';

export default function NavBar() {

  const colorMode = useContext(ColorModeContext);
  const { isAuth, baseApiUrl } = useContext(AuthContext);

  const handleLogout = () => {
    localStorage.clear();
    location.reload()

      // await axios
      //   .get(`${baseApiUrl}/v1/api/users/logout/`, {
      //     // headers: {
      //     //   "Content-Type": "application/json",
      //     //   Authorization: "Token " + getters.getUserAuthToken + "",
      //     // },
      //   })
      //   .then((response) => {
      //     const { message } = response.data;
      //     console.log(message);
      //     localStorage.clear();
      //     //expiring cookie and delete
      //     // document.cookie =
      //       // "userAuthToken=; expires=Thu, 01 Jan 1970 00:00:00 UTC; path=/;";

      //     // commit("SET_AUTH_USER", {});
      //     // router.go({ path: "/" });
      //   })
      //   .catch((error) => {
      //     console.log(error);
      //   });
    }

  return (
    <>
     <AppBar variant='elevated' 
        sx={{ backgroundImage:`url(${headerImage})`,
              backgroundPosition: 'center',
              backgroundRepeat: 'no-repeat',
              backgroundSize: 'cover',
              height: '7rem'}}>
      <Toolbar >  
        { isAuth ? [
          <MenuDrawer />,
          <AIDrawer/>] : ""}        
        <div style={{
            position: 'absolute', 
            left: '50%', 
            top: '50%',
            transform: 'translate(-50%, -50%)'
        }}>

        </div>
        <Stack direction="row" sx={{marginLeft: 'auto'}}>
          <IconButton onClick={colorMode}>
            <BrightnessMediumIcon sx={{marginLeft: "auto", color:"white"}} />
          </IconButton>
          <Link to="/">
            <IconButton >
              <HomeIcon sx={{marginLeft: "auto", color:"white"}} />
            </IconButton>
          </Link>
          { isAuth ?
            <IconButton 
              sx={{marginLeft: "auto", color:"white"}}
              onClick={handleLogout}>
              <LoginIcon />
            </IconButton>
            : ""
          }
        </Stack>
      </Toolbar>
    </AppBar>
    <Outlet />
    </>
  )
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
