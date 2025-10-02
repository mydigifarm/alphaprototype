// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,Login.jsx

// DESCRIPTION: Login page for the application.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import React, { useContext, useState } from 'react'
import { useNavigate } from "react-router-dom";
import axios from 'axios';
import { Stack, TextField, Button, Typography, Grid2, Container } from '@mui/material';
import { AuthContext } from '../components/context/AuthContext';
import { Link } from 'react-router-dom';

export default function Login() {

    const { setIsAuth, baseApiUrl } = useContext(AuthContext)
    const [isEnabled, setIsEnabled] = useState(true)

    const navigate = useNavigate();

    const linkStyle = {
    textDecoration: "none",
    color: '#048815',
    backgroundColor: '#FFF'
    };

    const submitForm = async (e) => {
        e.preventDefault()

        const formData = new FormData(e.target)

        await axios
        .post(`${baseApiUrl}/v1/api/users/login/`, formData, {
            headers: {
            "Content-Type": "multipart/form-data",
            },
        })
        .then((response) => {
            console.log(response);
            if (response.data.token) {
                document.cookie = `userAuthToken=${response.data.token}`;
                setIsAuth(true)
                // setUser(response.data.token)
                localStorage.setItem('user', response.data.token)
                // const { token, message, ...restAuthUser } = response.data;
                // console.log(token, message);
                // TO DO set state of Auth.
                navigate("/");
                // this.$store.commit("SET_AUTH_USER", { ...restAuthUser });
                // this.$router.go({ name: "HomePage" });
                
            }
        })
        .catch((error) => {
            console.log(error);
        });
    }

    const waitAnimation = async () => {
        setTimeout(() => {
            setIsEnabled(false)
        },1500)
    }
    
    waitAnimation()

  return (
    <>
    <div className={isEnabled ? 'color-overlay' : ''} style={isEnabled ? {backgroundColor: '#0C4510'} : {} }> </div>
        {/* <img src="/src/assets/mydigifarm_logo_transparent.png" className={ isEnabled ? 'color-overlay' : ''} />  */}

        <div className={ isEnabled ? 'circle' : ''}>    </div>
      <Grid2       
            container
            spacing={0}
            direction="column"
            alignItems="center"
            justifyContent="top"
            sx={{mt: '10rem'}}
            >        
        <img src='/src/assets/mydigifarm_logo_transparent_smaller.png' style={{width: '327px', height: '154px', marginBottom: '3em'}}></img>
        <form noValidate onSubmit={submitForm}>

            <Stack spacing={2} width={400}>
                <TextField name='email' id='email' label='Email' variant='filled' type='email' required/>
                <TextField name='password' id='password' label='Password' variant='filled' type="password" required />
                <Button variant='contained' type='submit'>
                    <Typography variant="button" color="primary.buttonText">Login</Typography>
                </Button>
                <Typography>Need to register? <Link to="/register" 
                style={linkStyle}>                    
                    Click here.</Link></Typography>                
            </Stack>
        </form>
    </Grid2>


    </>
    );
}

// *|*|*|*|* End Section 1 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
