import streamlit as st

def main():
    st.set_page_config(page_title="Aurasports Analytics Dashboard", page_icon="📊", layout="wide")

    st.title("📊 Aurasports Analytics Dashboard")

    sports = {
        "NFL - Football": "🏈",
        "NBA - Basketball": "🏀",
        "MLB - Baseball": "⚾",
        "NHL - Hockey": "🏒"
    }

    analysis_types = ["General Analytics", "Injury Risk Prediction"]

    col1, col2 = st.columns(2)

    with col1:
        selected_sport = st.selectbox("Select a sport:", list(sports.keys()))

    with col2:
        selected_analysis = st.selectbox("Select analysis type:", analysis_types)

    if selected_sport and selected_analysis:
        emoji = sports[selected_sport]
        st.write(f"You selected: {emoji} {selected_sport} - {selected_analysis}")

        # Generate a mock URL based on the selections
        url = f"https://your-aurasports-app.streamlit.app/{selected_sport.split(' - ')[0].lower()}/{selected_analysis.lower().replace(' ', '-')}"
        
        st.markdown(f"**[Click here to go to the {selected_sport} {selected_analysis} Dashboard]({url})**")

        st.write("---")
        st.write("Dashboard description:")
        
        if selected_analysis == "General Analytics":
            if selected_sport == "NFL - Football":
                st.write("Explore NFL statistics, player performance, and team analytics.")
            elif selected_sport == "NBA - Basketball":
                st.write("Dive into NBA player stats, team comparisons, and game predictions.")
            elif selected_sport == "MLB - Baseball":
                st.write("Analyze MLB batting averages, pitching stats, and team standings.")
            elif selected_sport == "NHL - Hockey":
                st.write("Track NHL player performance, team rankings, and game statistics.")
        else:  # Injury Risk Prediction
            st.write(f"Assess and predict injury risks for {selected_sport.split(' - ')[0]} players using advanced machine learning models.")
            st.write("- Player-specific injury risk assessments")
            st.write("- Historical injury data analysis")
            st.write("- Predictive models for injury prevention")

if __name__ == "__main__":
    main()