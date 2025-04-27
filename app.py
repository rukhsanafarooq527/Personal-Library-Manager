
import streamlit as st
import json
import os
import matplotlib.pyplot as plt

# File names
BOOKS_FILE = "books.json"
NOTES_FILE = "notes.json"

# Custom Theme
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

# Utility functions
def load_data(file_name):
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            return json.load(file)
    return []

def save_data(file_name, data):
    with open(file_name, "w") as file:
        json.dump(data, file)

# Book Management
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

def view_books(books):
    st.subheader("📚 Your Library")
    if books:
        for book in books:
            st.markdown(f"- **Title:** {book['title']}, **Author:** {book['author']}, **Year:** {book['year']}, **Genre:** {book['genre']}, **Status:** {'✅ Read' if book['read_status'] else '❌ Unread'}")
    else:
        st.info("📭 No books added yet.")

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

# Notes Management
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

def view_notes(notes):
    st.subheader("📝 Your Notes")
    if notes:
        for note in notes:
            st.markdown(f"### 📘 {note['subject']}")
            st.write(note['content'])
            st.markdown("---")
    else:
        st.info("📭 No notes added yet.")

# Main App
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

if __name__ == "__main__":
    main()



# Footer
st.markdown('<div class="footer">Made with ⋆❤️⋆ by Rukhsana Shaheen | rukhsanafsarooq527@gmail.com ⋆.˚🦋༘⋆</div>', unsafe_allow_html=True)






























