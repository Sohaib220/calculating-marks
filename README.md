# 🎓 Calculating Marks – Yearly Grade Calculator

This project is a simple system for **entering, calculating, and saving university course grades** using **Python**, **Gradio**, and **SQLite**. It allows users to select their grades for various materials and instantly calculates their **average, year rating, and overall result** — then stores the data locally in a database.

---

## 📸 Demo & Screenshots

![](media/Gradio-interface.png)  

---

![](media/display-of-database.png)

---

## 🧠 Features

- ✅ Interactive **Gradio interface** for grade input
- ✅ Calculates **average grades** and **year rating**
- ✅ Saves all student data to a **local SQLite database**
- ✅ Displays messages in **Arabic** (including encouragement for failed subjects)
- ✅ Supports common Arabic grade levels: `راسب`, `مقبول`, `متوسط`, `جيد`, `جيد جدا`, `امتياز`
- ✅ Dark theme for clean UI
- ✅ View full results using a separate Python script

---

## 🛠️ Technologies Used

- 🐍 Python
- 🖼️ Gradio (for user interface)
- 🗃️ SQLite (for local data storage)

---

## 📁 Project Structure

```bash
.
├── marks.py           # Main Gradio app for entering and saving grades
├── degres_check.py    # Script to print out all saved student records
├── grades.db          # SQLite database file (auto-created on first run)
├── media/
│   ├── form-example.jpg
│   └── result-display.jpg

---

## 📁 How to use it

1. Download the two files and put it in any python editor.
2. Run the file marks.py it will give you two links local and public you can use the public link to share it with others and let them use it.
3. after any one use it you will notice that there is a new file that have been created in the same directory of the mark.py file which is the grades.db.
4. the grades.db will automaticlly save all the responses of the users.
5. after you finish you can run the file degres_check.py to read all the data in grades.db make sure the path is correct.
6. you can modify it to match your materials it is simple.
7. have fun.

---

Don't forgit to give me a ⭐ on this project if you liked it






