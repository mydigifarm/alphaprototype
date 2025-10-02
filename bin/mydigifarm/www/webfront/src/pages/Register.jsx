// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,Register.jsx

// DESCRIPTION: Register page for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import { Stack, TextField, Button, Typography, Grid2 } from '@mui/material';
import axios from 'axios';
import { useNavigate, Link } from "react-router-dom";
import './circular-reveal.css'
import { useState, useEffect } from 'react';

export default function Register() {
    const navigate = useNavigate();
    const [password01, setPassword01] = useState();
    const [password02, setPassword02] = useState();
    const [passwordsMatch, setPasswordsMatch] = useState(false);
    const [disableSubmit, setDisableSubmit] = useState(true);
    const [message, setMessage] = useState();

    const API_BASE_URL = import.meta.env.VITE_API_BASE_URL

    const submitForm = async (e) => {
      setDisableSubmit(true)
        e.preventDefault()
        
        const formData = new FormData(e.target)

        await axios
        .post(`${API_BASE_URL}/v1/api/users/register/`, formData, {
          headers: {
            "Content-Type": "multipart/form-data",
          },
        })
        .then((response) => {
          console.log(response);

          if (response.data.token) {
            // console.log(`Token is : ${response.data.token}`)
            document.cookie = `userAuthToken=${response.data.token}`;
            navigate("/");
          }
        })
        .catch((error) => {
          setMessage(error.message)
          console.log(error);
          setDisableSubmit(false)
        });
    };    
    
    const linkStyle = {
        textDecoration: "none",
        color: '#048815',
        backgroundColor: '#FFF'
    };

    const handleFormValidate = () => {
      if (password01 === password02 && password01 != null && password02 != null) {
        console.log("Passwords match.")
        setPasswordsMatch(true)
        setDisableSubmit(false)
      } else {
        setPasswordsMatch(false)
        setDisableSubmit(true)
      }
    }
    
    useEffect(() => {
      handleFormValidate()
    }, [password01, password02])
    

  return (
      <Grid2   
            container
            spacing={0}
            direction="column"
            alignItems="center"
            justifyContent="top"
            sx={{mt: '6rem', mb: '6rem'}}
            >
        <img src='/src/assets/mydigifarm_logo_transparent_smaller.png' style={{width: '327px', height: '154px', marginBottom: '3em'}}></img>

        <Typography variant='h4'>Register</Typography>
        <form onSubmit={submitForm} >
          <Stack spacing={2} width={400}>
            <TextField name='first_name' id='first_name' label='First Name' variant='filled' type="text" required />
            <TextField name='last_name' id='last_name' label='Last Name' variant='filled' type="text" required />
            <TextField name='email' id='email' label='Email' variant='filled' type='email' required/>
            <TextField name='password'
                       id='password01' 
                       label='Password' 
                       variant='filled' 
                       type="password" 
                       required 
                       onChange={(e) => setPassword01(e.target.value)}
                       />
            <TextField name='password' 
                       id='password02' 
                       label='Confirm Password' 
                       variant='filled' 
                       type="password" 
                       required 
                       onChange={(e) => setPassword02(e.target.value)} />
            <Button variant='contained' type='submit' disabled={disableSubmit}>Register</Button>
            {!passwordsMatch && <Typography variant='body' sx={{color: 'red'}}>Password must match.</Typography> }
            {message && <Typography variant='body' sx={{color: 'red'}}>Email is already registered.</Typography> }
            <Link to="/login" style={linkStyle}>Return to login</Link> 
          </Stack>

        </form>
      </Grid2>
  );
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
