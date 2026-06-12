import streamlit as st
import os
from openai import OpenAI
import datetime
import json

# 设置页面的配置项
st.set_page_config(
    page_title="AI智能伴侣",
    page_icon="🤖",
    layout="wide",
    # 控制侧边栏的状态
    initial_sidebar_state="expanded",
    # 页面跳转
    menu_items={

    }
)

# 保存会话信息
def save_session_info():
    # 保存当前会话信息
    if st.session_state.session_time:
        # 构建会话对象
        session_object = {
            "name": st.session_state.name,
            "nature": st.session_state.nature,
            "session_time": st.session_state.session_time,
            "messages": st.session_state.messages
        }
        # 保存会话信息
        if not os.path.exists("session"):
            os.mkdir("session")
        with open(f"session/{st.session_state.session_time}.json", "w",encoding="utf-8") as f:
            json.dump(session_object, f, ensure_ascii=False, indent=2)

# 加载所有的会话列表信息

def load_session_list():
    if not os.path.exists("session"):
        return []
    session_list = []
    for file in os.listdir("session"):
        if file.endswith(".json"):
            with open(f"session/{file}", "r", encoding="utf-8") as f:
                session_object = json.load(f)
            session_name = file.replace(".json", "")
            session_list.append(session_name)
    session_list.sort(reverse=True)        
    return session_list
    
# 加载指定会话数据
def load_session(session_name):
    try:
        if os.path.exists(f"session/{session_name}.json"):
            with open(f"session/{session_name}.json", "r", encoding="utf-8") as f:
                session_object = json.load(f)
                st.session_state.current_session = session_name
                st.session_state.messages = session_object["messages"]
                st.session_state.name = session_object["name"]
                st.session_state.nature = session_object["nature"]
                st.session_state.session_time = session_object["session_time"]
    except Exception:
        st.error("加载会话数据失败")

# 删除会话信息
def delete_session(session_name):
    if os.path.exists(f"session/{session_name}.json"):
        os.remove(f"session/{session_name}.json")
        # 如果删除的是当前对话，则需要更新消息列表
        if session_name == st.session_state.current_session:
            st.session_state.messages = []
            st.session_state.name = "小爱"
            st.session_state.nature = "你很懒，回复都很少"
            st.session_state.session_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            st.session_state.current_session = st.session_state.session_time
        st.success("删除成功")

# 标题
st.title("AI智能伴侣")

# logo
st.logo(r'C:\Users\86189\Desktop\study\python\AI应用\picture\logo.jpg')

# 系统提示词
system_prompt = "你的名字是%s,你的性格是%s"

# 初始化聊天信息
if "messages" not in st.session_state:
    st.session_state.messages = []

# 初始化名称
if "name" not in st.session_state:
    st.session_state.name = "小爱"

# 初始化性格
if "nature" not in st.session_state:
    st.session_state.nature = "你很懒，回复都很少"

# 初始化会话时间标识
if "session_time" not in st.session_state:
    datetime_now = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
    st.session_state.session_time = datetime_now

# 初始化状态变量
if "current_session" not in st.session_state:
    st.session_state.current_session = st.session_state.session_time

# 展示聊天信息
# st.session_state.messages打开标签页创建，关闭标签页销毁；刷新页面不丢数据
for message in st.session_state.messages:
    if message["role"] == "user":
        st.chat_message("user").write(message["content"])
    elif message["role"] == "assistant":
        st.chat_message("assistant").write(message["content"])

# 创建与AI大模型交互的客户端对象        'DEEPSEEK_API_KEY'配置在环境变量
client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

# 侧边栏
with st.sidebar:
    st.subheader("AI控制面板")
    if st.button('新建会话',width='stretch',icon='💕'):
        # 保存会话信息
        save_session_info()

        # 创建新会话
        if st.session_state.messages:
            st.session_state.messages = []
            st.session_state.session_time = datetime.datetime.now().strftime("%Y%m%d%H%M%S")
            st.session_state.current_session = st.session_state.session_time
            save_session_info()
            # 重新运行程序
            st.rerun()

    st.text("历史会话")
    session_list = load_session_list()
    for session in session_list:
        col1,col2 = st.columns([4,1])
        with col1:
            # 三元条件判断：语法：值1 if 条件 else 值2
            if st.button(session,width="stretch",icon='🏁',key=f"load_{session}",type='primary' if session == st.session_state.current_session else 'secondary'):
                load_session(session)
                st.rerun()
        with col2:
            if st.button('',width="stretch",icon='❌',key=f"delete_{session}"):
                delete_session(session)
                st.rerun()

    # 分割线
    st.divider()

    st.subheader("伴侣信息")
    nick_name = st.text_input('名称',placeholder="请输入名称",value=st.session_state.name)
    if nick_name:
        st.session_state.name = nick_name
    nature = st.text_area("个性",placeholder="请输入个性",value=st.session_state.nature)
    if nature:
        st.session_state.nature = nature

# 输入框
prompt = st.chat_input("请输入你的问题:")
if prompt:
    # st.write(f"你: {prompt}")
    st.chat_message("user").write(prompt)
    # print(prompt)
    # 添加输入信息到会话中
    st.session_state.messages.append({"role": "user", "content": prompt})

    # 与AI大模型进行交互
    response = client.chat.completions.create(
        model="deepseek-v4-pro",
        messages=[
            {"role": "system", "content": system_prompt % (st.session_state.name, st.session_state.nature)},
            # 添加会话记忆信息
            *st.session_state.messages,
        ],
        stream=True,
        reasoning_effort="high",
        extra_body={"thinking": {"type": "enabled"}}
    )
    # 输出大模型返回的结果(非流式输出的解析方式)
    # print(response.choices[0].message.content)
    # st.chat_message("assistant").write(response.choices[0].message.content)

    # 保存大模型返回的结果
    # st.session_state.messages.append({"role": "assistant", "content": response.choices[0].message.content})


    # 输出大模型返回的结果(流式输出的解析方式)
    # 解决输出问题
    response_message = st.empty()
    full_response = ""
    for chunk in response:
        if chunk.choices[0].delta.content is not None:
            content = chunk.choices[0].delta.content
            full_response += content
            response_message.chat_message("assistant").write(full_response)
    st.session_state.messages.append({"role": "assistant", "content": full_response}) 

   