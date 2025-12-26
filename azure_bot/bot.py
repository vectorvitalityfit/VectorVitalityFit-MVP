from botbuilder.core import ActivityHandler, TurnContext
from botbuilder.schema import ChannelAccount

class BFRBot(ActivityHandler):
    async def on_message_activity(self, turn_context: TurnContext):
        text = turn_context.activity.text.lower()
        # Greetings
        if re.search(r"\b(hi|hello|hey|greetings|good morning|good afternoon)\b", text):
            await turn_context.send_activity("Hi there! 👋 I'm your BFR training assistant. How can I support your muscle growth journey today?")
        # Farewells
        elif re.search(r"\b(bye|goodbye|see you|thanks|thank you)\b", text):
            await turn_context.send_activity("You're welcome! Keep up the great work and stay safe with your training. 💪")
        # What is BFR?
        elif re.search(r"\b(what is bfr|explain bfr|blood flow restriction|bfr training)\b", text):
            await turn_context.send_activity(
                "Blood Flow Restriction (BFR) training uses controlled pressure on limbs to reduce blood flow during exercise, "
                "which helps amplify muscle growth even with lighter weights."
            )
        # Safety and Precautions
        elif re.search(r"\b(safe|safety|precaution|risk|danger|harm|pain|numbness)\b", text):
            await turn_context.send_activity(
                "BFR is generally safe when done correctly. Always avoid pain or numbness, use proper cuff pressure, "
                "and consult a professional if unsure. Your safety comes first!"
            )
        # Duration & Frequency
        elif re.search(r"\b(how long|duration|frequency|how often|sets|reps|rest)\b", text):
            await turn_context.send_activity(
                "Typically, BFR sets last 15-30 seconds with rest intervals of 30-60 seconds. Many train 2-3 times a week "
                "to balance growth and recovery."
            )
        # Benefits
        elif re.search(r"\b(benefit|advantage|why use bfr|effects|results|muscle growth)\b", text):
            await turn_context.send_activity(
                "BFR helps build muscle and strength using lighter weights, reducing joint stress and injury risk."
            )
        # Troubleshooting
        elif re.search(r"\b(problem|issue|pain|discomfort|numbness|trouble|concern)\b", text):
            await turn_context.send_activity(
                "If you experience sharp pain or numbness, stop immediately and consult a healthcare professional. "
                "Proper cuff placement and pressure are key to avoiding issues."
            )
        # Motivation & Tips
        elif re.search(r"\b(motivation|encourage|tips|help|advice)\b", text):
            await turn_context.send_activity(
                "Stay consistent and listen to your body. Track your progress and ask me anytime for guidance or tips!"
            )
        # Small talk / fun
        elif re.search(r"\b(how are you|what's up|how's it going|your name)\b", text):
            await turn_context.send_activity(
                "I'm just a bot, but I'm here 24/7 to help you with BFR training! What would you like to know?"
            )
        # Fallback - ask to clarify
        else:
            await turn_context.send_activity(
                "Sorry, I didn't quite understand that. Could you please rephrase or ask me about BFR training, safety, benefits, or workout tips?"
            )