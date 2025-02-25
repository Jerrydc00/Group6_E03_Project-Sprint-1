import json

# Updated database of police stations covering all NCR cities
police_stations = [
    # Manila
    {
        "name": "PNP - Manila Police District",
        "address": "Taft Avenue, Ermita, Manila",
        "phone": "(02) 523-0001"
    },
    
    # Quezon City
    {
        "name": "PNP - Quezon City Police District",
        "address": "Near Quezon City Hall, Quezon City",
        "phone": "(02) 8929-0001"
    },
    
    # Caloocan
    {
        "name": "PNP - Caloocan City Police Station",
        "address": "Caloocan City Hall Compound, Caloocan",
        "phone": "(02) 8364-0001"
    },
    
    # Las Piñas
    {
        "name": "PNP - Las Piñas Police Station",
        "address": "Diego Cera Avenue, Las Piñas",
        "phone": "(02) 8873-0001"
    },
    
    # Makati
    {
        "name": "PNP - Makati Police Station",
        "address": "Ayala Avenue, Makati",
        "phone": "(02) 8884-0001"
    },
    
    # Malabon
    {
        "name": "PNP - Malabon Police Station",
        "address": "F. Sevilla Blvd, Malabon",
        "phone": "(02) 8364-0002"
    },
    
    # Mandaluyong
    {
        "name": "PNP - Mandaluyong Police Station",
        "address": "Maysilo Circle, Mandaluyong",
        "phone": "(02) 8534-0002"
    },
    
    # Marikina
    {
        "name": "PNP - Marikina Police Station",
        "address": "Shoe Ave, Marikina",
        "phone": "(02) 8687-0002"
    },
    
    # Muntinlupa
    {
        "name": "PNP - Muntinlupa Police Station",
        "address": "National Road, Muntinlupa",
        "phone": "(02) 8862-0001"
    },
    
    # Navotas
    {
        "name": "PNP - Navotas Police Station",
        "address": "C-4 Road, Navotas",
        "phone": "(02) 8286-0001"
    },
    
    # Parañaque
    {
        "name": "PNP - Parañaque Police Station",
        "address": "San Antonio Ave, Parañaque",
        "phone": "(02) 8826-0001"
    },
    
    # Pasay
    {
        "name": "PNP - Pasay Police Station",
        "address": "Arnaiz Ave, Pasay",
        "phone": "(02) 8854-0001"
    },
    
    # Pasig
    {
        "name": "PNP - Pasig Police Station",
        "address": "Ortigas Avenue, Pasig",
        "phone": "(02) 8864-0001"
    },
    
    # San Juan
    {
        "name": "PNP - San Juan Police Station",
        "address": "Pinaglabanan Street, San Juan",
        "phone": "(02) 8725-0001"
    },
    
    # Taguig
    {
        "name": "PNP - Taguig Police Station",
        "address": "C-5 Road, Taguig",
        "phone": "(02) 8864-0002"
    },
    
    # Valenzuela
    {
        "name": "PNP - Valenzuela Police Station",
        "address": "MacArthur Highway, Valenzuela",
        "phone": "(02) 8353-0001"
    },
    
    # Pateros
    {
        "name": "PNP - Pateros Police Station",
        "address": "M. Almeda Street, Pateros",
        "phone": "(02) 8864-0003"
    }
]

# Emergency hotline database
emergency_contacts = {
    "police": {
        "National Emergency Hotline": "911",
        "Philippine National Police": "911",
        "NCR Police Regional Office": "(02) 8723-0401"
    },
    "medical": {
        "Philippine Red Cross": "(02) 8790-2300"
    },
    "fire": {
        "Bureau of Fire Protection": "911"
    }
}

def get_emergency_assistance():
    print("\nAvailable emergency services:")
    print("1. Police Emergency")
    print("2. Medical Emergency")
    print("3. Fire Emergency")
    print("4. Other Emergencies")
    
    while True:
        try:
            choice = int(input("Please enter your choice (1-4): "))
            if 1 <= choice <= 4:
                return choice
            print("Invalid input. Please enter a number between 1-4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

def display_emergency_info(emergency_type):
    if emergency_type == 1:  # Police Emergency
        print("\nPolice Stations in Metro Manila:")
        for station in police_stations:
            print(f"\n{station['name']}")
            print(f"Address: {station['address']}")
            print(f"Contact: {station['phone']}")
        print("\nNational Police Hotline: 911")
        
    elif emergency_type == 2:  # Medical Emergency
        print("\nMedical Emergency Contacts:")
        for service, number in emergency_contacts["medical"].items():
            print(f"{service}: {number}")
            
    elif emergency_type == 3:  # Fire Emergency
        print("\nFire Emergency Contacts:")
        for service, number in emergency_contacts["fire"].items():
            print(f"{service}: {number}")
            
    else:  # Other Emergencies
        print("\nFor other emergencies, please contact:")
        print("National Emergency Hotline: 911")
        print("Metro Manila Development Authority (MMDA): 136")

def main():
    print("="*50)
    print("Metro Manila Emergency Response System - Police Edition")
    print("="*50)
    
    while True:
        emergency_type = get_emergency_assistance()
        display_emergency_info(emergency_type)
        
        continue_help = input("\nDo you need further assistance? (yes/no): ").lower()
        if continue_help != "yes":
            print("\nThank you for using the emergency response system. Stay safe!")
            break

if __name__ == "__main__":
    main()
