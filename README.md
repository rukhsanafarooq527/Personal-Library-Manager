# Personal-Library-Manager

Madrasa Library & Notes Manager using Streamlit with several useful features. Here's a detailed breakdown of the app’s functions and structure,
App Overview:
This app is divided into three main sections:

Book Management
Notes Management
Statistics
With this app, users can add, view, and manage their books and notes, as well as track library statistics such as the total number of books, read books, and unread books.

Code Breakdown:
1. Streamlit Setup and Theme:
def set_custom_theme():
    st.markdown(
        """
        <style>
        body, .stApp {
            background-color: #e9edc9;
            color: #344e41;
        }
        .css-1d391kg {
            background-color: #fefae0 !important;
            padding: 20px !important;
        }
        .stButton button {
            background-color: #588157 !important;
            color: #ffffff !important;
            border-radius: 8px;
            padding: 8px 20px;
            font-weight: bold;
            border: none;
        }
        .stButton button:hover {
            background-color: #344e41 !important;
        }
        .stTextInput input, .stNumberInput input, .stTextArea textarea {
            background-color: #d4a373 !important;
            color: #000000 !important;
            border-radius: 5px;
            padding: 5px;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )
This function sets a custom theme for the app, including the background color, button styles, and text input design.

2. Data Load and Save Functions:
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)
These two functions, load_data() and save_data(), handle storing and loading data in JSON files. When the app starts, it loads the books and notes, and when any updates are made, it saves the data.

3. Book Management Functions:
Add Book:

def add_book(books):
    st.subheader("📚 Add a Book")
    title = st.text_input("Title")
    author = st.text_input("Author")
    year = st.number_input("Publication Year", min_value=1000, max_value=9999, step=1)
    genre = st.text_input("Genre")
    read_status = st.radio("Have you read this book?", ("Yes", "No"))

    if st.button("➕ Add Book"):
        if title and author and genre:
            book = {
                "title": title,
                "author": author,
                "year": int(year),
                "genre": genre,
                "read_status": read_status == "Yes"
            }
            books.append(book)
            save_data(BOOKS_FILE, books)
            st.success(f"✅ Book '{title}' added successfully!")
            st.balloons()
        else:
            st.error("❌ Please fill all fields.")
This function allows users to add a book by entering the title, author, publication year, genre, and read status. Upon clicking "Add Book," the book is saved to the books.json file.

View Books:

def view_books(books):
    st.subheader("📚 Your Library")
    if books:
        for book in books:
            st.markdown(f"- *Title:* {book['title']}, *Author:* {book['author']}, *Year:* {book['year']}, *Genre:* {book['genre']}, *Status:* {'✅ Read' if book['read_status'] else '❌ Unread'}")
    else:
        st.info("📭 No books added yet.")
This function displays the list of books in the library.

Book Statistics:

def book_statistics(books):
    st.subheader("📊 Library Statistics")
    total = len(books)
    read = sum(book['read_status'] for book in books)
    unread = total - read

    st.write(f"Total Books: {total}")
    st.write(f"Read Books: {read}")
    st.write(f"Unread Books: {unread}")

    if total > 0:
        fig, ax = plt.subplots()
        ax.pie([read, unread], labels=["Read", "Unread"], autopct="%1.1f%%", colors=["#588157", "#d4a373"])
        st.pyplot(fig)
This function provides library statistics, showing the total number of books, the number of read books, and unread books, along with a pie chart representing the data.

4. Notes Management Functions:
Add Note:

def add_note(notes):
    st.subheader("📝 Add a Note (Madrasa)")
    subject = st.text_input("Subject / Dars Title")
    content = st.text_area("Note Content")

    if st.button("➕ Add Note"):
        if subject and content:
            note = {
                "subject": subject,
                "content": content
            }
            notes.append(note)
            save_data(NOTES_FILE, notes)
            st.success(f"✅ Note '{subject}' added successfully!")
        else:
            st.error("❌ Please fill all fields.")
This function allows users to add madrasa notes by entering the subject and content.

View Notes:

def view_notes(notes):
    st.subheader("📝 Your Notes")
    if notes:
        for note in notes:
            st.markdown(f"### 📘 {note['subject']}")
            st.write(note['content'])
            st.markdown("---")
    else:
        st.info("📭 No notes added yet.")
This function displays the saved notes, subject-wise.

Main App Loop:
def main():
    set_custom_theme()
    st.title("📚 Madrasa Library & Notes Manager")

    # Load Data
    books = load_data(BOOKS_FILE)
    notes = load_data(NOTES_FILE)

    # Sidebar Menu
    menu = st.sidebar.selectbox("Menu", ["Home", "Manage Books", "Manage Notes", "Statistics"])

    if menu == "Home":
        st.image("https://cdn-icons-png.flaticon.com/512/201/201623.png", width=150)
        st.write("Welcome to your personal Madrasa Library and Notes Manager!")
    elif menu == "Manage Books":
        action = st.radio("Select Action", ["Add Book", "View Books"])
        if action == "Add Book":
            add_book(books)
        else:
            view_books(books)
    elif menu == "Manage Notes":
        action = st.radio("Select Action", ["Add Note", "View Notes"])
        if action == "Add Note":
            add_note(notes)
        else:
            view_notes(notes)
    elif menu == "Statistics":
        book_statistics(books)
The main() function runs the app, and the sidebar allows users to choose whether they want to manage books, manage notes, view statistics, or go to the home page.

Footer:
st.markdown('<div class="footer">Made with ⋆❤⋆ by Rukhsana Shaheen | rukhsanafsarooq527@gmail.com ⋆.˚🦋༘⋆</div>', unsafe_allow_html=True)
The footer contains your app's signature and contact information.

Final Thoughts:
Book Management: Users can add, view, and track their books.
Notes Management: Users can add and view madrasa notes.
Statistics: Provides visual statistics on the library, including read and unread books.
This app provides a complete system for efficiently managing books and notes while allowing users to track their library with useful statistics.😊
