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

if "puzzle_4_attempts" not in st.session_state:
    st.session_state.puzzle_4_attempts = 0

if "puzzle_4_solved" not in st.session_state:
    st.session_state.puzzle_4_solved = False

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

def pink_animation():

    components.html(
        """
        <style>

        body {
            margin: 0;
            background: transparent;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        @keyframes fillPink {
            0%, 25% {
                background-color: rgba(245,245,245,0.5);
            }

            100% {
                background-color: #ff69b4;
            }
        }

        @keyframes bubble {
            0% {
                transform: translateY(0);
                opacity: 0;
            }

            30% {
                opacity: 1;
            }

            100% {
                transform: translateY(-55px);
                opacity: 0;
            }
        }

        @keyframes reveal {
            0%, 70% {
                opacity: 0;
            }

            100% {
                opacity: 1;
            }
        }

        .experiment {
            text-align: center;
            padding: 10px;
        }

        .beaker {
            position: relative;
            width: 110px;
            height: 125px;
            margin: 10px auto 15px auto;
            border-left: 4px solid #777;
            border-right: 4px solid #777;
            border-bottom: 4px solid #777;
            border-radius: 0 0 18px 18px;
            overflow: hidden;
        }

        .liquid {
            position: absolute;
            bottom: 0;
            width: 100%;
            height: 70%;
            animation: fillPink 2.5s forwards;
        }

        .bubble {
            position: absolute;
            bottom: 15px;
            width: 10px;
            height: 10px;
            border: 2px solid white;
            border-radius: 50%;
            animation: bubble 1.4s infinite;
        }

        .b1 {
            left: 25px;
            animation-delay: 0.1s;
        }

        .b2 {
            left: 52px;
            animation-delay: 0.5s;
        }

        .b3 {
            left: 75px;
            animation-delay: 0.9s;
        }

        .result {
            font-size: 22px;
            font-weight: bold;
            color: #e83e8c;
            animation: reveal 3s forwards;
        }

        .sensor {
            margin-top: 8px;
            font-size: 16px;
            animation: reveal 3.5s forwards;
        }

        </style>

        <div class="experiment">

            <div class="beaker">

                <div class="liquid"></div>

                <div class="bubble b1"></div>
                <div class="bubble b2"></div>
                <div class="bubble b3"></div>

            </div>

            <div class="result">
                🩷 PINK COLOR DETECTED
            </div>

            <div class="sensor">
                ✓ Optical sensor calibrated
            </div>

        </div>
        """,
        height=240
    )


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


    selected = {reagent_1, reagent_2}

    if st.button("🧪 MIX SELECTED REAGENTS", use_container_width=True):


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

            pink_animation()

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
# PUZZLE 4 — MAGNETIC LOCK
# ---------------------------

