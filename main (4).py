from typing import List, Dict, Optional


def print_data(get_data):

  # a function for joining all the data stored in the data list
  stored_data = ", ".join(str(n) for n in get_data)
  stored_data = stored_data.replace(" ", "")
  return (stored_data)


def readPatientsFromFile(filename):
  patients = {}

  try:
    with open(filename, 'r') as file:
      # Getting the index of the line as well as getting the data
      for line, data in enumerate(file):
        try:
          # Reading the data from the text file
          data = data.strip()
          data = data.split(",")
          # print(f"{line}:{data}") just for checking
          if (len(data) != 8):
            print(
              f"Invalid number of fields {print_data(data)} in line: {line+1}")
            continue
            # To check weather the data has proper format or not
          try:
            patient_id = int(data[0])
            date = data[1]
            temp = round(float(data[2]), 2)
            pulse = int(data[3])
            resp_rate = int(data[4])
            systolic = int(data[5])
            diastolic = int(data[6])
            oxygen = int(data[7])
          except:
            print(f"Invalid data type in line: {line+1}")
            continue
          # To check the temperature value is  within the range of 30 to 43
          if temp < 30 or temp > 43:
            print(f"Invalid temperature value ({temp}) in line: {line+1}")
            continue
          # To check the heart rate value is not within the range of 30 to 200
          if pulse < 30 or pulse > 200:
            print(f"Invalid heart rate value {pulse} in line: {line+1}")
            continue
          # To check weather the respiratory rate value is  within the range of 5 to 60
          if resp_rate < 5 or resp_rate > 60:
            print(
              f"Invalid respiratory rate value {resp_rate} in line: {line+1}")
            continue
          # To check weather the systolic blood pressure value is  within the range of 50 to 250
          if systolic < 50 or systolic > 250:
            print(
              f"Invalid systolic blood pressure value {systolic} in line: {line+1}"
            )
            continue
          # To check weather the diastolic blood pressure value is  within the range of 30 to 150
          if diastolic < 30 or diastolic > 150:
            print(
              f"Invalid diastolic blood pressure value {diastolic} in line: {line+1}"
            )
            continue
          # To check weather the oxygen saturation value is within  the range of 80 to 100
          if oxygen < 80 or oxygen > 100:
            print(
              f"Invalid oxygen saturation value {oxygen} in line: {line+1}")
            continue
          # Finally after completing all the validation returning a dictionary

          if patient_id not in patients:
            patients[patient_id] = []
          patients[patient_id].append(
            [date, temp, pulse, resp_rate, systolic, diastolic, oxygen])
        except:
          # This will be executed when there will be an unexpected condition
          print("An unexpected error occurred while reading the file.")
  except FileNotFoundError:
    # To catch error when the file is not found
    print(f"The file '{filename}' could not be found.")
  return patients


def displayPatientData(patients, patientId=0):
  # Getting the patients data through the patients id no

  data = patients.get(patientId)

  if patientId == 0:
    # looping over the data of all the patients
    for i in patients:
      print(f"Patient ID: {i}")
      # Getting the data from the patients id
      visits = patients[i]
      for visit in visits:
        # displaying the visit details of all patient
        print(f" Visit Date: {visit[0]}")

        print(f"  Temperature: {(round(visit[1],2)):.2f} C")
        print(f"  Heart Rate: {visit[2]} bpm")
        print(f"  Respiratory Rate: {visit[3]} bpm")
        print(f"  Systolic Blood Pressure: {visit[4]} mmHg")
        print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")
        print(f"  Oxygen Saturation: {visit[6]} %")
  elif data is None:
    print(f"Patient with ID {patientId} not found.")
  # Print individual data
  else:
    # Displaying the details of single patient
    print(f"Patient ID: {patientId}")
    visits = patients[patientId]
    for visit in visits:
      print(f" Visit Date: {visit[0]}")
      print(f"  Temperature: {round(visit[1],2)} C")
      print(f"  Heart Rate: {visit[2]} bpm")
      print(f"  Respiratory Rate: {visit[3]} bpm")
      print(f"  Systolic Blood Pressure: {visit[4]} mmHg")
      print(f"  Diastolic Blood Pressure: {visit[5]} mmHg")
      print(f"  Oxygen Saturation: {visit[6]} %")


# This function will show out the average of the vital details of a patient
def averag(data: list) -> list:
  averages = []
  length = len(data)
  # This will loop over all data expect the date
  for i in range(1, len(data[0])):
    column_sum = sum([row[i] for row in data])
    column_average = column_sum / length
    averages.append(round(column_average, 2))
  return averages


