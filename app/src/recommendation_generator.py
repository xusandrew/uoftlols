import cohere
import angerStaticData
import sadnessStaticData
import sys


def recommendationGenerator(sentiment, incoming_text):

    co = cohere.Client('RHzTSvRIyHr2OlXmm3k1jLZ1B6cgg2eFbaV3VO1O')
    promptGiven = None
    if (sentiment == "anger"):
        angerStaticData.prompt += incoming_text+"\nreply: "
        promptGiven = angerStaticData.prompt
    elif (sentiment == "sadness"):
        sadnessStaticData.prompt += incoming_text+"\nreply: "
        promptGiven = sadnessStaticData.prompt

    response = co.generate(
        model='xlarge',
        prompt=promptGiven,
        max_tokens=20,
        temperature=0.6,
        stop_sequences=["--"])

    reply = response.generations[0].text
    return reply[0:len(reply)-2]


k = recommendationGenerator(sys.argv[1], sys.argv[2])
print(k, end='')
sys.stdout.flush()
