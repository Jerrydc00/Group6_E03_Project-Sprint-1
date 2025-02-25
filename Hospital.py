# Sample hospital data in Manila area
hospitals = [
    {"name": "Philippine General Hospital", "contact": "(02) 8554-8400", "location": "Ermita, Manila"},
    {"name": "Jose Reyes Memorial Medical Center", "contact": "(02) 8711-9491", "location": "Santa Cruz, Manila"},
    {"name": "Dr. Jose Fabella Memorial Hospital", "contact": "(02) 8733-8553", "location": "Santa Cruz, Manila"},
    {"name": "Manila Doctors Hospital", "contact": "(02) 8558-0888", "location": "Ermita, Manila"},
    {"name": "Ospital ng Maynila Medical Center", "contact": "(02) 8523-5171", "location": "Malate, Manila"},
    {"name": "San Lazaro Hospital", "contact": "(02) 8711-3485", "location": "Santa Cruz, Manila"},
    {"name": "University of Santo Tomas Hospital", "contact": "(02) 8731-3001", "location": "Sampaloc, Manila"},
    {"name": "Metropolitan Medical Center", "contact": "(02) 8527-0001", "location": "Binondo, Manila"}
]

# Emergency instructions based on type
emergency_instructions = {
    "General Emergency": "Stay calm, check for breathing, and apply first aid if necessary.",
    "Cardiac Emergency": "Perform CPR if needed and keep the patient in a comfortable position.",
    "Trauma Emergency": "Apply pressure to stop bleeding and avoid unnecessary movement.",
    "Pediatric Emergency": "Keep the child calm and monitor their breathing and consciousness.",
    "OB-GYN Emergency": "Ensure the patient is in a comfortable position and monitor contractions.",
    "Poisoning": "Do not induce vomiting unless instructed by a medical professional. Provide details of the substance ingested.",
    "COVID-19 or Infectious Disease": "Wear a mask, isolate the patient, and monitor symptoms such as difficulty breathing.",
    "Burn Injuries": "Cool the burn with running water for at least 10 minutes and avoid applying ice or ointments.",
    "Choking": "Perform the Heimlich maneuver if the person is conscious and encourage coughing.",
    "Seizures": "Ensure the person is lying on their side, clear nearby objects, and do not restrain their movements.",
    "Stroke": "Check for signs of stroke (Face drooping, Arm weakness, Speech difficulty) and keep the person calm.",
    "Fractures": "Immobilize the injured area and avoid unnecessary movement.",
    "Allergic Reactions": "Administer an epinephrine auto-injector if available and monitor breathing.",
    "Heat Stroke": "Move the person to a cool area, hydrate with water, and apply cool cloths to their skin."
}

def get_nearest_hospital(user_area, emergency_type):
    matching_hospitals = [h for h in hospitals if user_area.lower() in h["location"].lower()]
    
    if matching_hospitals:
        nearest_hospital = matching_hospitals[0]
    else:
        nearest_hospital = hospitals[0]  # Default to the first hospital if no match is found
    
    instructions = emergency_instructions.get(emergency_type, "Stay calm and wait for medical professionals.")
    
    return {
        "name": nearest_hospital["name"],
        "contact": nearest_hospital["contact"],
        "location": nearest_hospital["location"],
        "instructions": instructions
    }

if __name__ == "__main__":
    user_area = input("Enter your area in Manila: ")
    print("Select emergency type:")
    for idx, key in enumerate(emergency_instructions.keys(), start=1):
        print(f"{idx}. {key}")
    emergency_choice = int(input("Enter the number corresponding to your emergency: "))
    emergency_type = list(emergency_instructions.keys())[emergency_choice - 1]
    
    result = get_nearest_hospital(user_area, emergency_type)
    print("\nNearest Hospital:")
    print(f"Name: {result['name']}")
    print(f"Contact: {result['contact']}")
    print(f"Location: {result['location']}")
    print(f"Instructions: {result['instructions']}")
