// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,AuthContext.jsx

// DESCRIPTION: Authentication context provider for managing user authentication state across the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import React from 'react'
import { useState, createContext, useEffect } from "react"

export const AuthContext = createContext(null)

// *|*|*|*|* End Section 1 *|*|*|*|*

// *|*|*|*|* Start Section 2 *|*|*|*|*
// Section 2 covers Function creation along with classes and other more complex objects.  
// Most functions are created here and used in the next section. 
// *|*|*|*|* Section 2 *|*|*|*|*

const AuthProvider = ({ children }) => {
  // const wtf = import.meta.env.VITE_API_BASE_URL
  const [isAuth, setIsAuth] = useState(false)
  const [baseApiUrl, setBaseApiUrl] = useState(import.meta.env.VITE_API_BASE_URL)
  const loggedInUser = localStorage.getItem("user");
  
  useEffect(() => {    
      if (loggedInUser) {
          setIsAuth(true)
      }
  }, []);

  return (
    <AuthContext.Provider value={{ isAuth, setIsAuth, baseApiUrl }}> {children} </AuthContext.Provider>
  )
}

// Makes the AuthProvider component available for import in other files.
export default AuthProvider;

// *|*|*|*|* End Section 2 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
