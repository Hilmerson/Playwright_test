# Email Automation with Playwright and pytest-bdd

This project demonstrates how to automate email interactions, including login, composing an email with an attachment, sending the email, and logout, on Yahoo Mail using Playwright and pytest-bdd in Python.

https://github.com/Hilmerson/Playwright_test/assets/103628349/7e9e0075-d514-4cba-90ed-f89bfa9a3c37

## Features

- **Login to Yahoo Mail**: Automates the login process using environment variables for credentials.
- **Compose Email**: Automatically composes an email to a contact, including subject and body text.
- **Attach File**: Demonstrates adding an attachment to the email.
- **Send Email**: Automates the process of sending the email.
- **Logout**: Automates the logout process, ensuring a clean session end.

## Setup and Installation

### Prerequisites

- Python 3.6+
- A Yahoo Mail account
- Git (for version control)

### Installation Steps

1. **Clone the repository**:
    ```bash
    git clone https://github.com/Hilmerson/Playwright_test.git
    cd Playwright_test
    ```

2. **Create and activate a virtual environment** (optional but recommended):
    ```bash
    python -m venv venv
    # On Windows
    venv\Scripts\activate
    # On Unix or MacOS
    source venv/bin/activate
    ```

3. **Install required packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set up environment variables**:
    Create a `.env` file in the root of the project and add your Yahoo Mail credentials:
    ```
    PLAYWRIGHT_EMAIL_USERNAME=yourEmailUsername
    PLAYWRIGHT_EMAIL_PASSWORD=yourEmailPassword
    ```
    Ensure the `.env` file is added to `.gitignore` to keep your credentials secure.

5. **Run the tests**:
    ```bash
    pytest nameofyourfile.py
    ```

## Usage

The tests can be run using the pytest command as shown above. Make sure you're in the project's root directory.
