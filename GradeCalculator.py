import customtkinter

customtkinter.set_appearance_mode("system")
customtkinter.set_default_color_theme("green")

root = customtkinter.CTk()
root.geometry("300x425")

gradesList = [
	(92.50, "A"),
	(89.50, "A-"),
	(86.50, "B+"),
	(82.50, "B"),
	(79.50, "B-"),
	(76.50, "C+"),
	(72.50, "C"),
	(69.50, "C-"),
	(66.50, "D+"),
	(62.50, "D"),
	(55.00, "D-"),
	(00.00, "F"),
]

def getLetterGrade(percentGrade):
	for i in range(len(gradesList)):
		if percentGrade >= gradesList[i][0]:
			return gradesList[i][1]


##############################################################################

def calculateGrade():
	maxAssignmentScore = 0
	currentAssignmentScore = 0
	maxAssessmentScore = 0
	currentAssessmentScore = 0

	# Assignments
	try:
		currentAssignmentScore = float(assignmentsCurrentEntry.get())
	except:
		assignmentsCurrentEntry.configure(placeholder_text="That's not a number!")

	try:
		maxAssignmentScore = float(assignmentsMaxEntry.get())
	except:
		assignmentsMaxEntry.configure(placeholder_text="That's not a number!")

	# Assessments
	try:
		currentAssessmentScore = float(assessmentsCurrentEntry.get())
	except:
		assessmentsCurrentEntry.configure(placeholder_text="That's not a number!")

	try:
		maxAssessmentScore = float(assessmentsMaxEntry.get())
	except:
		assessmentsMaxEntry.configure(placeholder_text="That's not a number!")

	if maxAssignmentScore > 0 and maxAssessmentScore > 0:
		grade = (
				(currentAssessmentScore / maxAssessmentScore) * 80 +
				(currentAssignmentScore / maxAssignmentScore) * 20
		)
		resultLabel.configure(text=f"{grade}% | {getLetterGrade(grade)}")


##############################################################################

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=10, padx=10, fill="both", expand=True)

titleLabel = customtkinter.CTkLabel(
	master=frame,
	text="Enter Grade Info",
	font=("Exo", 25)
)

titleLabel.pack(pady=12, padx=10)

##############################################################################

# Assignments
assignmentsCurrentEntryTitle = customtkinter.CTkLabel(
	master=frame,
	text="Current assignments grade",
	font=("Exo", 15)
)

assignmentsCurrentEntry = customtkinter.CTkEntry(
	master=frame,
	placeholder_text="<number>",
	font=("Exo", 12)
)

assignmentsMaxEntryTitle = customtkinter.CTkLabel(
	master=frame,
	text="Maximum assignments grade",
	font=("Exo", 15)
)

assignmentsMaxEntry = customtkinter.CTkEntry(
	master=frame,
	placeholder_text="<number>",
	font=("Exo", 12)
)

assignmentsCurrentEntryTitle.pack(pady=2, padx=5)
assignmentsCurrentEntry.pack(pady=1, padx=5)
assignmentsMaxEntryTitle.pack(pady=2, padx=5)
assignmentsMaxEntry.pack(pady=1, padx=5)

##############################################################################

# Assessments
assessmentsCurrentEntryTitle = customtkinter.CTkLabel(
	master=frame,
	text="Current assessment grade",
	font=("Exo", 15)
)

assessmentsCurrentEntry = customtkinter.CTkEntry(
	master=frame,
	placeholder_text="<number>",
	font=("Exo", 12)
)

assessmentsMaxEntryTitle = customtkinter.CTkLabel(
	master=frame,
	text="Maximum assessment grade",
	font=("Exo", 15)
)

assessmentsMaxEntry = customtkinter.CTkEntry(
	master=frame,
	placeholder_text="<number>",
	font=("Exo", 12)
)

assessmentsCurrentEntryTitle.pack(pady=2, padx=10)
assessmentsCurrentEntry.pack(pady=1, padx=5)
assessmentsMaxEntryTitle.pack(pady=2, padx=10)
assessmentsMaxEntry.pack(pady=1, padx=5)

##############################################################################

# Interface
button = customtkinter.CTkButton(
	master=frame,
	text="Calculate grade",
	command=calculateGrade,
	font=("Exo", 15)
)
button.pack(pady=10, padx=5)

resultLabel = customtkinter.CTkLabel(
	master=frame,
	text="Result: ",
	font=("Exo", 15)
)
resultLabel.pack(pady=2, padx=10)

##############################################################################

root.mainloop()
