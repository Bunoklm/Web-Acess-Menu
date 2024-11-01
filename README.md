# Server Management Dashboard

## Overview

This project is a **Server Management Dashboard** built with Flask that allows users to manage applications across different categories (areas). Users can add, view, and delete applications within specified areas, providing a streamlined way to handle server applications.

## Features

- **Add Applications**: Easily add new applications with a name, URL, and icon URL.
- **View Applications**: Display applications categorized under different areas.
- **Delete Applications**: Remove applications from specified areas.
- **Customizable Areas**: Rename areas (Area 1, Area 2, etc.) as needed.
- **Responsive Design**: The interface adjusts for both desktop and mobile devices.

## Installation

### Prerequisites

To run this application, you need to have **Python** installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

### Required Python Packages

Before running the application, install the required Python packages using the following command:

```bash
pip install Flask
```

### Setup Instructions

1. **Clone the Repository**: Clone this repository to your local machine.

   ```bash
   git clone https://github.com/Bunoklm/Web-Acess-Menu
   cd Web-Acess-Menu
   ```

2. **Modify the Server IP**:
   - Open the `index.html` file.
   - Look for the line where the application makes fetch requests (e.g., `http://192.168.178.102:5000/...`).
   - Replace `192.168.178.102` with your server's IP address. If you are running it on your local machine, you can use `localhost`.
   - **Important**: When using `localhost` in the code and accessing the site via your IP, the apps will not load.

3. **Change the Logo**:
   - In the `index.html` file, locate the `<h1>` tag where the logo image is defined:

   ```html
   <h1><img src="add link for Logo" alt="Logo"> Management Menu</h1>
   ```

   - Replace `add link for Logo` with the URL or path to your desired logo image.

4. **Run the Server**:
   - Navigate to the directory where `serve.py` is located.
   - Start the Flask server with:

   ```bash
   python serve.py
   ```

5. **Access the Dashboard**:
   - Open a web browser and go to `http://<your-ip>:5000` or `http://localhost:5000`.

## How to Rename Areas

You can rename the areas directly in the HTML file:

1. Open the `index.html` file.
2. Locate the sidebar section where the area tabs are defined:

   ```html
   <div class="tab active" onclick="switchTab('Area 1')">Area 1</div>
   <div class="tab" onclick="switchTab('Area 2')">Area 2</div>
   <div class="tab" onclick="switchTab('Area 3')">Area 3</div>
   <div class="tab" onclick="switchTab('Area 4')">Area 4</div>
   <div class="tab" onclick="switchTab('Area 5')">Area 5</div>
   ```

3. Change `'Area 1'`, `'Area 2'`, etc., to your desired names.

## How It Works

- The Flask server hosts the dashboard and handles requests to manage applications.
- Applications are stored in a JSON file named `apps.json`.
- You can add applications by sending a POST request to `/add_app` with JSON data.
- Applications can be retrieved by accessing `/apps/<category>` and deleted by sending a DELETE request to `/delete_app/<category>/<name>`.
