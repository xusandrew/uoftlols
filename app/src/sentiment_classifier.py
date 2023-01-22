import cohere
import sys


def classify_sentiment(input):

    co = cohere.Client('RHzTSvRIyHr2OlXmm3k1jLZ1B6cgg2eFbaV3VO1O')
    inputMessage = []
    inputMessage.append(input)

    finetuned_response = co.classify(
        model="705d8a21-1edb-444b-92c5-76e61167ee00-ft",  # model id
        inputs=inputMessage
    )
    return finetuned_response.classifications[0].prediction


k = classify_sentiment(sys.argv[1])
print(k, end='')
sys.stdout.flush()
