import streamlit as st


# 创建自定义的CSS类
st.write(
    """
    <style>
    .grid-container {
        display: grid;
        grid-template-columns: 1fr 2fr;
    }
    .sidebar {
        grid-column: 1;
    }
    .content {
        grid-column: 2;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# 创建一个 div 元素来应用样式
st.write('<div class="grid-container">', unsafe_allow_html=True)

# 放置 sidebar 内容
st.write('<div class="sidebar">', st.sidebar, '</div>', unsafe_allow_html=True)

# 放置主内容
st.write('<div class="content">', "主要内容", '</div>', unsafe_allow_html=True)

# 关闭 grid-container
st.write('</div>', unsafe_allow_html=True)