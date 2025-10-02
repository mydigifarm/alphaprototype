// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,custom-theme-provider.jsx

// DESCRIPTION: Custom theme provider for managing light and dark modes using Material-UI.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import { useState, createContext } from "react"
import { createTheme, ThemeProvider } from "@mui/material"
import { green, purple, blue, red, pink, orange, yellow } from "@mui/material/colors"

export const ColorModeContext = createContext(null)

// *|*|*|*|* End Section 1 *|*|*|*|*

// *|*|*|*|* Start Section 2 *|*|*|*|*
// Section 2 covers Function creation along with classes and other more complex objects.  
// Most functions are created here and used in the next section. 
// *|*|*|*|* Section 2 *|*|*|*|*

// Makes the CustomThemProvider component available for import in other files.
const CustomThemeProvider = ({ children }) => {
    const [mode, setMode] = useState('light')

    const colorMode = () => {
        setMode((prev) => (prev === "light" ? "dark" : "light"))
    }

    const theme = createTheme({
        palette: {
            mode: mode,
            ...(mode === 'light' ?
                {
                    primary: {
                        main: "#048815",
                        light: purple[100],
                        dark: blue[800],
                        contrastText: "black",
                        buttonText: "white",
                    },
                    secondary: {
                        main: blue[600],
                        light: blue[100],
                        dark: blue[800],
                        contrastText: orange[800],
                        },
                }
            :   {
                    primary: {
                        main: "#048815",
                        light: red[100],
                        dark: blue[800],
                        contrastText: "white",
                        buttonText: "white"
                    },
                    secondary: {
                        main: blue[600],
                        light: pink[100],
                        dark: pink[800],
                        contrastText: blue[800]
                    },
                }
            )
        },
    })

    return (
        <ColorModeContext.Provider value={colorMode}>    
                <ThemeProvider theme={theme}>
                    {children}
                </ThemeProvider>
        </ColorModeContext.Provider>
           )      
}

export default CustomThemeProvider;

// *|*|*|*|* End Section 2 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
