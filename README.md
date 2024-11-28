# Letter-Converter
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![macOS](https://img.shields.io/badge/mac%20os-000000?style=for-the-badge&logo=macos&logoColor=F0F0F0)

"Convert Letters" is a Python-based tool that allows you to translate selected text between Hebrew and English directly from the right-click Services menu on macOS.

Features
- Translate text from Hebrew to English or English to Hebrew.
- Accessible via right-click menu in any application.
- Easy to set up using Automator and Python.

---

## **Prerequisites**
Before setting up the service, ensure you have the following:
1. **Python 3** installed on your macOS system.
   - Test with: `python3 --version`.
2. **Required Python libraries**:
   - Install them by running:
     ```bash
     pip install pyperclip langdetect keyboard
     ```
3. Save the `translate.py` script to a known location. (You’ll use this path during the setup.)

---

## **Setup Instructions**

### **Step 1: Download the Python Script**
1. Save the `translate.py` script to a location on your computer, e.g., `/Users/yourusername/Documents/translate.py`.
2. Make the script executable:
   ```bash
   chmod +x /path/to/translate.py
   ```
3. Copy the execute note at the top of the `translate.py` script
  <img width="359" alt="image" src="https://github.com/user-attachments/assets/6fce773a-631e-4ec3-b75e-98c64ecb2037">


### **Step 2: Create the Automator Quick Action**
1. **Open Automator**:
   - Search for **Automator** in Spotlight or open it from Applications. <br>
      <img width="112" alt="Screen Shot 2024-11-28 at 18 25 32" src="https://github.com/user-attachments/assets/a234f097-fe10-4363-8900-269d357b2c56">

2. **Create a New Quick Action**:
   - Select **File → New** and choose **Quick Action**.<br>
    ![image](https://github.com/user-attachments/assets/44ac8197-ce1f-4bbe-bdc0-4df217891172)

3. **Configure the Quick Action**:
   - Set **Workflow receives** to `text`.
   - Set **In** to `any application`. <br>
  ![image](https://github.com/user-attachments/assets/42d6ac71-915d-455c-84f8-3aeaa2427ae1)

4. **Add a "Run Shell Script" Action**:
   - Drag the **Run Shell Script** action into the workflow.
   - Configure it as follows:
     - **Shell**: `/bin/bash`
     - **Pass input**: `to stdin`
     - Script:
       ```bash
       <first row (note) of translate.py> <path to translate.py>
       ```
       Replace `/path/to/translate.py` with the full path to your script.
       ![image](https://github.com/user-attachments/assets/4d47c197-23c7-40bc-b2a5-9a02796a2fb8)


5. **Save the Quick Action**:
   - Save it with the name `Convert Letters`.
   - The Quick Action is now available in the right-click **Services** menu.
      ![image](https://github.com/user-attachments/assets/733f09f2-c2ab-4e51-8a32-3e1840b72fec)

---

## **Usage**
1. Select text in any application.
2. Right-click and navigate to **Services → Convert Letters**.
3. The script will process the selected text and output the result.

---

## **Testing the Setup**
To ensure everything works:
1. Select some sample text.
2. Right-click and choose **Services → TranslateText**.
3. Verify that the script runs and provides the expected translation.

---

## **Troubleshooting**
1. **Service Not Appearing in the Right-Click Menu**:
   - Ensure the Quick Action is saved under **~/Library/Services/**.
   - Restart your Mac or log out and log back in to refresh macOS Services.

2. **Python Script Not Running**:
   - Verify the Python path in Automator:
   - Ensure the script is executable:

3. **Dependencies Missing**:
   - Install required libraries:
     ```bash
     pip install pyperclip langdetect keyboard
     ```

---

## **Customization**
- Modify the `translate.py` script to:
  - Copy translated text to the clipboard.
  - Automatically replace selected text in certain applications.

