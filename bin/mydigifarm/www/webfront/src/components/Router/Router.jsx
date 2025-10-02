// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,Router.jsx

// DESCRIPTION: Router component for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import Home from '../../pages/Home.jsx'
import Dashboard from '../../pages/Dashboard.jsx'
import Temperature from '../../pages/Temperature.jsx'
import Humidity from '../../pages/Humidity.jsx'
import Moisture from '../../pages/Moisture.jsx'
import Light from '../../pages/Light.jsx'
import Login from '../../pages/Login.jsx'
import Register from '../../pages/Register.jsx'
import Health from '../../pages/Health.jsx'

import NavBar from '../NavBar/NavBar.jsx'
import DefaultRoute from '../DefaultRoute/DefaultRoute.jsx'
import Footer from '../Footer/Footer.jsx'

import { Route, Routes, Navigate } from 'react-router-dom'
import { useContext } from 'react'

import { AuthContext } from '../context/AuthContext.jsx'

function Router() {

  const { isAuth } = useContext(AuthContext)

  return (
    <>
    <Routes>
      <Route path="/" element={<NavBar isAuth={isAuth} />}>      
        <Route exact path="/" element={isAuth ? <Home /> : <Navigate replace to={"/login"} />}/>
        <Route path="/dashboard" element={isAuth ? <Dashboard /> : <Navigate replace to={"/login"} />}/>
        <Route path="/temperature" element={isAuth ? <Temperature /> : <Navigate replace to={"/login"} />}/>
        <Route path="/humidity" element={isAuth ? <Humidity /> : <Navigate replace to={"/login"} />}/>
        <Route path="/moisture" element={isAuth ? <Moisture /> : <Navigate replace to={"/login"} />}/>
        <Route path="/light" element={isAuth ? <Light /> : <Navigate replace to={"/login"} />}/>
        <Route path="/health" element={isAuth ? <Health /> : <Navigate replace to={"/login"} />}/>
        <Route path="*" element={isAuth ? <DefaultRoute /> : <Navigate replace to={"/login"} />} />
        <Route path="/login" element={isAuth ? <Navigate replace to={"/"} /> : <Login />} />
         <Route path="/register" element={<Register />}/>
      </Route>
    </Routes>
    <Footer />
    </>
  )
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// *|*|*|*|* Start Section 2 *|*|*|*|*
// Section 2 covers Function creation along with classes and other more complex objects.  
// Most functions are created here and used in the next section. 
// *|*|*|*|* Section 2 *|*|*|*|*

// Export the Router component
export default Router;

// *|*|*|*|* End Section 2 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
