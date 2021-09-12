import qrcode
img = qrcode.make('''Dhananjay Porwal
65A Sudama Nagar, Indore
Madhya Pradesh, India
PIN CODE: 452007
Mob: +918962390430
Email: dporwal214@gmail.com

========================================================================

SUMMARY

Third Year Computer Science Engineering Student. Expertise in Linux, python and cloud (GCP). Looking for opportunities related to ML/Cloud.Excelled in DSA. "I found technology to explore myself". 

========================================================================

EDUCATION

B.Tech in CSE | Medicaps University 			| 2019-23

10th to 12th  | Shri R.K. Daga Maheshwari Academy	| 2016-2018

========================================================================

TECHNICAL SKILLS

Python | Linux | Google Cloud | SQL | Video Editing | C/C++ | Java | Android Development | ML | Git | Web Development | MS-Office

========================================================================

HOBBIES

Reading | Traveling | Writing | Sketching

========================================================================

ACHIEVEMENTS

Global Rank 38 - CodeChef July Long Challenge 2021 Div 3''')

img.save("/QrResume.png")
