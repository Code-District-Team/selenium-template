# Project Name

## Overview

This repository is designed to facilitate the onboarding process for users, particularly focusing on freelance onboarding. It includes various scripts and configurations to automate and manage user profiles, business information, and trade details.

## Features

- Automates the onboarding process for freelance users.
- Manages user profiles and business information.
- Supports integration with social media platforms like Instagram and Snapchat.
- Provides a structured approach to handle business trade information.

## Folder Structure

- **config.py**: Contains configuration settings such as base URLs and browser preferences.
- **Drivers/**: Includes necessary drivers for browser automation.
- **Pages/**: Contains modules for different page interactions, including user profile onboarding and business profile management.
- **Resources/**: Holds data classes for user and business information.
- **Tests/**: Contains test scripts for validating the onboarding process.
- **Utils/**: Includes utility classes such as locators for web elements.

## Prerequisites

- Python 3.x
- pip (Python package manager)
- Git
- A web browser (e.g., Chrome) and its corresponding WebDriver (e.g., ChromeDriver)

## Setup Instructions

### 1. Install Python and pip

#### Windows

1. Download the Python installer from the [official website](https://www.python.org/downloads/).
2. Run the installer and ensure you check the box "Add Python to PATH".
3. Verify the installation by opening a command prompt and typing:
   ```bash
   python --version
   pip --version
   ```

#### macOS

1. Open Terminal.
2. Install Homebrew if not already installed:
   ```bash
   /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
   ```
3. Install Python:
   ```bash
   brew install python
   ```
4. Verify the installation:
   ```bash
   python3 --version
   pip3 --version
   ```

#### Linux

1. Open Terminal.
2. Update package lists:
   ```bash
   sudo apt update
   ```
3. Install Python and pip:
   ```bash
   sudo apt install python3 python3-pip
   ```
4. Verify the installation:
   ```bash
   python3 --version
   pip3 --version
   ```

### 2. Install Git

#### Windows

1. Download the Git installer from the [official website](https://git-scm.com/download/win).
2. Run the installer and follow the setup instructions.
3. Verify the installation by opening a command prompt and typing:
   ```bash
   git --version
   ```

#### macOS

1. Open Terminal.
2. Install Git using Homebrew:
   ```bash
   brew install git
   ```
3. Verify the installation:
   ```bash
   git --version
   ```

#### Linux

1. Open Terminal.
2. Update package lists:
   ```bash
   sudo apt update
   ```
3. Install Git:
   ```bash
   sudo apt install git
   ```
4. Verify the installation:
   ```bash
   git --version
   ```

### 3. Install ChromeDriver

1. Check your Chrome version by navigating to `chrome://settings/help` in your browser.
2. Download the corresponding ChromeDriver from the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
3. Extract the downloaded file and place the `chromedriver` executable in the `Drivers/` directory of the project.
4. Ensure `chromedriver` is executable and added to your system's PATH.

### 4. Clone the Repository

```bash
git clone <repository-url>
cd <repository-directory>
```

### 5. Install Project Dependencies

Run the following command to install the required packages:

```bash
pip install -r requirements.txt
```

### 6. Run Tests

Execute the test scripts to verify the setup:

```bash
pytest Tests/onboarding/freelanceonboarding_test.py
```

## Additional Information

- **License**: This project is licensed under the MIT License.
- **Contributing**: Contributions are welcome. Please fork the repository and submit a pull request.
- **Contact**: For any queries, please contact [your-email@example.com].

## Notes

- Ensure that the WebDriver is executable and properly configured in your system's PATH.
- Modify the `config.py` file to change the base URL or browser settings as needed.
