// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20250922
// VERSION: 1.0
// FILE: mydigifarm,1.0,AIDrawer.jsx

// DESCRIPTION: Drawer component for AI chat interface.
// LASTMODIFIED: 20250922

//! .jsx

// *|*|*|*|* Start Section 1 *|*|*|*|*
// Section 1 covers the basic setup of variables and library configurations. 
// This is used to set initial variables and import libraries.
// *|*|*|*|* Section 1 *|*|*|*|*

// Import necessary libraries
import * as React from 'react';
import { useState } from 'react';
import Drawer from '@mui/material/Drawer';
import Divider from '@mui/material/Divider';
import { IconButton, Typography, Button } from '@mui/material'
import { Link } from 'react-router-dom';
import AutoAwesomeIcon from '@mui/icons-material/AutoAwesome';
import { Container } from '@mui/material';
import Box from '@mui/material/Box';
import TextField from '@mui/material/TextField';
import KeyboardDoubleArrowRightIcon from '@mui/icons-material/KeyboardDoubleArrowRight';
import axios from 'axios';

// *|*|*|*|* End Section 1 *|*|*|*|*

// *|*|*|*|* Start Section 2 *|*|*|*|*
// Section 2 covers Function creation along with classes and other more complex objects.  
// Most functions are created here and used in the next section. 
// *|*|*|*|* Section 2 *|*|*|*|*

