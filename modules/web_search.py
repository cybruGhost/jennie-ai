import wikipedia
import spacy

# Load SpaCy English model
nlp = spacy.load("en_core_web_sm")

def search(query):
    try:
        # Set the language to English (you can change this as needed)
        wikipedia.set_lang("en")
        
        # Process the query using SpaCy
        doc = nlp(query)
        
        # Check if the query is a question
        if doc[0].pos_ == "AUX":
            # Get the root verb (main action) of the question
            verb = None
            for token in doc:
                if token.dep_ == "ROOT":
                    verb = token.text
                    break
            
            # Search based on the verb (action) in the question
            if verb:
                # You can add more specific search criteria based on the verb/action
                if verb.lower() == "who":
                    # Search for people-related queries
                    summary = wikipedia.summary(query, sentences=2)
                elif verb.lower() == "what":
                    # Search for general queries
                    summary = wikipedia.summary(query, sentences=2)
                else:
                    # Default search if the action is not recognized
                    summary = wikipedia.summary(query, sentences=2)
            else:
                # Default search if no action is identified in the question
                summary = wikipedia.summary(query, sentences=2)
        else:
            # Non-question query, perform a regular search
            summary = wikipedia.summary(query, sentences=2)
        
        return summary
    except wikipedia.exceptions.DisambiguationError as e:
        # Handle disambiguation pages by suggesting some options
        options = e.options[:3]  # Limit to first 3 options for brevity
        return f"Your query may refer to multiple topics. Please be more specific. Some options include: {', '.join(options)}"
    except wikipedia.exceptions.PageError:
        # Handle page not found
        return "No detailed information found."
    except Exception as e:
        # General error handling (e.g., network issues)
        return "Failed to retrieve information due to an error."
