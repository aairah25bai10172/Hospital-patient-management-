# Global list to hold patient records in memory
patients = []
next_id = 1 # Simple counter for ID generation

def add_patient():
    """Adds a new patient record."""
    global next_id
    print("\n--- Add New Patient ---")

    # Collect required information
    name = input("Enter Patient Name: ").strip()
    age = input("Enter Age: ").strip()
    gender = input("Enter gender: ").strip()
    disease = input("Enter Diagnosis/Disease: ").strip()
    
    # Create the patient dictionary
    new_patient = {
        'id': next_id,
        'name': name,
        'age': age,
        'gender': gender,
        'disease': disease,
        'status': 'Admitted' # Default status
    }
    
    patients.append(new_patient)
    print(f"\n➕ Patient '{name}' added with ID: {next_id}.")
    next_id += 1

def view_patients():
    """Displays all patient records."""
    print("\n--- Current Patient Records ---")
    if not patients:
        print("🚫 No patient records found.")
        return

    # Print data rows simply
    for patient in patients:
        print(f"ID: {patient['id']}, Name: {patient['name']}, Age: {patient['age']}, Disease: {patient['disease']}, Status: {patient['status']}")

def main():
    """The main loop of the application."""
    while True:
        print("\n" + "="*30)
        print("🏥 Simple Patient Manager")
        print("="*30)
        print("1. Add Patient")
        print("2. View All Patients")
        print("3. Exit")
        print("-" * 30)
        
        choice = input("Enter your choice (1-3): ").strip()
        
        if choice == '1':
            add_patient()
        elif choice == '2':
            view_patients()
        elif choice == '3':
            print("\n 🔚 exited succesfully!")
            break
        else:
            print("🛑 Invalid choice. Try again.")

if __name__ == "__main__":
    main()
