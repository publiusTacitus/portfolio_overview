
import streamlit as st

# ---------------------------------------------------------
# Titel
# ---------------------------------------------------------

st.set_page_config(page_title="Portfolio Überblick", layout="wide")

st.title("Portfolio Überblick", text_alignment="center")

st.header("Projektliste mit exemplarischer Vorschau", text_alignment="center")

# ---------------------------------------------------------
# Überblick
# ---------------------------------------------------------

st.markdown("---")

st.space("xxsmall")


with st.container(horizontal_alignment="center"):
        st.subheader("KANTGYM – Automatisierte Active-Directory-Umgebung", text_alignment="center")

        st.markdown(
            """Automatisierte Active-Directory-Umgebung für ein fiktives Gymnasium.""",
            text_alignment="center"
        )

        r1, s1 = st.columns(2)

        with r1:
            with st.container(horizontal_alignment="center"):
                st.link_button(
                    "README",
                    "https://github.com/publiusTacitus/active_directory_kantgym",
                    use_container_width=False
                )

            with s1:
                with st.container(horizontal_alignment="center"):
                    st.link_button(
                        "Webpage",
                        "https://kantgym.streamlit.app/",
                        use_container_width=False
                    )

        st.image("previews/benutzerdaten_pipeline.png")


st.space("xxsmall")

col1, col2 = st.columns(2)

with st.container(horizontal_alignment="center"):
    with col1:

        st.subheader("Analysis: Comparative Political Data Set (1960–2022)", text_alignment="center")

        st.markdown(
            """
            Untersuchung des Zusammenhangs zwischen Wirtschaftsindikatoren, Staatsausgaben und Wahlergebnissen.
            """,
            text_alignment="center"
        )

        r2, s2 = st.columns(2)

        with r2:
            with st.container(horizontal_alignment="center"):
                st.link_button(
                    "README",
                    "https://github.com/publiusTacitus/comp_political_data_analysis",
                    use_container_width=False
                )

            with s2:
                with st.container(horizontal_alignment="center"):
                    st.link_button(
                        "Dashboard",
                        "https://comppoliticaldataanalysis.streamlit.app/?lang=de",
                        use_container_width=False
                    )

        st.image("previews/comp_political_data_analysis.png")


    with col2:

        st.subheader("Simulated Airline Database Portal", text_alignment="center")

        st.markdown(
            """Simulierte relationale Datenbank für Übungen und Projekte im Bereich Datenanalyse.""",
            text_alignment="center"
        )

        r3, s3 = st.columns(2)

        with r3:
            with st.container(horizontal_alignment="center"):
                st.link_button(
                    "README",
                    "https://github.com/publiusTacitus/simulated_airline_database",
                    use_container_width=False
                )

            with s3:
                with st.container(horizontal_alignment="center"):
                    st.link_button(
                        "Webpage",
                        "https://simulatedairlinedatabase.streamlit.app/",
                        use_container_width=False
                    )

        with st.container(horizontal_alignment="center"):
            st.image("previews/database_portal.png")


st.space("xxsmall")

col3, col4 = st.columns(2)

with st.container(horizontal_alignment="center"):
    with col3:

        st.subheader("Kundensegmente und Buchungsverhalten", text_alignment="center")

        st.markdown(
            """
            Analyse des Verhaltens verschiedener Kundensegmente im Buchungsumfeld einer Fluggesellschaft.
            """,
            text_alignment="center"
        )

        r4, s4 = st.columns(2)

        with r4:
            with st.container(horizontal_alignment="center"):
                st.link_button(
                    "README",
                    "https://github.com/publiusTacitus/customer_segments_booking_behavior",
                    use_container_width=False
                )

            with s4:
                with st.container(horizontal_alignment="center"):
                    st.link_button(
                        "Dashboard",
                        "https://customersegmentsbookingbehavior.streamlit.app/?lang=de",
                        use_container_width=False
                    )

        with st.container(horizontal_alignment="center"):
            st.image("previews/customer_segments_booking_behavior.png")


    with col4:

        st.subheader("Analyse: Flugstreckennachfrage", text_alignment="center")

        st.markdown(
            """Detaillierte Analyse des Nachfrageverhaltens auf Flugstrecken.""",
            text_alignment="center"
        )

        r5, s5 = st.columns(2)

        with r5:
            with st.container(horizontal_alignment="center"):
                st.link_button(
                    "README",
                    "https://github.com/publiusTacitus/flight_route_demand_analysis",
                    use_container_width=False
                )

            with s5:
                with st.container(horizontal_alignment="center"):
                    st.link_button(
                        "Dashboard",
                        "https://flightroutedemandanalysis.streamlit.app/?lang=de",
                        use_container_width=False
                    )

        with st.container(horizontal_alignment="center"):
            st.image("previews/flight_route_demand_analysis.png")


# ---------------------------------------------------------
# GitHub-Repository
# ---------------------------------------------------------

st.space("xxsmall")

st.markdown("---")

with st.container(horizontal_alignment="center"):

        st.link_button(
            "Projektüberblick auf GitHub",
            "https://github.com/publiusTacitus/portfolio_overview",
            use_container_width=False
        )

        st.markdown("Jan H. Schüttler", text_alignment="center")