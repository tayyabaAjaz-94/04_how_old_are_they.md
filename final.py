import streamlit as st
import sqlite3

def create_database():
    conn = sqlite3.connect("ages.db")
    cursor = conn.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Friends (
            name TEXT PRIMARY KEY,
            age INTEGER
        )
    """)
    conn.commit()
    conn.close()

def insert_data(anton=21):
    beth = anton + 6
    chen = beth + 20
    drew = chen + anton
    ethan = chen
    
    data = [("Anton", anton), ("Beth", beth), ("Chen", chen), ("Drew", drew), ("Ethan", ethan)]
    
    conn = sqlite3.connect("ages.db")
    cursor = conn.cursor()
    
    for name, age in data:
        cursor.execute("INSERT OR REPLACE INTO Friends (name, age) VALUES (?, ?)", (name, age))
    
    conn.commit()
    conn.close()

def fetch_data():
    conn = sqlite3.connect("ages.db")
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Friends")
    data = cursor.fetchall()
    conn.close()
    return data

def main():
    st.title("Age Riddle Solver")
    
    option = st.radio("Choose an option:", [
        "View predefined ages",
        "Enter Anton's age and calculate"
    ])
    
    create_database()
    
    if option == "View predefined ages":
        insert_data()  # Default Anton's age as 21
        data = fetch_data()
        
        st.subheader("Stored Ages:")
        for name, age in data:
            st.write(f"**{name}** is **{age}** years old")
        
        st.success("Ages stored and displayed successfully!")
    
    elif option == "Enter Anton's age and calculate":
        anton = st.number_input("Enter Anton's Age", min_value=1, max_value=100, value=21, step=1)
        
        if st.button("Calculate Ages"):
            insert_data(anton)
            data = fetch_data()
            
            st.subheader("Calculated Ages:")
            for name, age in data:
                st.write(f"**{name}** is **{age}** years old")
            
            st.success("Ages stored and displayed successfully!")

if __name__ == '__main__':
    main()