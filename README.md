# Simple Patient Manager

## Project Overview

**Simple Patient Manager** is a Python-based command-line application designed to manage basic patient records in a healthcare environment. This project demonstrates fundamental concepts of data management, user interface design, and object-oriented programming principles suitable for educational purposes in Computer Science Engineering.

---

## Project Information

| Field | Details |
|-------|---------|
| **Institution** | VIT Bhopal |
| **Student Name** | Aairah Parvaiz |
| **Registration Number** | 25BAI10172 |
| **Professor** | G Prabhu Kanna |
| **Department** | Computer Science and Engineering |
| **Project Type** | Python Application - Healthcare Management System |
| **Date** | November 2025 |

---

## Objective

The primary objective of this project is to create a simplified patient management system that allows healthcare administrators or staff to:

- **Add new patient records** with essential information (name, age, gender, diagnosis)
- **View all stored patient records** in a structured format
- **Generate unique patient IDs** automatically for identification
- **Manage patient data** efficiently using in-memory data structures

This project serves as a foundational application for understanding:
- Data structure management (lists and dictionaries)
- User input/output handling
- Menu-driven application design
- Python programming fundamentals

---

## Features

### 1. Add Patient
- Collects comprehensive patient information including name, age, gender, and diagnosis/disease
- Automatically generates unique patient IDs
- Sets default admission status for new patients
- Provides user feedback upon successful record addition

### 2. View All Patients
- Displays all currently stored patient records
- Presents information in a clear, readable format
- Handles cases where no patient records exist
- Shows complete patient details (ID, Name, Age, Disease, Status)

### 3. User-Friendly Menu
- Interactive command-line interface
- Numbered menu options for easy navigation
- Input validation for user choices
- Clear exit functionality

---

## Technical Specifications

### Technology Stack
- **Language**: Python 3.x
- **Data Storage**: In-memory list of dictionaries
- **Interface**: Command-line based user interface
- **Architecture**: Procedural programming with functional decomposition

### System Requirements
- Python 3.6 or higher
- 10 MB RAM (minimum)
- Terminal/Command Prompt access
- No external dependencies or library installations required

### Data Structure
The application uses the following data structure to store patient information:

```python
patient = {
    'id': int,           # Unique patient identifier (auto-generated)
    'name': str,         # Patient's full name
    'age': str,          # Patient's age
    'gender': str,       # Patient's gender (Male/Female/Other)
    'disease': str,      # Patient's diagnosis/disease information
    'status': str        # Patient's admission status (default: 'Admitted')
}
```

---

## Installation and Setup

### Prerequisites
- Python 3.6 or higher installed on your system
- Code editor or IDE (Visual Studio Code, PyCharm, or any text editor)

### Installation Steps

1. **Download the project file**: Obtain the `Simple_Patient_Manager.py` file

2. **Place the file in a project directory**:
   ```bash
   mkdir PatientManager
   cd PatientManager
   ```

3. **Verify Python installation**:
   ```bash
   python --version
   ```

4. **Run the application**:
   ```bash
   python Simple_Patient_Manager.py
   ```

---

## Usage Guide

### Starting the Application

Execute the following command in your terminal:

```bash
python Simple_Patient_Manager.py
```

### Main Menu Options

Upon running the application, you will see the following menu:

```
==============================
🏥 Simple Patient Manager
==============================
1. Add Patient
2. View All Patients
3. Exit
------------------------------
Enter your choice (1-3):
```

### Option 1: Add Patient

When you select option 1, the application will prompt you to enter:

1. **Patient Name**: Full name of the patient
   ```
   Enter Patient Name: Aairah Khan
   ```

2. **Age**: Patient's age in years
   ```
   Enter Age: 25
   ```

3. **Gender**: Gender of the patient
   ```
   Enter gender: Female
   ```

4. **Diagnosis/Disease**: Medical diagnosis or disease information
   ```
   Enter Diagnosis/Disease: Migraine Headache
   ```

Upon successful addition, you will receive confirmation:
```
➕ Patient 'Aairah Khan' added with ID: 1.
```

### Option 2: View All Patients

This option displays all currently stored patient records in the following format:

```
--- Current Patient Records ---
ID: 1, Name: Aairah Khan, Age: 25, Disease: Migraine Headache, Status: Admitted
ID: 2, Name: John Doe, Age: 35, Disease: Diabetes, Status: Admitted
```

If no records exist, the system will display:
```
🚫 No patient records found.
```

### Option 3: Exit

Selecting this option will close the application with a confirmation message:
```
🔚 exited successfully!
```

---

## Program Workflow

### Main Application Flow

1. **Start Application** → Initialize empty patient list and counter
2. **Display Menu** → Show available options to user
3. **Get User Input** → Receive choice from user
4. **Process Choice**:
   - If choice == '1': Execute add_patient() function
   - If choice == '2': Execute view_patients() function
   - If choice == '3': Exit the application
   - Else: Display error message and repeat menu
