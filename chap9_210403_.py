# file
import os
print(os.path.join("Users", "wish-", "python"))

# open, close
st = open("st.txt", "w", encoding="utf-8") # 日本語用
st.write("Hi! from Python")
st.close()