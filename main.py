import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import plotly.express as px

st.set_page_config(page_title="Tech Stack Recommender", page_icon="🧠", layout="wide")

st.title("🧠 AI Recommendation Engine")
st.markdown("### DecodeLabs · Project 3 · Tech Stack Recommender")
st.markdown("---")

@st.cache_data
def load_data():
    df = pd.read_csv('raw_Skills.csv')
    vectorizer = TfidfVectorizer()
    job_skills_matrix = vectorizer.fit_transform(df['Skills'])
    
    all_skills = set()
    for skills in df['Skills']:
        for skill in skills.split(','):
            all_skills.add(skill.strip())
    
    return df, vectorizer, job_skills_matrix, sorted(list(all_skills))

try:
    df, vectorizer, job_skills_matrix, all_skills = load_data()
    st.success(f"Loaded {len(df)} job roles")
except:
    st.error("raw_Skills.csv not found!")
    st.stop()

with st.sidebar:
    st.header("About")
    st.info("Content-Based Filtering using TF-IDF and Cosine Similarity")
    st.metric("Job Roles", len(df))
    st.metric("Unique Skills", len(all_skills))

col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("Enter Your Skills")
    skills_input = st.text_area(
        "Enter skills (comma-separated):",
        placeholder="Example: Python, Cloud Computing, Automation, Docker",
        height=100
    )

with col2:
    st.subheader("Settings")
    top_n = st.slider("Number of recommendations:", 1, 10, 3)
    recommend_btn = st.button("Get Recommendations", type="primary")

if recommend_btn:
    if not skills_input:
        st.warning("Please enter at least one skill!")
    else:
        with st.spinner("Finding your perfect match..."):
            user_vector = vectorizer.transform([skills_input])
            similarity_scores = cosine_similarity(user_vector, job_skills_matrix)
            
            df_copy = df.copy()
            df_copy['Similarity'] = similarity_scores[0]
            recommendations = df_copy.sort_values('Similarity', ascending=False).head(top_n)
            
            st.markdown("---")
            st.subheader(f"Top {len(recommendations)} Career Recommendations")
            
            for idx, (_, row) in enumerate(recommendations.iterrows()):
                emojis = ["🥇", "🥈", "🥉", "4️⃣", "5️⃣"]
                emoji = emojis[idx] if idx < len(emojis) else f"#{idx+1}"
                
                with st.expander(f"{emoji} {row['Job_Role']} - {row['Similarity']:.1%} match", expanded=True):
                    col1, col2 = st.columns([1, 3])
                    with col1:
                        st.metric("Match Score", f"{row['Similarity']:.1%}")
                    with col2:
                        st.write(f"Skills: {row['Skills']}")
                        st.progress(min(1.0, row['Similarity']))
            
            st.subheader("Similarity Chart")
            fig = px.bar(
                recommendations,
                x='Job_Role',
                y='Similarity',
                color='Similarity',
                color_continuous_scale='Blues',
                text_auto='.1%'
            )
            fig.update_layout(height=400, showlegend=False)
            st.plotly_chart(fig, use_container_width=True)
            
            csv = recommendations[['Job_Role', 'Skills', 'Similarity']].to_csv(index=False)
            st.download_button(
                label="Download CSV",
                data=csv,
                file_name="recommendations.csv",
                mime="text/csv"
            )

else:
    st.info("Enter your skills and click 'Get Recommendations'")
    
    with st.expander("Example"):
        st.markdown("""
        Input: Python, Cloud Computing, Automation, Docker
        
        Output:
        - Cloud Architect (87% match)
        - DevOps Engineer (76% match)
        - AI Engineer (58% match)
        """)

st.markdown("---")
st.markdown("Made with for DecodeLabs | Batch 2026")