5. **Loop Back** → Continue until user selects exit

### Function-Level Workflows

#### add_patient() Function Workflow
```
1. Display "Add New Patient" header
2. Declare global next_id variable
3. Collect patient information via input():
   - Name
   - Age
   - Gender
   - Disease
4. Create new_patient dictionary with collected data
5. Set default status to 'Admitted'
6. Append new_patient to patients list
7. Display success message with assigned ID
8. Increment next_id counter
9. Return to main menu
```

#### view_patients() Function Workflow
```
1. Display "Current Patient Records" header
2. Check if patients list is empty
   - If empty: Display "No records found" message and return
   - If not empty: Proceed to step 3
3. Iterate through each patient in patients list
4. Display formatted patient information for each record
5. Return to main menu
```

---

## Pseudocode

### Main Program Structure

```
PROGRAM SimplePatientManager

DECLARE patients AS LIST
DECLARE next_id AS INTEGER = 1

FUNCTION add_patient()
    DECLARE new_patient AS DICTIONARY
    
    DISPLAY "--- Add New Patient ---"
    
    INPUT name FROM user
    INPUT age FROM user
    INPUT gender FROM user
    INPUT disease FROM user
    
    SET new_patient['id'] = next_id
    SET new_patient['name'] = name
    SET new_patient['age'] = age
    SET new_patient['gender'] = gender
    SET new_patient['disease'] = disease
    SET new_patient['status'] = 'Admitted'
    
    APPEND new_patient TO patients
    DISPLAY "➕ Patient added with ID: " + next_id
    
    INCREMENT next_id
END FUNCTION

FUNCTION view_patients()
    DISPLAY "--- Current Patient Records ---"
    
    IF patients IS EMPTY THEN
        DISPLAY "🚫 No patient records found."
        RETURN
    END IF
    
    FOR EACH patient IN patients DO
        DISPLAY patient['id'], patient['name'], patient['age'], 
                patient['disease'], patient['status']
    END FOR
END FUNCTION

FUNCTION main()
    WHILE TRUE DO
        DISPLAY Menu Options
        INPUT user_choice
        
        IF user_choice == '1' THEN
            CALL add_patient()
        ELSE IF user_choice == '2' THEN
            CALL view_patients()
        ELSE IF user_choice == '3' THEN
            DISPLAY "🔚 exited successfully!"
            BREAK
        ELSE
            DISPLAY "🛑 Invalid choice. Try again."
        END IF
    END WHILE
END FUNCTION

CALL main()
END PROGRAM
```

---

## Application Flowchart

The following flowchart represents the overall program flow:

```
                        ┌─────────────┐
                        │   START     │
                        └──────┬──────┘
                               │
                        ┌──────▼──────┐
                        │ Initialize  │
                        │ patients=[] │
                        │ next_id=1   │
                        └──────┬──────┘
                               │
                        ┌──────▼─────────────┐
                        │  Display Main Menu │
                        └──────┬─────────────┘
                               │
                    ┌──────────┼──────────┐
                    │          │          │
                ┌───▼──┐  ┌───▼──┐  ┌──▼───┐
                │ '1'  │  │ '2'  │  │ '3'  │
                └───┬──┘  └───┬──┘  └──┬───┘
                    │        │        │
              ┌─────▼┐  ┌────▼───┐  ┌─▼──────┐
              │ Add  │  │ View   │  │Display │
              │Patient│ │Patient │  │Exit Msg│
              └─────┬─┘  └────┬───┘  └─┬──────┘
                    │        │        │
                    │        │    ┌───▼─────┐
                    │        │    │   END   │
                    │        │    └─────────┘
                    │        │
                    └────┬───┘
                         │
                         │(Loop back if not '3')
                         │
                    ┌────▼──────┐
                    │ Back to    │
                    │  Menu      │
                    └────┬───────┘
                         │
                         └─────────(return to Display Menu)
```

---

## Screenshots

### Screenshot 1: Application Code Structure
![Code Overview](image:1)

### Screenshot 2: Application Code (Continued)
![Code Continuation](image:2)

### Screenshot 3: Application Output - Running Application
![Application Execution](image:3)

---

## Code Implementation Details

### Global Variables
- `patients`: A Python list that stores all patient records as dictionaries
- `next_id`: An integer counter that generates unique patient IDs sequentially

### Core Functions

#### 1. add_patient()
- **Purpose**: Captures new patient information and adds it to the system
- **Input Parameters**: None (uses input() for user entry)
- **Output**: Confirmation message with assigned patient ID
- **Data Validation**: Uses .strip() method to remove leading/trailing whitespace

