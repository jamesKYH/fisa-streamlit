import streamlit as st 

# 데이터 정의
ani_list = ['짱구는못말려', '몬스터','릭앤모티']
img_list = ['https://i.imgur.com/t2ewhfH.png', 
            'https://i.imgur.com/ECROFMC.png', 
            'https://i.imgur.com/MDKQoDc.jpg']

a = st.text_input("검색할 애니메이션을 입력하세요")






for ani in ani_list:
    if a in ani:
        img_idx=ani_list.index(ani)
        break
if a != '':
    st.image(img_list[img_idx])

# for ani, img in zip(ani_list, img_list):
#     if a in ani: 
#         st.text(f"검색 결과: {ani}")
#         st.image(img)
#         break