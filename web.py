import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] +"\n"
    # print(todo)
    todos.append(todo)
    functions.write_todos(todos)

st.title("my todo app")
st.subheader("This is my todo app")
st.write("my todos is: ")
for index, item in enumerate (todos):
    checkbox = st.checkbox(item, key=item )
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[item]
        st.rerun()


st.text_input(label="Enter an item", placeholder="Enter an item", on_change=add_todo, key='new_todo')
print("hello")
# st.session_state