def displayStats(patients, patientId=0):

  try:
    data = patients.get(int(patientId))
    # a condition to check out weather a valid integer is passed or not
    if (int(patientId) >= 0):
      if patientId == "0":
        print("Vital Signs for All Patients:")
        patient_li = []
        # looping over the data of all the patients
        for i in patients:
          for patient_data in patients[i]:
            # Storing all data in a list
            patient_li.append(patient_data)
        avg = averag(patient_li)
        print(f"  Average Temperature: {avg[0]} C")
        # Average temperature: 37.00 C
        print(f"  Average Heart Rate: {avg[1]} bpm")
        print(f"  Average Respiratory Rate: {avg[2]} bpm")
        print(f"  Average Systolic Blood Pressure: {avg[3]} mmHg")
        print(f"  Average Diastolic Blood Pressure: {avg[4]} mmHg")
        print(f"  Average Oxygen Saturation: {avg[5]} %")

      elif data is None:
        print(f"Patient with ID {patientId} not found.")
      # Print individual data
      else:

        avg = averag(data)
        print(f"Vital Signs for Patient {patientId}:")
        print(f"  Average Temperature: {avg[0]} C")
        # Average temperature: 37.00 C
        print(f"  Average Heart Rate: {avg[1]} bpm")
        print(f"  Average Respiratory Rate: {avg[2]} bpm")
        print(f"  Average Systolic Blood Pressure: {avg[3]} mmHg")
        print(f"  Average Diastolic Blood Pressure: {avg[4]} mmHg")
        print(f"  Average Oxygen Saturation: {avg[5]} %")

  except:
    print("Error: 'patientId' should be an integer.")


def addPatientData(patients, patientId, date, temp, hr, rr, sbp, dbp, spo2,
                   fileName):
  dates = date.split("-")
  # Validating the date
  if (int(dates[1]) < 1 or int(dates[1]) > 12 or int(dates[2]) < 1
      or int(dates[2]) > 31):
    print("Invalid date. Please enter a valid date.")
# To check the temperature value is  within the range of 30 to 43
  elif temp < 30 or temp > 43:
    print(
      "Invalid temperature. Please enter a temperature between 30 and 43 Celsius."
    )

  # To check the heart rate value is not within the range of 30 to 200
  elif hr < 30 or hr > 200:
    print(
      "Invalid heart rate. Please enter an heart rate between 30 and 200 bpm.")

  # To check weather the respiratory rate value is  within the range of 5 to 60
  elif rr < 5 or rr > 60:
    print(
      "Invalid respiratory rate. Please enter a respiratory rate between 5 and 60 breaths per minute."
    )

  # To check weather the systolic blood pressure value is  within the range of 50 to 250
  elif sbp < 50 or sbp > 250:
    print(
      "Invalid systolic blood pressure. Please enter a systolic blood pressure between 50 and 250 mmhg."
    )

  # To check weather the diastolic blood pressure value is  within the range of 30 to 150
  elif dbp < 30 or dbp > 150:
    print(
      "Invalid diastolic blood pressure. Please enter a diastolic blood pressure between 30 and 150 mmhg."
    )

  # To check weather the oxygen saturation value is within  the range of 80 to 100
  elif spo2 < 80 or spo2 > 100:
    print(
      "Invalid oxygen saturation. Please enter an oxygen saturation between 70 and 100%."
    )
  else:
    if patientId not in patients:
      patients[patientId] = []
    patients[patientId].append([date, temp, hr, rr, sbp, dbp, spo2])
    with open('patients.txt', 'w') as f:
      # Write to the text  file
      for patient in patients:
        records = patients[patient]
        for data in records:
          f.write(
            f"{patient},{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n"
          )
    print(f"Visit saved for Patient # {patientId}")


# function to find the patients by date


def findVisitsByDate(patients, year=None, month=None):
  patient_list = []
  # Checking weather the date is valid or not
  if year != None and month != None:
    # This conditional will be executed  when nor date or month is provided
    if (len(str(year)) != 4) or int(month) > 12 or int(month) < 0:
      return (None)
    else:
      for patient in patients:
        datas = patients[patient]
        for record in datas:
          date = record[0].split("-")
          if (int(date[0]) == year) and int(date[1]) == month:
            patient_list.append((patient, record))
      return (patient_list)
  # Incase year is not given
  elif (year == None):
    # This conditional is executed when only month is provided
    for patient in patients:
      datas = patients[patient]
      for record in datas:
        date = record[0].split("-")
        if int(date[1]) == month:
          patient_list.append((patient, record))
    return (patient_list)
  # Incase the month is not given
  elif (month == None):
    # This conditional is executed when only year is provided
    for patient in patients:
      datas = patients[patient]
      for record in datas:
        date = record[0].split("-")
        if int(date[0]) == year:
          patient_list.append((patient, record))
    return (patient_list)
  else:
    # Looping over patient data
    for patient in patients:
      datas = patients[patient]
      for record in datas:
        # Splitting the date to validate weather it is correct or not
        date = record[0].split("-")
        patient_list.append((patient, record))
    return (patient_list)


