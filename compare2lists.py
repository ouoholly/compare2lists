import streamlit as st
############################################
## Page info
############################################

st.set_page_config(
    page_title="Compare 2 Lists of data | ouoholly's Tools", 
    page_icon="🔍"
    )

st.title("🔍 Compare 2 Lists of data")
st.markdown("""
+ The comparison is case-sensitive
+ Leading and trailing space for each item will be removed automatically
+ New line for a new item
""")

st.markdown("---")

col1, col2 = st.columns(2)
res1, res2 = st.columns(2)

############################################
## List 1
############################################

list1_name = col1.text_input('List 1 name:', 'Stocktake List')

txt1 = col1.text_area(f"`{list1_name}`", '''Apple
Bananna   
   Cat
Hi halo''', height=200)

txt1 = [txt1][0].split('\n')
txt1 = [s.strip() for s in txt1] #remove leading and trailing spaces

############################################
## List 2
############################################

list2_name = col2.text_input('List 2 name:', 'System Records')

txt2 = col2.text_area(f"`{list2_name}`",'''Cat
Apple
  Drink
apple juice
apple
What''', height=200)

txt2 = [txt2][0].split('\n') 
txt2 = [s.strip() for s in txt2] #remove leading and trailing spaces

############################################

#for checking, results of the textarea input, in list format
# col1.write(txt1)
# col2.write(txt2)

############################################
## Comparison result
############################################

col1.markdown("---")
col2.markdown("---")

res1.markdown(f"**Below are the items in `{list1_name}` but not in `{list2_name}`**")
in1_notin2 = list(set(txt1) - set(txt2))
in1_notin2 = '\n\r'.join(e for e in in1_notin2) #turn list to string

if not in1_notin2:
      res1.write("None. The two lists above are the same.")
else:
      res1.write(in1_notin2)

#######

res2.markdown(f"**Below are the items in `{list2_name}` but not in `{list1_name}`**")
in2_notin1 = list(set(txt2) - set(txt1))
in2_notin1 = '\n\r'.join(e for e in in2_notin1) #turn list to string

if not in2_notin1:
      res2.write("None. The two lists above are the same.")
else:
      res2.write(in2_notin1)


############################################
## footer
############################################

st.markdown("---")

footer="""
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.0.0/css/all.min.css"> 
<style>
a:link, a:visited{
  color:grey;
  text-decoration: none;}
a:hover, a:active {
  color:#229e85;
  text-decoration: none;}
}
</style>
<a href="https://github.com/ouoholly/compare2lists">View source on GitHub <i class="fa-brands fa-github"></i></a>

"""
st.markdown(footer,unsafe_allow_html=True)
