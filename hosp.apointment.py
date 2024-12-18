import tkinter as tk
from tkinter import messagebox

# PROJECT INFORMATION
print("\n---Project Information---")
print("NURUL AMNA ZAFIRAH BINTI MOHD ASHID")
print("2023620732")
print("Topic: Hospital Appointment System")

# HOSPITAL APPOINTMENT SYSTEM
appointments = []

# Functions for Appointment System
def create_appointment():
    patient_name = patient_name_var.get()
    doctor = doctor_var.get()
    appointment_date = date_var.get()
    reason = reason_var.get()

    if not (patient_name and doctor and appointment_date and reason):
        messagebox.showerror("Error", "All fields are required!")
        return

    id = len(appointments) + 1
    appointments.append({
        "id": id,
        "patient_name": patient_name,
        "doctor": doctor,
        "appointment_date": appointment_date,
        "reason": reason
    })
    messagebox.showinfo("Success", f"Appointment for {patient_name} created!")
    clear_fields()

def view_appointment():
    try:
        id = int(view_id_var.get())
        appointment = next((app for app in appointments if app["id"] == id), None)
        if appointment:
            result = (f"ID: {appointment['id']}\n"
                      f"Patient: {appointment['patient_name']}\n"
                      f"Doctor: {appointment['doctor']}\n"
                      f"Date: {appointment['appointment_date']}\n"
                      f"Reason: {appointment['reason']}")
            messagebox.showinfo("Appointment Details", result)
        else:
            messagebox.showerror("Error", "Appointment not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID!")

def update_appointment():
    try:
        id = int(update_id_var.get())
        appointment = next((app for app in appointments if app["id"] == id), None)
        if appointment:
            new_patient_name = update_patient_var.get() or appointment['patient_name']
            new_doctor = update_doctor_var.get() or appointment['doctor']
            new_date = update_date_var.get() or appointment['appointment_date']
            new_reason = update_reason_var.get() or appointment['reason']

            appointment.update({
                "patient_name": new_patient_name,
                "doctor": new_doctor,
                "appointment_date": new_date,
                "reason": new_reason
            })
            messagebox.showinfo("Success", f"Appointment ID {id} updated!")
            clear_update_fields()
        else:
            messagebox.showerror("Error", "Appointment not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID!")

def delete_appointment():
    try:
        id = int(delete_id_var.get())
        global appointments
        new_appointments = [app for app in appointments if app["id"] != id]
        if len(new_appointments) < len(appointments):
            appointments[:] = new_appointments
            messagebox.showinfo("Success", f"Appointment ID {id} deleted.")
        else:
            messagebox.showerror("Error", "Appointment not found.")
    except ValueError:
        messagebox.showerror("Error", "Invalid ID!")

def list_appointments():
    if appointments:
        result = "\n".join([f"ID: {app['id']}, Patient: {app['patient_name']}, Doctor: {app['doctor']}, "
                            f"Date: {app['appointment_date']}, Reason: {app['reason']}" for app in appointments])
        messagebox.showinfo("All Appointments", result)
    else:
        messagebox.showinfo("Info", "No appointments available.")

def clear_fields():
    patient_name_var.set("")
    doctor_var.set("")
    date_var.set("")
    reason_var.set("")
    view_id_var.set("")
    delete_id_var.set("")

def clear_update_fields():
    update_id_var.set("")
    update_patient_var.set("")
    update_doctor_var.set("")
    update_date_var.set("")
    update_reason_var.set("")

# Tkinter Window
root = tk.Tk()
root.title("Hospital Appointment System")
root.geometry("500x700")

# Variables
patient_name_var = tk.StringVar()
doctor_var = tk.StringVar()
date_var = tk.StringVar()
reason_var = tk.StringVar()
view_id_var = tk.StringVar()
delete_id_var = tk.StringVar()
update_id_var = tk.StringVar()
update_patient_var = tk.StringVar()
update_doctor_var = tk.StringVar()
update_date_var = tk.StringVar()
update_reason_var = tk.StringVar()

# Create Appointment
tk.Label(root, text="Create Appointment", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Patient Name").pack()
tk.Entry(root, textvariable=patient_name_var).pack()
tk.Label(root, text="Doctor").pack()
tk.Entry(root, textvariable=doctor_var).pack()
tk.Label(root, text="Appointment Date").pack()
tk.Entry(root, textvariable=date_var).pack()
tk.Label(root, text="Reason").pack()
tk.Entry(root, textvariable=reason_var).pack()
tk.Button(root, text="Create", command=create_appointment).pack(pady=10)

# View Appointment
tk.Label(root, text="View Appointment by ID", font=("Arial", 14)).pack(pady=10)
tk.Entry(root, textvariable=view_id_var).pack()
tk.Button(root, text="View", command=view_appointment).pack(pady=5)

# Update Appointment
tk.Label(root, text="Update Appointment by ID", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="Appointment ID").pack()
tk.Entry(root, textvariable=update_id_var).pack()
tk.Label(root, text="New Patient Name (Optional)").pack()
tk.Entry(root, textvariable=update_patient_var).pack()
tk.Label(root, text="New Doctor (Optional)").pack()
tk.Entry(root, textvariable=update_doctor_var).pack()
tk.Label(root, text="New Appointment Date (Optional)").pack()
tk.Entry(root, textvariable=update_date_var).pack()
tk.Label(root, text="New Reason (Optional)").pack()
tk.Entry(root, textvariable=update_reason_var).pack()
tk.Button(root, text="Update", command=update_appointment).pack(pady=5)

# Delete Appointment
tk.Label(root, text="Delete Appointment by ID", font=("Arial", 14)).pack(pady=10)
tk.Entry(root, textvariable=delete_id_var).pack()
tk.Button(root, text="Delete", command=delete_appointment).pack(pady=5)

# List All Appointments
tk.Button(root, text="List All Appointments", command=list_appointments).pack(pady=10)

# Run Tkinter Loop
root.mainloop()