def puzzle_4():

    st.title("🧲 MAGNETIC LOCK")

    st.error("⚠️ SYSTEM 04 — MAGNETIC SECURITY ARRAY OFFLINE")

    st.write("""
    The final security lock is controlled by a triangular
    arrangement of magnetic moments.

    The interactions between neighboring spins are
    **antiferromagnetic**.

    The system attempts to align every neighboring pair
    in opposite directions.
    """)

    st.info("""
    🎯 **MISSION**

    Determine the orientation of the third spin
    that satisfies the magnetic interactions.
    """)

    st.subheader("Magnetic Array")

    components.html(
        """
        <style>

        body {
            margin: 0;
            background: transparent;
            font-family: Arial, sans-serif;
        }

        .triangle-container {
            position: relative;
            width: 320px;
            height: 230px;
            margin: 0 auto;
        }

        .triangle {
            position: absolute;
            left: 60px;
            top: 25px;
            width: 200px;
            height: 170px;
        }

        .line {
            position: absolute;
            height: 4px;
            background: #666;
            transform-origin: left center;
            border-radius: 3px;
        }

        .left-line {
            width: 175px;
            left: 100px;
            top: 20px;
            transform: rotate(120deg);
        }

        .right-line {
            width: 175px;
            left: 100px;
            top: 20px;
            transform: rotate(60deg);
        }

        .bottom-line {
            width: 175px;
            left: 13px;
            top: 170px;
        }

        .spin {
            position: absolute;
            font-size: 48px;
            font-weight: bold;
            z-index: 2;
        }

        .top-spin {
            left: 137px;
            top: 0px;
        }

        .left-spin {
            left: 35px;
            top: 155px;
        }

        .unknown-spin {
            right: 28px;
            top: 155px;
            font-size: 44px;
        }

        .label {
            position: absolute;
            font-size: 13px;
            color: #777;
        }

        .interaction {
            bottom: 0px;
            width: 100%;
            text-align: center;
        }

        </style>

        <div class="triangle-container">

            <div class="triangle">

                <div class="line left-line"></div>
                <div class="line right-line"></div>
                <div class="line bottom-line"></div>

            </div>

            <div class="spin top-spin">↑</div>

            <div class="spin left-spin">↓</div>

            <div class="spin unknown-spin">?</div>

            <div class="label interaction">
                Antiferromagnetic interactions
            </div>

        </div>
        """,
        height=260
    )

    st.write("""
    Two spins are already fixed.

    Select the orientation of the final spin:
    """)

    col1, col2 = st.columns(2)

    with col1:

        if st.button(
            "⬆️ SPIN UP",
            use_container_width=True
        ):

            st.session_state.puzzle_4_attempts += 1

            st.warning("""
            ⚠️ INTERACTION CONFLICT

            One neighboring interaction is satisfied,
            but another is not.

            The magnetic array remains unstable.
            """)

    with col2:

        if st.button(
            "⬇️ SPIN DOWN",
            use_container_width=True
        ):

            st.session_state.puzzle_4_attempts += 1

            st.warning("""
            ⚠️ INTERACTION CONFLICT

            One neighboring interaction is satisfied,
            but another is not.

            The magnetic array remains unstable.
            """)

    if st.session_state.puzzle_4_attempts >= 2:

        st.divider()

        st.error("""
        🚨 NO SPIN ORIENTATION SATISFIES ALL INTERACTIONS

        The security system cannot find a stable configuration.
        """)

        st.write("""
        Something else is happening in this triangular magnetic system...
        """)

        explanation = st.radio(
            "Identify the phenomenon:",
            [
                "Ferromagnetism",
                "Magnetic frustration",
                "Diamagnetism"
            ],
            index=None
        )

        if st.button(
            "SUBMIT DIAGNOSIS",
            use_container_width=True
        ):

            if explanation == "Magnetic frustration":

                st.session_state.puzzle_4_solved = True

            elif explanation is None:

                st.warning("Select a diagnosis first.")

            else:

                st.error("""
                ❌ INCORRECT DIAGNOSIS

                Examine the competing interactions again.
                """)

    if st.session_state.puzzle_4_solved:

        st.success("🧲 MAGNETIC FRUSTRATION DETECTED")

        st.write("""
        The triangular geometry prevents all
        antiferromagnetic interactions from being
        satisfied simultaneously.

        **MAGNETIC SECURITY ARRAY RESTORED.**

        **FINAL DIGIT RECOVERED: 9**
        """)

        st.info("""
        🔐 EMERGENCY CODE COMPLETE

        **4 — 1 — 6 — 9**
        """)

        if st.button(
            "GO TO EMERGENCY EXIT ➜",
            use_container_width=True
        ):
            st.session_state.stage = 5
            st.rerun()

