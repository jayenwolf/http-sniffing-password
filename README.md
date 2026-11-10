# HTTP Credential Sniffing & Network Packet Analysis Lab

A hands-on network security lab demonstrating the vulnerabilities of unencrypted plaintext data transmission via an HTTP `POST` login flow, analyzed using Wireshark on Kali Linux.

---

## 1. Overview & Objectives

The purpose of this laboratory exercise is to examine how application-layer authentication data travels across a network when unencrypted protocols are utilized.

* **Protocol Analysis:** Inspect HTTP `POST` transaction mechanics and request header structures.
* **Traffic Sniffing:** Capture live local packets and perform stream reassembly using Wireshark.
* **Vulnerability Demonstration:** Expose the risk of cleartext credential exposure and explain its susceptibility to Man-in-the-Middle (MitM) attacks.

---

## 2. Lab Environment

* **Operating System:** Kali Linux (Virtualized via Oracle VM VirtualBox)
* **Packet Analyzer:** Wireshark
* **Backend Runtime:** Python 3 (`http.server`, `HTTPServer`, `SimpleHTTPRequestHandler`)
* **Capture Interface:** Loopback (`lo`)
* **Service Port:** `8080` (HTTP)

---

## 3. Project Structure

* `index.html`: A minimal authentication form using standard HTML `<form method="POST" action="/login">`.
* `server.py`: A lightweight custom Python HTTP server that captures incoming POST payloads, extracts request body parameters, and returns an HTTP `200 OK` response.

---

## 4. Methodology & Execution

### Step 1: Initialize the Local Web Server
Run the custom Python HTTP listener:
```bash
python3 server.py
