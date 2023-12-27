import tkinter as tk

class AdmissionForm:
    def __init__(self, master):
        self.master = master
        master.title("College Admission Form")

        # Labels and entry fields for student information
        self.name_label = tk.Label(master, text="Name:")
        self.name_label.grid(row=0, column=0)
        self.name_entry = tk.Entry(master)
        self.name_entry.grid(row=0, column=1)

        self.email_label = tk.Label(master, text="Email:")
        self.email_label.grid(row=1, column=0)
        self.email_entry = tk.Entry(master)
        self.email_entry.grid(row=1, column=1)

        # Add more fields as needed (e.g., phone, address, etc.)

        # Submit button
        self.submit_button = tk.Button(master, text="Submit", command=self.submit_form)
        self.submit_button.grid(row=2, column=0, columnspan=2)

    def submit_form(self):
        student_name = self.name_entry.get()
        student_email = self.email_entry.get()
        # Gather data from other fields as needed

        print("Admission form submitted for:")
        print("Name:", student_name)
        print("Email:", student_email)
        # Print data from other fields as needed

        # You can add logic here to save the data to a file or database

root = tk.Tk()
form = AdmissionForm(root)
root.mainloop()
