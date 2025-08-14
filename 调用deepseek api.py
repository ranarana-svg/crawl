from openai import OpenAI
api_key='sk-96536c45708e41b09ab64379fbe64bbd'
base_url='https://api.deepseek.com'
def PrintChar(text,delay=0.1):
    for char in text:
        print(char,end='',flush=True)
        time.sleep(delay)
    print()
def SendToDeepseek(say):
    print("正在验证身份，请稍等------")     
    client = OpenAI(api_key="sk-96536c45708e41b09ab64379fbe64bbd", base_url="https://api.deepseek.com")
    print("正在思考，请稍候————")
    response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "You are a helpful assistant"},
        {"role": "user", "content": say},
    ],
    stream=False
    )
    return response.choices[0].message.content
while True:
    myin=input("您请说：")
    if myin=="bye":
        print("欢迎下次使用")
        break
    resp=SendToDeepseek(myin)
    PrintChar(resp)
    print(resp)
    print("--------------------------------------")

