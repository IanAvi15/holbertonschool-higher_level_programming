# RESTful API

## Description

This project explores the fundamentals of RESTful APIs, a core architectural style used for communication between systems over the web. The Representational State Transfer (REST) architecture is built on a set of constraints that allow for scalable, stateless, and cacheable communication, making it a foundational concept in modern software development and system integration.

Through this project, the focus moves across the full lifecycle of API interaction: understanding the underlying HTTP/HTTPS protocols, consuming APIs from the command line, consuming and processing API data in Python, building APIs from scratch using Python's built-in `http.server` module, developing more robust APIs with Flask, securing APIs through authentication, and documenting APIs using OpenAPI standards.

## Learning Objectives

By the end of this project, the following concepts should be well understood:

- HTTP/HTTPS Basics — the foundational principles of the web's primary protocol, including request methods and the difference between secure and non-secure communication.
- API Consumption with Command Line — interacting with APIs using basic command-line tools.
- API Consumption with Python — fetching, parsing, and manipulating API data using Python.
- API Development with http.server — building a simple API from scratch using Python's standard library.
- API Development with Flask — building more scalable APIs with routing and data management using Flask.
- API Security & Authentication — protecting data transfer and restricting access to authorized users.
- API Standards & Documentation with OpenAPI — maintaining standardized, usable, and maintainable API documentation.

## REST API Conceptual Diagram

```
+-------+           +-------+           +---------+           +---------+
|       |  Request  |       |  Process  |         |  Fetch/   |         |
|       |   ----->  |       |  -------> |         |  Modify   |         |
|       |           |       |           |         |  -------> |         |
|       | <-----    |       | <-------  |         |           |         |
|       |  Response |       |  Return   |         |           |         |
+-------+           +-------+           +---------+           +---------+
  Client            Web Server           API Server           Database
```

**Components:**

- **Client** — the requester of the service, often a web browser or application.
- **Web Server** — handles the incoming request and acts as a middleman before passing it to the API server.
- **API Server** — the logic layer that processes the request and determines what data or action is required.
- **Database** — stores the data which the API might fetch or modify.

**Flow:**

1. The client sends an HTTP/HTTPS request to the Web Server.
2. The Web Server, after potential routing and load balancing, forwards the request to the API Server.
3. The API Server processes the request, interacting with the database if needed.
4. The API Server returns the processed response to the Web Server.
5. The Web Server sends back the final HTTP/HTTPS response to the client.

In simpler setups, the Web Server and API Server may be combined into a single layer. The separation above illustrates the potential layers present in a more complex or scaled environment.

## Requirements

- All scripts are tested with Python 3.9.
- Code follows the `pycodestyle` style guide (version 2.x).
- All files end with a new line.
- A `README.md` file at the root of the project is mandatory.

## Author
- Ian Aviles - [GitHub](https://github.com/IanAvi15)