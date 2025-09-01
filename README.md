# Tabuada: Simple XML-RPC Multiplication Table Server

This project provides a simple XML-RPC server that calculates and returns the multiplication table for a given integer.  A client application is also provided to interact with the server, allowing users to request the multiplication table for any integer they input.

## Features and Functionality

*   **Multiplication Table Generation:** The server calculates the multiplication table (0 to 10) for a number provided by the client.
*   **XML-RPC Communication:** Uses XML-RPC for communication between the client and server.
*   **Client-Server Architecture:**  The client requests the multiplication table, and the server processes the request and returns the result.
*   **Input Validation (Client-Side):** The client prompts the user for an integer input.  While the server handles non-integer input without crashing (due to Python's dynamic typing), the client encourages integer input for optimal behavior.
*   **Error Handling (Implicit):**  The `SimpleXMLRPCServer` provides basic error handling.  Invalid requests will result in XML-RPC fault responses.

## Technology Stack

*   **Python:**  The entire project is written in Python.
*   **xmlrpc.server:**  Used for creating the XML-RPC server.
*   **xmlrpc.client:** Used for creating the XML-RPC client.

## Prerequisites

Before running the project, ensure you have the following installed:

*   **Python 3.x:** The code is written in Python 3. It may not be compatible with Python 2.  You can download Python from [https://www.python.org/downloads/](https://www.python.org/downloads/).

## Installation Instructions

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/JoaoGaspar04/Tabuada.git
    cd Tabuada
    ```

2.  **Navigate to the code directory:**

    ```bash
    cd Trabalho/Código
    ```

## Usage Guide

1.  **Start the server:**

    ```bash
    python SimpleXMLRPCServer.py
    ```

    The server will start and listen on `localhost:8000`.  Keep this terminal window open while using the client.

2.  **Run the client:**

    Open a new terminal window and navigate to the `Trabalho/Código` directory (as in step 2 of installation).  Then, execute the client script:

    ```bash
    python client.py
    ```

3.  **Enter an integer:**

    The client will prompt you to enter an integer.  Type in the number and press Enter.

4.  **View the multiplication table:**

    The client will display the multiplication table for the number you entered, calculated by the server.

## API Documentation

The XML-RPC server exposes one function:

*   **`tb(x)`:**  This function takes an integer `x` as input and returns a string containing the multiplication table of `x` from 0 to 10.

    *   **Parameters:**
        *   `x` (int): The integer for which to calculate the multiplication table.
    *   **Return Value:**
        *   (str): A string containing the multiplication table, with each line formatted as `"x x n = x * n\n"`.

Example Request (using a generic XML-RPC client):

```xml
<?xml version="1.0"?>
<methodCall>
  <methodName>tb</methodName>
  <params>
    <param>
      <value><int>7</int></value>
    </param>
  </params>
</methodCall>
```

Example Response:

```xml
<?xml version="1.0"?>
<methodResponse>
  <params>
    <param>
      <value><string>7 x 0 = 0
7 x 1 = 7
7 x 2 = 14
7 x 3 = 21
7 x 4 = 28
7 x 5 = 35
7 x 6 = 42
7 x 7 = 49
7 x 8 = 56
7 x 9 = 63
7 x 10 = 70
</string></value>
    </param>
  </params>
</methodResponse>
```

## Contributing Guidelines

Contributions are welcome! To contribute to this project, follow these steps:

1.  Fork the repository.
2.  Create a new branch for your feature or bug fix.
3.  Make your changes and commit them with descriptive commit messages.
4.  Push your changes to your forked repository.
5.  Submit a pull request to the main repository.

Please ensure your code adheres to the existing style and includes appropriate comments and documentation.

## License Information

This project has no license specified. All rights are reserved.

## Contact/Support Information

For questions or support, please contact JoaoGaspar04 through GitHub.