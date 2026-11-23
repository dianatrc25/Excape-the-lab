import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="Escape the Lab",
    page_icon="🧪",
    layout="centered"
)

# ---------------------------
# GAME STATE
# ---------------------------

if "stage" not in st.session_state:
    st.session_state.stage = 0

if "puzzle_1_solved" not in st.session_state:
    st.session_state.puzzle_1_solved = False

if "puzzle_2_solved" not in st.session_state:
    st.session_state.puzzle_2_solved = False

if "puzzle_3_solved" not in st.session_state:
    st.session_state.puzzle_3_solved = False
# ---------------------------
# INTRO
# ---------------------------

def intro():

    st.title("🧪 ESCAPE THE LAB")
    st.subheader("An Interactive Chemistry Escape Room")

    st.write("""
    It's 6:47 PM.

    Everyone else has left the chemistry building.

    You're finishing one last experiment when suddenly...
    """)

    st.error("🚨 LABORATORY LOCKDOWN INITIATED")

    st.write("""
    The laboratory's automated safety system has malfunctioned.

    The doors are locked.

    The furnace is still running.

    You must restore the laboratory systems before you can escape.
    """)

    if st.button("🔓 START GAME", use_container_width=True):

        st.session_state.stage = 1
        st.rerun()


# ---------------------------
# PUZZLE 1
# ---------------------------

def puzzle_1():

    st.title("🔐 SECURITY TERMINAL")

    st.warning("SYSTEM 01 — ACCESS LOCKED")

    st.write("""
    The laboratory security terminal has lost its access key.

    A message appears on the screen:
    """)

    st.info("""
    **IDENTIFY THE ELEMENT**

    • Atomic number: 64  
    • Period: 6  
    • f-block element  
    • Magnetic lanthanide
    """)

    answer = st.text_input(
        "Enter the chemical symbol:"
    )

    if st.button("UNLOCK TERMINAL", use_container_width=True):

        if answer.strip().lower() == "gd":
            st.session_state.puzzle_1_solved = True

        else:
            st.error("❌ ACCESS DENIED — Try again.")

    if st.session_state.puzzle_1_solved:

        st.success("✅ ACCESS GRANTED")

        st.write("""
        SECURITY SYSTEM RESTORED.

        **FIRST DIGIT RECOVERED: 4**
        """)

        if st.button("CONTINUE ➜", use_container_width=True):
            st.session_state.stage = 2
            st.rerun()

# ---------------------------
# PUZZLE 2 — FURNACE
# ---------------------------

def puzzle_2():

    st.title("🔥 FURNACE EMERGENCY")

    st.error("⚠️ SYSTEM 02 — TEMPERATURE CONTROL FAILURE")

    st.write("""
    The furnace is still running.

    A valuable crystal-growth experiment is trapped inside.

    You need to configure the cooling program correctly
    before the sample can be recovered.
    """)

    st.metric(
        label="CURRENT FURNACE TEMPERATURE",
        value="1050 °C"
    )

    st.subheader("Configure cooling program")

    target_temp = st.slider(
        "Target temperature (°C)",
        min_value=400,
        max_value=800,
        value=700,
        step=50
    )

    cooling_rate = st.slider(
        "Cooling rate (°C/hour)",
        min_value=1.0,
        max_value=10.0,
        value=5.0,
        step=0.5
    )

    st.write(f"""
    **Program selected**

    Target temperature: **{target_temp} °C**

    Cooling rate: **{cooling_rate} °C/hour**
    """)

    if st.button("🔥 ACTIVATE COOLING", use_container_width=True):

        if target_temp == 600 and cooling_rate == 3.0:
            st.session_state.puzzle_2_solved = True

        elif target_temp > 650:
            st.warning("""
            ⚠️ SAMPLE CANNOT BE RECOVERED

            Temperature is still too high.
            """)

        elif cooling_rate > 5:
            st.error("""
            🚨 COOLING RATE TOO FAST

            Crystal growth compromised.

            Reconfigure the furnace.
            """)

        else:
            st.error("""
            ❌ INCORRECT FURNACE PROGRAM

            Check the target temperature and cooling rate.
            """)

    if st.session_state.puzzle_2_solved:

        st.success("✅ COOLING PROGRAM ACCEPTED")

        st.progress(100)

        st.write("""
        Furnace stabilized.

        Sample recovery temperature reached.

        **SECOND DIGIT RECOVERED: 1**
        """)

        if st.button(
            "CONTINUE TO CHEMICAL STORAGE ➜",
            use_container_width=True
        ):
            st.session_state.stage = 3
            st.rerun()
