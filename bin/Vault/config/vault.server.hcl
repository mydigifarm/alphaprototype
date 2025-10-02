// Copyright 2025 mydigifarm
// License mydigifarm
// Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:
// The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.
// THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL mydigifarm BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
// Except as contained in this notice, the name of mydigifarm shall not be used in advertising or otherwise to promote the sale, use or other dealings in this Software without prior written authorization from mydigifarm.
// mydigifarm.com
// EFFECTIVEDATE: 20240106
// VERSION: 1.0
// FILE: mydigifarm,1.0,template.hcl
 
// DESCRIPTION: This file is used to set up the port listeners for the APIs used by vault for the mydigifarm project. 
// LASTMODIFIED: 20250723
 
//! .hcl
 
storage "raft"{
        path = "/vault/data"
        node_id = "node1"
}
 
listener "tcp"{
        address = "0.0.0.0:8200"
        tls_disable_client_certs = "false"
        tls_cert_file = "/vault/cert/vault.crt"
        tls_key_file = "/vault/cert/vault.key"
}
 
disable_mlock = true
 
api_addr = "https://0.0.0.0:8200"
cluster_addr = "https://127.0.0.1:8201"
 
// -10924
// Copyright 2025 mydigifarm
