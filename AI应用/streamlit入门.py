import streamlit as st
# 设置页面的配置项
st.set_page_config(
    page_title="streamlit入门",
    page_icon="🧊",
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
    # 页面跳转
    menu_items={
        'Get Help': 'https://www.extremelycoolapp.com/help',
        'Report a bug': "https://www.extremelycoolapp.com/bug",
        'About': "# This is a header. This is an *extremely* cool app!"
    }
)

st.title('Streamlit 入门')

# 文字
st.write('DeepSeek-V4 预览版本发布，具备世界顶级推理性能，Agent 能力大幅提高，已在网页端、APP 和 API 上线，点击查看详情')

# 图片
st.image('./picture/captcha.png')

# 音频
# st.audio('./picture/xxx.mp3')

# 视频
# st.video('./picture/xxx.mp4')


# logo
st.logo('./picture/captcha.png')


# 表格
student_data = {
    '姓名':['ccc','sss','fff'],
    '年龄':[22,33,44]
}
st.table(student_data)
# 输入框
name = st.text_input('请输入')
st.write(f'您输入的内容为:{name}')

# 密码框
password = st.text_input("请输入密码:" ,type="password")
st.write(f'您输入的密码为:{password}')

# 按钮
gender = st.radio('请输入你的性别',["男","女"],index=1)
st.write(f'性别为：{gender}')