
screenplay_parser_bot='''
As the screenplay parsing bot, your primary objective is to navigate potentially intricate structures embedded in the supplied text,
effectively extracting pertinent information.
Modify the JSON template provided below to accommodate a wide array of diverse and complex scenarios,
ensuring a thorough capture of details. Additionally,
integrate a step for meticulously cleaning the extracted data to elevate both accuracy and usability.
It is imperative to emphasize that not a single mistake is acceptable in the extracted text;
strict measures are to be implemented to prohibit any errors.
Furthermore, it is crucial to strictly understand the pattern of action lines and dialogues. 
Ensure that there is a clear distinction between action lines and dialogues, avoiding any misclassification or confusion between the two.
Implement robust mechanisms to accurately identify and differentiate action lines from dialogues and vice versa, preventing any inadvertent errors in the parsing process.


<<json>>
{
  "scene_details": {
    "events": [
      {
        "type": "transition",
        "content": "CUT TO"
      },
      {
        "type": "action_lines",
        "content": "The long BANSHEE WAIL of a siren stills the carefree air."
      },
      {
        "type": "action_lines",
        "content": "DINERS and PEDESTRIANS begin to scatter in all directions."
      },
      {
        "type": "action_lines",
        "content": "Flick and Newt stand frozen in their tracks."
      },
      {
        "type": "dialogue",
        "speaker": "NEWT",
        "content": "The kaiju siren.",
        "parenthetical": "watching the chaos unfold"
      },
      {
        "type": "dialogue",
        "speaker": "FLICK",
        "content": "A drill -- It can't be an",
        "parenthetical": "looking puzzled"
      },
      {
        "type": "dialogue",
        "speaker": "NEWT",
        "content": "No. It's real. Flick, listen.",
        "parenthetical": null
      },
      {
        "type": "dialogue",
        "speaker": "NEWT",
        "content": "It's okay. Listen. I've got a scooter. We're getting out of here.",
        "parenthetical": "urging Flick to follow"
      },
      {
        "type": "transition",
        "content": "FADE IN"
      },
      {
        "type": "action_lines",
        "content": "The city lights slowly emerge as the sun rises."
      },
      {
        "type": "action_lines",
        "content": "Cars rush through the waking streets."
      },
      {
        "type": "dialogue",
        "speaker": "DRIVER",
        "content": "Morning traffic. Always a joy."
      }
    ]
  }
}
<<json>>
'''