#### 2. view_patients()
- **Purpose**: Displays all stored patient records
- **Input Parameters**: None
- **Output**: Formatted patient records or "no records found" message
- **Error Handling**: Checks for empty patient list

#### 3. main()
- **Purpose**: Controls the application loop and menu navigation
- **Input Parameters**: None
- **Output**: Interactive menu and function calls based on user choice
- **Loop Control**: Continues until user selects exit (option 3)

### Special Features

- **Auto-incrementing ID System**: Each patient receives a unique ID automatically
- **Default Status**: All new patients are assigned "Admitted" status by default
- **User-Friendly Emoji Icons**: Enhanced visual appeal with emoji indicators
- **Input Sanitization**: Uses .strip() method to clean user input
- **Menu Validation**: Handles invalid choices gracefully

---

## Data Flow Diagram

```
User Input
    │
    ├──► Choice = '1' ──► add_patient() ──► Input Collection
    │                         │
    │                    Create Dictionary
    │                         │
    │                    Append to patients[]
    │                         │
    │                    Display Confirmation
    │
    ├──► Choice = '2' ──► view_patients() ──► Check patients[]
    │                         │
    │                    Display Records
    │                         │
    │                    Return to Menu
    │
    └──► Choice = '3' ──► Exit Application
```

---

## Testing and Validation

### Test Case 1: Add Single Patient
**Input**: Name = "Aairah", Age = "25", Gender = "Female", Disease = "Fever"
**Expected Output**: Patient added with ID: 1 confirmation

### Test Case 2: Add Multiple Patients
**Process**: Add 3 different patients sequentially
**Expected Output**: Each patient receives unique IDs (1, 2, 3)

### Test Case 3: View Empty List
**Initial State**: No patients added yet
**Expected Output**: "🚫 No patient records found." message

### Test Case 4: View Populated List
**Initial State**: 2 patients already added
**Expected Output**: Display both patient records with all details

### Test Case 5: Invalid Menu Choice
**Input**: Choice = "5"
**Expected Output**: "🛑 Invalid choice. Try again." message and menu reappears

---

## Future Enhancements

Potential improvements for future versions include:

1. **Search Functionality**: Search patients by ID, name, or disease
2. **Update Patient Records**: Modify existing patient information
3. **Delete Patient Records**: Remove patients from the system
4. **File Persistence**: Save and load patient data from files
5. **Database Integration**: Use SQLite or MySQL for permanent storage
6. **Advanced Filtering**: Filter patients by disease, age range, or status
7. **Statistics Dashboard**: Display statistics like total patients, disease distribution
8. **Discharge Management**: Update patient status from "Admitted" to "Discharged"
9. **Appointment Scheduling**: Schedule follow-up appointments for patients
10. **Data Export**: Export patient records to CSV or PDF formats

---

## Limitations and Considerations

### Current Limitations
1. **In-Memory Storage**: Data is lost when the application closes
2. **No Data Persistence**: No permanent storage of patient records
3. **Limited Fields**: Only stores basic patient information
4. **No Search/Edit**: Cannot modify or search for existing records
5. **Single User**: No multi-user or authentication system
6. **No Input Validation**: Accepts any input without validation
7. **Console Only**: No graphical user interface

### Considerations for Production
- Implement database for data persistence
- Add comprehensive input validation
- Implement user authentication and authorization
- Create GUI for better user experience
- Add data backup and recovery mechanisms
- Implement encryption for sensitive data

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Python not recognized | Install Python and add to PATH environment variable |
| Script won't run | Ensure Python version is 3.6 or higher |
| No output appears | Check that the script is in the correct directory |
| Menu options not working | Ensure exact input (1, 2, or 3) without extra spaces |

---

## Academic Value and Learning Outcomes

This project demonstrates proficiency in:

- **Data Structures**: Usage of lists and dictionaries for data management
- **Control Flow**: Implementation of loops and conditional statements
- **Functions**: Modular design with well-defined function responsibilities
- **User Interaction**: Interactive menu system design
- **Python Fundamentals**: Core programming concepts and syntax
- **Problem-Solving**: Systematic approach to application development
- **Documentation**: Professional code documentation and comments

---

## References and Resources

- Python Official Documentation: https://www.python.org/doc/
- Data Structures in Python: Lists and Dictionaries
- Command-Line Interface Design Best Practices
- Healthcare System Architecture and Requirements

---

## Conclusion

The Simple Patient Manager project represents a practical application of Python programming fundamentals in a real-world healthcare scenario. While simplified for educational purposes, it demonstrates essential concepts that form the foundation for developing more complex management systems. The project showcases proper program structure, user interface design, and data management practices suitable for academic assessment and professional development.

---

**Project Status**: Completed ✓  
**Last Updated**: November 23, 2025  
**Version**: 1.0
