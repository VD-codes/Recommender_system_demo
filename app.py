import streamlit as st
import pickle
import pandas as pd #there is a problem that un pickle to pandas dataframes so use dictoinary

#


st.title("MOvie Recommmender system")
movies_dict=pickle.load(open('movie_dict.pkl','rb'))
#movies_names=movies_dict['title'].values
movies=pd.DataFrame(movies_dict)
similarity=pickle.load(open('similarity.pkl','rb'))


def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distances = similarity[movie_index]
    movies_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[
                  1:6]  # top 5 similar distances
    recommended_movies=[]
    for i in movies_list:
        recommended_movies.append(movies.iloc[i[0]].title)
    return recommended_movies


selected_movie = st.selectbox(
    'Select A Movie',
    (movies['title'].values))
#st.write('You selected:', option)



if st.button('RecommenD'):
    recommandations= recommend(selected_movie)
    for i in recommandations:
        st.write(i)