# ---------------------------
# FINAL STAGE — EMERGENCY EXIT
# ---------------------------
def escape_animation():

    components.html(
        """
        <style>

        body {
            margin: 0;
            background: transparent;
            font-family: Arial, sans-serif;
            text-align: center;
        }

        @keyframes unlock {
            0%, 25% {
                opacity: 1;
            }
            30%, 100% {
                opacity: 0;
            }
        }

        @keyframes unlocked {
            0%, 30% {
                opacity: 0;
            }
            40%, 100% {
                opacity: 1;
            }
        }

        @keyframes openDoor {
            0%, 40% {
                transform: perspective(600px) rotateY(0deg);
            }

            100% {
                transform: perspective(600px) rotateY(-70deg);
            }
        }

        @keyframes reveal {
            0%, 70% {
                opacity: 0;
                transform: translateY(15px);
            }

            100% {
                opacity: 1;
                transform: translateY(0);
            }
        }

        .exit-scene {
            padding: 15px;
        }

        .status {
            position: relative;
            height: 35px;
            margin-bottom: 10px;
            font-size: 18px;
            font-weight: bold;
        }

        .locked {
            position: absolute;
            width: 100%;
            color: #d9534f;
            animation: unlock 3s forwards;
        }

        .unlocked {
            position: absolute;
            width: 100%;
            color: #28a745;
            opacity: 0;
            animation: unlocked 3s forwards;
        }

        .door-frame {
            position: relative;
            width: 150px;
            height: 210px;
            margin: 10px auto 20px auto;
            border: 7px solid #555;
            background: #fff6c7;
            perspective: 600px;
        }

        .door {
            position: absolute;
            width: 100%;
            height: 100%;
            background: #555;
            transform-origin: left center;
            animation: openDoor 3.5s forwards;
        }

        .handle {
            position: absolute;
            right: 15px;
            top: 100px;
            width: 12px;
            height: 12px;
            background: #ddd;
            border-radius: 50%;
        }

        .victory {
            font-size: 28px;
            font-weight: bold;
            animation: reveal 4s forwards;
        }

        .message {
            margin-top: 8px;
            font-size: 17px;
            animation: reveal 4.5s forwards;
        }

        </style>

        <div class="exit-scene">

            <div class="status">

                <div class="locked">
                    🔒 ACCESS CODE PROCESSING...
                </div>

                <div class="unlocked">
                    🔓 ACCESS GRANTED — DOOR UNLOCKED
                </div>

            </div>

            <div class="door-frame">

                <div class="door">
                    <div class="handle"></div>
                </div>

            </div>

            <div class="victory">
                🧪 YOU ESCAPED THE LAB!
            </div>

            <div class="message">
                All emergency systems restored.
            </div>

        </div>
        """,
        height=390
    )

def puzzle_5():

    st.title("🚪 EMERGENCY EXIT")

    st.error("🚨 FINAL SECURITY LOCK")

    st.write("""
    All laboratory systems have been restored.

    The emergency exit is now responding, but the door
    remains electronically locked.

    Enter the four-digit emergency code recovered
    throughout the laboratory.
    """)

    st.info("""
    🔐 **EMERGENCY OVERRIDE**

    Enter the recovered access code below.
    """)

    code = st.text_input(
        "Emergency code",
        max_chars=4,
        placeholder="_ _ _ _"
    )

    if st.button(
        "🔓 UNLOCK LAB",
        use_container_width=True
    ):

        if code.strip() == "4169":

            st.session_state.stage = 6
            st.rerun()

        else:

            st.error("""
            ❌ ACCESS CODE REJECTED

            Emergency exit remains locked.
            """)

def victory_screen():

    st.title("🔓 LABORATORY UNLOCKED")

    escape_animation()

    st.success("MISSION COMPLETE")

    st.write("""
    **Laboratory systems status**

    🔐 Security terminal — RESTORED  
    🔥 Furnace control — RESTORED  
    🧪 Emergency ventilation — RESTORED  
    🧲 Magnetic security array — RESTORED  
    🚪 Emergency exit — UNLOCKED
    """)

    st.divider()

    st.subheader("🎉 Congratulations!")

    st.write("""
    You successfully recovered all four security digits
    and escaped the laboratory.
    """)

    st.caption(
        "Explosions caused during escape: classified information. 💥"
    )

    st.balloons()
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

elif st.session_state.stage == 4:
    puzzle_4()

elif st.session_state.stage == 5:
    puzzle_5()

elif st.session_state.stage == 6:
    victory_screen()
