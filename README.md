# Python Web Browser

This project is a simple web browser built using Python and PyQt5. It leverages the PyQt5 framework to create a graphical user interface (GUI) and the `QWebEngineView` widget to render web pages.

## Features

- **Navigation Buttons**:
  - Back: Navigate to the previous page.
  - Forward: Navigate to the next page.
  - Reload: Refresh the current page.
  - Stop: Halt the loading of the current page.
  - Home: Navigate to the homepage (default: Google).

- **URL Bar**:
  - Enter a URL to navigate to a specific website.
  - The URL bar updates dynamically as you browse.

- **Custom Buttons**:
  - Clear URL: Clears the URL bar.

## Prerequisites

- Python 3.6 or higher
- PyQt5

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/abhijeet02323/python-web-browser.git
   cd python-web-browser
   ```

2. Install the required library:
   ```bash
   pip install PyQt5
   ```

## Usage

1. Run the browser:
   ```bash
   python browser.py
   ```

2. Interact with the browser using the navigation buttons and URL bar.

## Code Overview

The main functionality is provided by the `WebBrowser` class:

- **Browser Initialization**:
  The `QWebEngineView` widget initializes with Google as the default page.

- **Navigation Toolbar**:
  - Buttons for Back, Forward, Reload, Stop, and Home.
  - A URL bar for entering or editing URLs.

- **Event Handling**:
  - `urlChanged`: Updates the URL bar when navigating to a new page.
  - `returnPressed`: Navigates to the URL entered in the URL bar.

## Screenshot

![Python Web Browser UI](https://via.placeholder.com/800x400?text=Screenshot+Coming+Soon)


## Contribution

Contributions are welcome! Feel free to fork the repository, make changes, and submit a pull request.

## Author

[Abhijeet Dwivedi](https://github.com/abhijeet02323)
