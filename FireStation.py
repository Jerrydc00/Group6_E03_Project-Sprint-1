import json

fire_stations = [
    {
        "name": "RAHA Volunteers Fire Department",
        "address": "1085 Padre Noval Street, Sampaloc, Manila, National Capital Region, 1015",
        "phone": "0906 668 7242"
    },
    {
        "name": "Bfp-Ncr Masambong Fire Substation",
        "address": "Malac 4, Quezon City, 00, 1115",
        "phone": "(02) 8373 3731"
    },
    {
        "name": "Punturin Fire Station",
        "address": "3S Center, Metro Manila, Philippines",
        "phone": ""
    },
    {
        "name": "Teejay Fire and Rescue Volunteer",
        "address": "45 Bayani St Brgy Doña Aurora Galas, Manila, National Capital Region, 1113",
        "phone": "0933 360 5082"
    }
]

def find_fire_station():
    emergency_type = input("What type of emergency are you experiencing? (fire, medical, etc.): ").lower()
    
    if emergency_type == "fire":
        print("Here are the nearest fire stations and their hotlines:")
        for station in fire_stations:
            print(f"Name: {station['name']}")
            print(f"Address: {station['address']}")
            print(f"Phone: {station['phone']}\n")
    else:
        print("Sorry, I can only provide information for fire emergencies at the moment.")

def main():
    print("Welcome to the Emergency Assistance Chatbot!")
    while True:
        find_fire_station()
        continue_chat = input("Do you need further assistance? (yes/no): ").lower()
        if continue_chat != "yes":
            print("Thank you for using the Emergency Assistance Chatbot. Stay safe!")
            break

if __name__ == "__main__":
    main()
