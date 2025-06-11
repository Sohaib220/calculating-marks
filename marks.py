import gradio as gr
import sqlite3
import atexit





"""c.execute('''CREATE TABLE IF NOT EXISTS grades
             (name TEXT, English_III TEXT, Software_Engineering_I TEXT, Database_Management_System TEXT, 
              Mobile_Application_Development TEXT, Information_Security TEXT, E_commerce TEXT, 
              Software_Engineering_II TEXT, IOT TEXT, Knowledge_Representation TEXT, 
              Cyber_Security_for_Business TEXT, Operation_Management TEXT, Multimedia_Technology TEXT, 
              course_mark REAL, year_rating REAL)''')
conn.commit()"""


def grade(name, course1, English_III, Software_Engineering_I, Database_Management_System,
          Mobile_Application_Development, Information_Security, E_commerce, course2,
          Software_Engineering_II, IOT, Knowledge_Representation, Cyber_Security_for_Business,
          Operation_Management, Multimedia_Technology):

    conn = sqlite3.connect('grades.db')
    c = conn.cursor()

    course1_grades = [English_III, Software_Engineering_I, Database_Management_System,
                      Mobile_Application_Development, Information_Security, E_commerce]
    course1_material = ["English_III", "Software_Engineering_I", "Database_Management_System",
                        "Mobile_Application_Development", "Information_Security", "E_commerce"]

    course2_grades = [Software_Engineering_II, IOT, Knowledge_Representation, Cyber_Security_for_Business,
                      Operation_Management, Multimedia_Technology]
    course2_material = ["Software_Engineering_II", "IOT", "Knowledge_Representation",
                        "Cyber_Security_for_Business", "Operation_Management", "Multimedia_Technology"]

    if (None in course1_grades) or (None in course2_grades):
        return "enter all the grades please !!"



    def calculate_grade(grades, material):
        number = 6
        total = 0
        failed_grade = []

        for i in range(len(grades)):
            if grades[i] == "راسب":
                number -= 1
                failed_grade.append(material[i])
            elif grades[i] == "مقبول":
                total += 50
            elif grades[i] == "متوسط":
                total += 60
            elif grades[i] == "جيد":
                total += 70
            elif grades[i] == "جيد جدا":
                total += 80
            else:
                total += 90

        if number == 0:
            return (total, failed_grade)
        else:
            return ((total / number), failed_grade)

    course1_avg, course1_failed = calculate_grade(course1_grades, course1_material)
    course2_avg, course2_failed = calculate_grade(course2_grades, course2_material)
    year_rating = 0.3 * ((course1_avg + course2_avg) / 2)
    the_result=(int((course1_avg + course2_avg) / 2)//10)*10
    the_result_mark=""
    if the_result==50:
        the_result_mark+="مقبول"
    elif the_result==60:
        the_result_mark+="متوسط"
    elif the_result==70:
        the_result_mark+="جيد"
    elif the_result==80:
        the_result_mark+="جيد جدا"
    else:
        the_result_mark+="امتياز"


    c.execute('INSERT INTO grades VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)',
              (name, English_III, Software_Engineering_I, Database_Management_System,
               Mobile_Application_Development, Information_Security, E_commerce,
               Software_Engineering_II, IOT, Knowledge_Representation,
               Cyber_Security_for_Business, Operation_Management, Multimedia_Technology,
               (course1_avg + course2_avg) / 2, year_rating))
    conn.commit()
    atexit.register(conn.close)
    if len(course1_failed) > 0 or len(course2_failed) > 0:
        if len(course1_failed) > 0 and len(course2_failed) > 0:
            return (f"hello {name} your rating is : {(course1_avg + course2_avg) / 2}\n"
                    f"your year result is : {the_result_mark}\n"
                    f"but you have failed in {', '.join(map(str, course1_failed))}, {', '.join(map(str, course2_failed))}\n"
                    "but don't worry I'm sure you can do it\n\n\n"
                    f"note : try to get on the subjects that you have failed result {the_result_mark} so your rating won't be effected")
        elif len(course1_failed) > 0:
            return (f"hello {name} your rating is : {(course1_avg + course2_avg) / 2}\n"
                    f"your year result is : {the_result_mark}\n"
                    f"but you have failed in {', '.join(map(str, course1_failed))}\n"
                    "but don't worry I'm sure you can do it"
                    f"note : try to get on the subjects that you have failed result {the_result_mark} so your rating won't be effected")
        else:
            return (f"hello {name} your rating is : {(course1_avg + course2_avg) / 2}\n"
                    f"your year result is : {the_result_mark}\n"
                    f"but you have failed in {', '.join(map(str, course2_failed))}\n"
                    "but don't worry I'm sure you can do it"
                    f"note : try to get on the subjects that you have failed result {the_result_mark} so your rating won't be effected")
    else:
        return (f"hello {name} your rating is : {(course1_avg + course2_avg) / 2}\n"
                f"your year result is : {the_result_mark}\n"
                f"and your year rating is : {year_rating}")


types_of_grade = ["راسب", "مقبول", "متوسط", "جيد", "جيد جدا", "امتياز"]

dark_theme_css = """
body {
    background-color: #1E1E1E;
    color: #FFFFF;
    font-family: Arial, sans-serif;
}
.gradio-container {
    background-color: #1E1E1E;
    color: #1E1E1E;
}
.gr-button {
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
}
.gr-button:hover {
    background-color: #1E1E1E;
}
.gr-box {
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
}
.gr-input input, .gr-output {
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
}
.gr-dropdown select {
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
}
.gr-markdown {
    background-color: #1E1E1E;
    color: #FFFFFF;
}
.gr-textbox input {
    background-color: #1E1E1E;
    color: #FFFFFF;
    border: 1px solid #1E1E1E;
}
"""


def submit_handler(name, *grades):
    output = grade(name, *grades)
    return output


interface = gr.Interface(
    fn=submit_handler,
    inputs=[
        gr.Textbox(label="Enter your name:"),
        gr.Markdown("Course1 marks:"),
        gr.Dropdown(label="English III", choices=types_of_grade),
        gr.Dropdown(label="Software Engineering I", choices=types_of_grade),
        gr.Dropdown(label="Database Management System", choices=types_of_grade),
        gr.Dropdown(label="Mobile Application Development", choices=types_of_grade),
        gr.Dropdown(label="Information Security", choices=types_of_grade),
        gr.Dropdown(label="E-commerce", choices=types_of_grade),
        gr.Markdown("Course2 marks:"),
        gr.Dropdown(label="Software Engineering II", choices=types_of_grade),
        gr.Dropdown(label="Internet of Things (IOT)", choices=types_of_grade),
        gr.Dropdown(label="Knowledge Representation", choices=types_of_grade),
        gr.Dropdown(label="Cyber Security for Business", choices=types_of_grade),
        gr.Dropdown(label="Operation Management", choices=types_of_grade),
        gr.Dropdown(label="Multimedia Technology", choices=types_of_grade)
    ],
    outputs=gr.Textbox(),
    examples=[["صهيب", "course1 marks:", "متوسط", "متوسط", "متوسط", "متوسط", "متوسط", "متوسط", "course 2 marks:",
               "متوسط", "متوسط", "متوسط", "متوسط", "متوسط", "متوسط"],
              ["احمد", "course1 marks:", "مقبول", "مقبول", "مقبول", "مقبول", "مقبول", "مقبول", "course 2 marks:",
               "مقبول", "مقبول", "مقبول", "مقبول", "مقبول", "مقبول"],
              ["امير باسم", "course1 marks:", "جيد جدا", "جيد جدا", "جيد جدا", "جيد جدا", "جيد جدا", "جيد جدا", "course 2 marks:",
              "جيد جدا", "جيد جدا", "جيد جدا", "جيد جدا", "جيد جدا", "جيد جدا"],
              ["امير اسامة", "course1 marks:", "جيد", "جيد", "جيد", "جيد", "جيد", "جيد", "course 2 marks:",
              "جيد", "جيد", "جيد", "جيد", "جيد", "جيد"],
              ["زين", "course1 marks:", "امتياز", "امتياز", "امتياز", "امتياز", "امتياز", "امتياز", "course 2 marks:",
              "امتياز", "امتياز", "امتياز", "امتياز", "امتياز", "امتياز"]
              ],
)

interface.launch(share=True)