# ---------------------------
# PUZZLE 3 — CHEMICAL STORAGE
# ---------------------------

def puzzle_3():

    st.title("🧪 CHEMICAL STORAGE")

    st.error("⚠️ SYSTEM 03 — EMERGENCY VENTILATION OFFLINE")

    st.write("""
    The ventilation system's optical chemical sensor has lost calibration.

    Three solutions were found inside the chemical cabinet.

    Your task is to produce a **PINK solution** to recalibrate the sensor.
    """)

    st.info("""
    🎯 **MISSION**

    Inspect the available reagents.

    Select **TWO** solutions that will produce the required color change.
    """)

    st.subheader("Chemical Cabinet")

    col1, col2, col3, col4 = st.columns(4)

    # -------- BOTTLE A --------
    with col1:
        st.markdown("### 🧪 Bottle A")
        st.markdown("**UNKNOWN SOLUTION**")
        st.caption("Label partially damaged")
        
        with st.expander("🔎 Inspect"):
            st.markdown("**IDENTIFICATION: Hydrochloric acid**")
            st.code("HCl(aq)")

            st.write("""
            **Type:** Acidic solution

            **Appearance:** Colorless

            **Chemical behavior:**  
            Strong acid in aqueous solution.
            """)

    # -------- BOTTLE B --------
    with col2:
        st.markdown("### 🧪 Bottle B")
        st.markdown("**UNKNOWN SOLUTION**")
        st.caption("Label partially damaged")

        with st.expander("🔎 Inspect"):
            st.markdown("**IDENTIFICATION: Sodium hydroxide**")
            st.code("NaOH(aq)")

            st.write("""
            **Type:** Basic solution

            **Appearance:** Colorless

           **Chemical behavior:**  
           Strong base in aqueous solution.
           """)

    # -------- BOTTLE C --------
    with col3:
        st.markdown("### 🧪 Bottle C")
        st.markdown("**UNKNOWN SOLUTION**")
        st.caption("Label partially damaged")
        
        with st.expander("🔎 Inspect"):
            st.markdown("**IDENTIFICATION: Phenolphthalein**")
            st.code("Acid–base indicator")

            st.write("""
            **Type:** Acid–base indicator

            **Appearance:** Colorless

            **Chemical behavior:**  
            Its color depends strongly on pH.
            """)

    # -------- BOTTLE D --------
    with col4:
        
        st.markdown("### 🧪 Bottle D")
        st.markdown("**UNKNOWN SOLUTION**")
        st.caption("⚠️ Hazard label intact")
        
        with st.expander("🔎 Inspect"):
            st.markdown("**IDENTIFICATION: Hydrogen peroxide**")
            st.code("H₂O₂(aq)")

            st.write("""
            **Type:** Oxidizing agent

            **Appearance:** Colorless

            **Safety information:**  
            ⚠️ Oxidizer — chemical compatibility
            must be checked before mixing.
            """)

    st.divider()

    st.subheader("Select reagents")

    reagent_1 = st.selectbox(
        "First reagent",
        ["Bottle A", "Bottle B", "Bottle C", "Bottle D"]
    )

    reagent_2 = st.selectbox(
        "Second reagent",
        ["Bottle A", "Bottle B", "Bottle C","Bottle D"],
        index=1
    )

    if st.button("🧪 MIX SELECTED REAGENTS", use_container_width=True):

        selected = {reagent_1, reagent_2}

        if reagent_1 == reagent_2:

            st.warning("""
            ⚠️ Select two different reagents.
            """)

        elif "Bottle D" in selected:

                        components.html(
                """
                <style>

                body {
                    margin: 0;
                    background: transparent;
                    overflow: hidden;
                    font-family: Arial, sans-serif;
                }

                @keyframes explosion {
                    0% {
                        transform: scale(0);
                        opacity: 0;
                    }

                    20% {
                        transform: scale(0.5);
                        opacity: 1;
                    }

                    45% {
                        transform: scale(3);
                        opacity: 1;
                    }

                    65% {
                        transform: scale(1.8);
                    }

                    100% {
                        transform: scale(1);
                    }
                }

                @keyframes shake {
                    0% { transform: translateX(0); }
                    10% { transform: translateX(-15px); }
                    20% { transform: translateX(15px); }
                    30% { transform: translateX(-15px); }
                    40% { transform: translateX(15px); }
                    50% { transform: translateX(-8px); }
                    60% { transform: translateX(8px); }
                    100% { transform: translateX(0); }
                }

                @keyframes smoke {
                    0% {
                        opacity: 0;
                        transform: translateY(25px) scale(0.5);
                    }

                    60% {
                        opacity: 0;
                    }

                    100% {
                        opacity: 1;
                        transform: translateY(-5px) scale(1);
                    }
                }

                @keyframes warning {
                    0%, 100% {
                        opacity: 1;
                    }

                    50% {
                        opacity: 0.25;
                    }
                }

                .explosion-box {
                    text-align: center;
                    padding: 20px;
                    animation: shake 0.8s ease-in-out;
                }

                .boom {
                    font-size: 90px;
                    line-height: 1.2;
                    animation: explosion 1s ease-out;
                }

                .warning-text {
                    margin-top: 10px;
                    font-size: 20px;
                    font-weight: bold;
                    color: #ff4b4b;
                    animation: warning 0.5s 3;
                }

                .smoke {
                    margin-top: 10px;
                    font-size: 40px;
                    animation: smoke 1.8s ease-out;
                }

                .message {
                    margin-top: 15px;
                    font-size: 16px;
                }

                </style>

                <div class="explosion-box">

                    <div class="boom">
                        💥
                    </div>

                    <div class="warning-text">
                        🚨 CHEMICAL INCOMPATIBILITY DETECTED 🚨
                    </div>

                    <div class="smoke">
                        ☁️ ☁️ ☁️
                    </div>

                    <div class="message">
                        Emergency safety system activated.
                        <br><br>
                        <b>That was definitely not the calibration solution.</b>
                    </div>

                </div>
                """,
                height=330
            )

        elif selected == {"Bottle B", "Bottle C"}:

            st.session_state.puzzle_3_solved = True

        elif selected == {"Bottle A", "Bottle C"}:

            st.info("""
            ⚪ NO COLOR CHANGE DETECTED

            The solution remains colorless.

            Optical sensor calibration failed.
            """)

        elif selected == {"Bottle A", "Bottle B"}:

            st.warning("""
            🌡️ TEMPERATURE CHANGE DETECTED

            An acid–base neutralization occurred,
            but no indicator is present to produce
            the required pink signal.

            Try another combination.
            """)

    if st.session_state.puzzle_3_solved:

        st.success("🩷 PINK COLOR DETECTED")

        st.write("""
        The phenolphthalein responds to the basic solution.

        Optical sensor calibrated.

        **EMERGENCY VENTILATION RESTORED.**

        **THIRD DIGIT RECOVERED: 6**
        """)

        if st.button("CONTINUE ➜", use_container_width=True):
            st.session_state.stage = 4
            st.rerun()

# ---------------------------
# GAME CONTROLLER
# ---------------------------

if st.session_state.stage == 0:
    intro()

elif st.session_state.stage == 1:
    puzzle_1()

elif st.session_state.stage == 2:
    puzzle_2()

elif st.session_state.stage == 3:
    puzzle_3()