# a function to check for patients who need follow up
def findPatientsWhoNeedFollowUp(patients):
  follow_up_list = []
  for patient in patients:
    data = patients.get(patient)
    for record in data:
      # Condition to check out the conditions and break out if there is abnormal coditions

      heart_rate = record[2]
      systolic_pressure = record[4]
      diastolic_pressure = record[5]
      oxygen_level = record[6]
      # Condition to check out the conditions of heart rate
      if (heart_rate > 100) or (heart_rate < 60):
        follow_up_list.append(patient)
        break
      # Condition to check out the conditions of systolic blood preesure
      elif (systolic_pressure > 140):
        follow_up_list.append(patient)
        break
      # Condition to check out the conditions of diastolic blood preesure
      elif (diastolic_pressure > 90):
        follow_up_list.append(patient)
        break
      # Condition to check out the conditions of oxygen leve
      elif (oxygen_level < 90):
        follow_up_list.append(patient)
        break
      else:
        pass
  return (follow_up_list)


def deleteAllVisitsOfPatient(patients, patientId, filename):
  # A try except block to catch error in case there is no patients
  try:
    del patients[patientId]
    print(f"Data for patient {patientId} has been deleted.")

    # It is being written in format patientId,date,temp,hr,rr,sbp,dbp,spo2\n
    with open('patients.txt', 'w') as f:
      # Write to the text  file
      for patient in patients:
        # Looping over patient data
        records = patients[patient]
        for data in records:
          f.write(
            f"{patient},{data[0]},{data[1]},{data[2]},{data[3]},{data[4]},{data[5]},{data[6]}\n"
          )
  # This will be executed when there will be no patient
  except:
    print(f"No data found for patient with ID {patientId}")


###########################################################################
###########################################################################
#   The following code is being provided to you. Please don't modify it.  #
#   If this doesn't work for you, use Google Colab,                       #
#   where these libraries are already installed.                          #
###########################################################################
###########################################################################


def main():
  patients = readPatientsFromFile('patients.txt')
  while True:
    print("\n\nWelcome to the Health Information System\n\n")
    print("1. Display all patient data")
    print("2. Display patient data by ID")
    print("3. Add patient data")
    print("4. Display patient statistics")
    print("5. Find visits by year, month, or both")
    print("6. Find patients who need follow-up")
    print("7. Delete all visits of a particular patient")
    print("8. Quit\n")

    choice = input("Enter your choice (1-8): ")
    if choice == '1':
      displayPatientData(patients)
    elif choice == '2':
      patientID = int(input("Enter patient ID: "))
      displayPatientData(patients, patientID)
    elif choice == '3':
      patientID = int(input("Enter patient ID: "))
      date = input("Enter date (YYYY-MM-DD): ")
      try:
        temp = float(input("Enter temperature (Celsius): "))
        hr = int(input("Enter heart rate (bpm): "))
        rr = int(input("Enter respiratory rate (breaths per minute): "))
        sbp = int(input("Enter systolic blood pressure (mmHg): "))
        dbp = int(input("Enter diastolic blood pressure (mmHg): "))
        spo2 = int(input("Enter oxygen saturation (%): "))
        addPatientData(patients, patientID, date, temp, hr, rr, sbp, dbp, spo2,
                       'patients.txt')
      except ValueError:
        print("Invalid input. Please enter valid data.")
    elif choice == '4':
      patientID = input("Enter patient ID (or '0' for all patients): ")
      displayStats(patients, patientID)
    elif choice == '5':
      year = input("Enter year (YYYY) (or 0 for all years): ")
      month = input("Enter month (MM) (or 0 for all months): ")
      visits = findVisitsByDate(patients,
                                int(year) if year != '0' else None,
                                int(month) if month != '0' else None)
      if visits:
        for visit in visits:
          print("Patient ID:", visit[0])
          print(" Visit Date:", visit[1][0])
          print("  Temperature:", "%.2f" % visit[1][1], "C")
          print("  Heart Rate:", visit[1][2], "bpm")
          print("  Respiratory Rate:", visit[1][3], "bpm")
          print("  Systolic Blood Pressure:", visit[1][4], "mmHg")
          print("  Diastolic Blood Pressure:", visit[1][5], "mmHg")
          print("  Oxygen Saturation:", visit[1][6], "%")
      else:
        print("No visits found for the specified year/month.")
    elif choice == '6':
      followup_patients = findPatientsWhoNeedFollowUp(patients)
      if followup_patients:
        print("Patients who need follow-up visits:")
        for patientId in followup_patients:
          print(patientId)
      else:
        print("No patients found who need follow-up visits.")
    elif choice == '7':
      patientID = input("Enter patient ID: ")
      deleteAllVisitsOfPatient(patients, int(patientID), "patients.txt")
    elif choice == '8':
      print("Goodbye!")
      break
    else:
      print("Invalid choice. Please try again.\n")


if __name__ == '__main__':
  main()
