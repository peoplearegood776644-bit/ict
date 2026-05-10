import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

# Display user information as requested
st.set_page_config(page_title="Miller Indices Direction App")
st.title("Miller Indices Direction Visualizer")
st.sidebar.markdown(f"### Developed By:\n**Awais Ahmad**\n**Roll No: 25-ME-108**")

st.write("Enter the Miller indices [u v w] to visualize the crystallographic direction in a cubic unit cell.")

# Input fields for Miller indices
col1, col2, col3 = st.columns(3)
with col1:
    u = st.number_input("u", value=1, step=1)
with col2:
    v = st.number_input("v", value=1, step=1)
with col3:
    w = st.number_input("w", value=1, step=1)

# Visualization logic
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Draw a unit cube for reference
r = [0, 1]
for s, e in [(np.array([x, y, z]), np.array([x, y, z])) for x in r for y in r for z in r]:
    for i in range(3):
        target = s.copy()
        if target[i] == 0:
            target[i] = 1
            ax.plot3D(*zip(s, target), color="gray", linestyle="--", alpha=0.3)

# Define the direction vector [u v w]
# In crystallography, [uvw] is a vector sum of u*(1,0,0) + v*(0,1,0) + w*(0,0,1)
vector = np.array([u, v, w])
# Normalize for plotting within the unit cube if needed, or keep scale
ax.quiver(0, 0, 0, u, v, w, color='red', arrow_length_ratio=0.1, label=f'Direction [{u} {v} {w}]')

# Set labels and limits
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
ax.set_xlim([0, max(1, u)])
ax.set_ylim([0, max(1, v)])
ax.set_zlim([0, max(1, w)])
ax.legend()

st.pyplot(fig)

st.info("Note: Square brackets [uvw] denote a specific direction vector from the origin.")