export default function AIDrawer() {

  const botStyle = {
    backgroundColor: '#2596be',
    marginTop: 1,
    marginRight: 1,
    marginLeft: 1,
    width: 'fit-content',
    boxShadow: ' 13px 9px 15px -4px rgba(0,0,0,0.41),-webkit-box-shadow: 13px 9px 15px -4px rgba(0,0,0,0.41),-moz-box-shadow: 13px 9px 15px -4px rgba(0,0,0,0.41)',
    fontSize: ' 1em',
    lineHeight: '1',
    borderRadius: '10px 10px 10px 0px',
    padding: ' 5px 20px',
  }
  const userStyle = {
    backgroundColor: '#F57F17',
    marginTop: 1,
    marginLeft: 1,
    marginRight: 1,
    width: 'fit-content',
    boxShadow: ' 13px 9px 15px -4px rgba(0,0,0,0.41),-webkit-box-shadow: 13px 9px 15px -4px rgba(0,0,0,0.41),-moz-box-shadow: 13px 9px 15px -4px rgba(0,0,0,0.41)',
    fontSize: ' 1em',
    lineHeight: '1',
    borderRadius: '10px 10px 0px 10px',
    padding: ' 10px 20px',
    marginLeft: 'auto'
  }

  const [open, setOpen] = useState(false);
  const [userMessage, setUserMessage] = useState("");
  const [chatHistory, setChatHistory] = useState([]);
  const [loading, setLoading] = useState(false);
  const [imageFile, setImageFile] = useState(null)
  const [apiKey, setApiKey] = useState("")
  const [apiError, setApiError] = useState({ isError: true, status: "", errorMessage: "" })

  const fileInput = React.useRef();

  const toggleDrawer = (newOpen) => () => {
    setOpen(newOpen);
  };

  const sendMessage = async () => {
    if (!userMessage.trim()) return;
    setLoading(true);
    setApiError(false)

    // try {
    // const formData = new FormData();
    // formData.append("prompt", userMessage);

    if (imageFile) {
      // formData.append("file", imageFile)

      // const response = await fetch(`${import.meta.env.VITE_API_BASE_URL}/v1/api/users/prompt/`, {
      //     method: "POST",
      //     body : formData,
      // })

      // if (!response.ok) {
      //     throw new Error("Failed to get response from the server");
      // }

      // const data = await response.json();
      //     setChatHistory((prev) => [
      //         ...prev,
      //         { sender: "user", message: userMessage, isImage: false},
      //         { sender: "user", message: imageFile, isImage: true},
      //         { sender: "bot", message: data.response, isImage: false}
      // ])
    }
    else {
      const json = JSON.stringify({ "prompt": userMessage })
      await axios.post(
        `${import.meta.env.VITE_API_BASE_URL}/v1/api/users/prompt/`, json,
        {
          // body: JSON.stringify({ "prompt": userMessage }),
          headers: {
            "Authorization": apiKey,
            "Content-Type": "application/json"
          }
        })
        .then((response) => {
          { console.log(JSON.stringify(response)) }
          // const data = response.json();
          setChatHistory((prev) => [
            ...prev,
            { sender: "user", message: userMessage, isImage: false },
            { sender: "bot", message: response.data.response, isImage: false }
          ])
          setUserMessage('')
          setImageFile(null)
          setLoading(false);
        })
        .catch((error) => {
          console.log({ isError: true, status: error.status, errorMessage: error.request.statusText })
          setApiError({ isError: true, status: error.status, errorMessage: error.request.statusText })
          setLoading(false);
        })
    }
  }

  const handleImageUpload = (e) => {
    const file = e.target.files[0]
    if (file) {
      setImageFile(file);
    }
  }

  const chat = (
    <Container display='flex'>
      <Box align="left" sx={{ mt: 1 }}>
        <Typography variant="h5">Grow Assistant</Typography>
        <Typography variant="body2" sx={{ marginBottom: 2 }}>Ask our grow assistant to identify a plant, share grow tips, or other plant related questions.</Typography>
      </Box>
      <Box sx={{
        minHeight: "45vh",
        maxHeight: "45vh",
        border: '1px solid #DBDBDB',
        borderRadius: 1,
        marginBottom: 1,
        overflow: 'auto',
        // display: 'flex',
        // flexDirection: 'column-reverse',
      }}>
        {chatHistory.map((chat, index) => (
          <Box
            align={chat.sender === 'user' ? 'right' : 'left'}
            sx={chat.sender === 'bot' ? botStyle : userStyle}
            key={index}>
            {chat.isImage ? (
              <img src={URL.createObjectURL(chat.message)}
                // src={URL.createObjectURL(chat.message)}
                alt="Uploaded"
              />
            ) : (
              chat.message
            )}
          </Box>
        ))}
      </Box>

      <Box>
        <TextField
          multiline
          rows={4}
          placeholder="Enter prompt..."
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          disabled={loading}
          sx={{ width: '100%', marginBottom: 1 }}
        />
        <Box sx={{ display: 'grid', gridTemplateColumns: '50% 50%', marginBottom: 1 }}>
          {/* <Button
                    sx={{justifySelf: 'start'}}
                    disableRipple
                    color="secondary"
                    variant="contained" 
                    disableElevation
                    onClick={()=>fileInput.current.click()}>
                      <Typography color="primary.buttonText" variant="button">Add File</Typography>
                      <input 
                        ref={fileInput} 
                        type="file" 
                        style={{ display: 'none' }} 
                        onChange = {handleImageUpload}
                        accept="image/*"/>
                  </Button> */}
          <Button
            sx={{ justifySelf: 'start' }}
            disableRipple
            color="primary"
            variant="contained"
            disableElevation
            onClick={sendMessage} disabled={loading}>
            {loading ? (<Typography color="primary.buttonText" variant="button">Sending...</Typography>) :
              (<Typography color="primary.buttonText" variant="button">Send</Typography>)}
          </Button>
        </Box>
        <Box>
          <TextField
            placeholder="Enter OpenAI API Key"
            disabled={loading}
            sx={{ width: '100%' }}
            type="password"
            value={apiKey}
            onChange={(e) => setApiKey(e.target.value)}
          />
        </Box>
        {apiError.isError &&
          <Container sx={{
            display: 'grid', gridTemplateColumns: '15% 80%',
          }}>
            <Typography variant='body' align='left' sx={{ color: 'red' }}>{apiError.status}  </Typography>
            <Typography variant='body' align='left' sx={{ color: 'red' }}>{apiError.errorMessage}</Typography>
          </Container>
        }
      </Box>
    </Container>
  )
  const DrawerList = (
    <Container maxWidth="xs" sx={{ display: 'grid' }} role="presentation">
      <KeyboardDoubleArrowRightIcon
        fontSize="large"
        sx={{ marginRight: "auto", color: "#CFCFCF" }}
        onClick={toggleDrawer(false)}>
      </KeyboardDoubleArrowRightIcon>
      <Link to="/" style={{ textDecoration: 'none', margin: 'auto' }}>
        <img src="/src/assets/mydigifarm_logo_transparent.png" style={{ width: "9em", marginTop: '10%' }} />
      </Link>
      <Divider />
      {chat}
    </Container>
  );

  return (
    <div>
      <IconButton onClick={toggleDrawer(true)}
        size="large"
        sx={{ position: 'absolute', right: 30, top: 50 }}>
        <AutoAwesomeIcon sx={{ color: "#FFF49E" }} />
      </IconButton>
      <Drawer anchor='right' open={open} onClose={toggleDrawer(false)}>
        {DrawerList}
      </Drawer>
    </div>
  );
}

// *|*|*|*|* End Section 2 *|*|*|*|*

// -10959
// Copyright 2025 mydigifarm
