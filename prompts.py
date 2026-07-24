
def resume_prompt(resume,job):


    prompt=f"""

You are an expert ATS resume analyzer.

Analyze this resume.

Resume:

{resume}


Job Description:

{job}


Return ONLY JSON:

{{
"resume_score":0,
"ats_score":0,

"skills":[],

"missing_skills":[],

"strengths":[],

"weakness":[],

"suggestions":[]
}}

"""

    return prompt
