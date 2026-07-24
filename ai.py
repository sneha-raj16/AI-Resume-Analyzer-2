import os
import json
from groq import Groq


client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)



def analyze_resume(resume_text, job_role):


    prompt = f"""

You are an expert AI Resume Analyzer.

Analyze the resume below for the role:

Target Role:
{job_role}


Resume:

{resume_text}


Return ONLY valid JSON.

Do not add markdown.
Do not add ```json.
Do not explain anything.


JSON format:

{{
"ats_score":85,

"summary":"short professional summary",

"skills":[
"skill1",
"skill2"
],

"improvements":[
"improvement1",
"improvement2"
],

"suggestions":[
"suggestion1",
"suggestion2"
],

"interview_questions":[
"question1",
"question2"
]

}}

"""


    response = client.chat.completions.create(

        model="llama-3.3-70b-versatile",

        messages=[
            {
                "role":"user",
                "content":prompt
            }
        ],

        temperature=0.2

    )



    result = response.choices[0].message.content



    try:

        data = json.loads(result)

        return data


    except Exception:


        # Remove markdown if AI adds it

        cleaned = result.replace(
            "```json",
            ""
        ).replace(
            "```",
            ""
        ).strip()



        try:

            return json.loads(cleaned)


        except:


            return {
                "ats_score":0,

                "summary":
                "AI could not analyze the resume.",

                "skills":[],

                "improvements":[],

                "suggestions":[],

                "interview_questions":[],

                "error":result
            }