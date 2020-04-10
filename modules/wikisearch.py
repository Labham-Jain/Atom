# Wkipedia Search Code
import wikipedia
import wikipedia.exceptions


def wikipediaSummary(Topic, Sentences=2):
    """
        This Will Return Wikipedia's Result Requires A Topic
    """
    try:
        summary = wikipedia.summary(title=Topic, sentences=Sentences)
        return summary
    except:

        return ("Error Occurred...")
