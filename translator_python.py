import streamlit as st
import requests
st.set_page_config(page_title="Translator",page_icon="🧑‍🤝‍🧑")
st.markdown("""
<style>
.st-at.st-au.st-av.st-aw.st-ae.st-ag.st-ah.st-af.st-c2.st-bo.st-c3.st-c4.st-c5.st-c6.st-am.st-an.st-ao.st-ap.st-c7.st-ar.st-as.st-bb.st-ax.st-ay.st-az.st-b0.st-b1 {
    width: 100%;
    text-align: center; 
    display: inline-block;
}
svg.st-cn.st-db.st-bb.st-dc.st-dd {
    display:none;
}
button.styles_terminalButton__JBj5T {
    display: none;
}
.row-widget.stButton{
    display: ruby-text; 
    width: fit-content;
    }
svg {
    display: none;
    color:none;
    background-color:none;
    pointer-events: none;
}
h1#translator {
    text-align: -webkit-center;
}
button.st-emotion-cache-iiif1v.ef3psqc4 {
    display: none;
}
button.st-emotion-cache-ztfqz8.ef3psqc5 {
    display: none;
}
.block-container.st-emotion-cache-1y4p8pa.ea3mdgi2 {
    padding: 0;
    margin:20px;
}
header.st-emotion-cache-18ni7ap.ezrtsby2 {
    display: none;
}
</style>
""",True)
def main():
    # from googletrans import Translator, LANGUAGES
    # l_list = list(LANGUAGES.values())
    
    # def change(text, dest):
    #     trans = Translator()
    #     trans1 = trans.translate(text, dest=dest)
    #     return trans1.text
    l_list=["h","k"]
    st.title("Translate")
    tex = st.text_area("", placeholder="Enter ...")
    len2 = st.selectbox("", l_list, key="2nd")
    if st.button("Translator"):
        if(tex!=""):
            st.markdown("<textarea rows='3' style='pointer-events: none;caret-color: transparent;background-color:gainsboro;min-width:100%;max-width:100%;outline:none;border-radius:10px;padding:1em;margin:0;' readonly >{Hello}</textarea>",True)
        else:
            st.warning("Enter some text ... ")
def check_internet_connection():
    try:
        response = requests.get("http://www.google.com", timeout=5)
        if response.status_code == 200:
            main()
        else:
            st.error("Check your internet connection ...")
    except requests.ConnectionError:
        st.error("Check your internet connection ...")
check_internet_connection()
