from utils.preprocess import preprocess_text
from utils.skills import compare_skills

resume_text = """
Raj Gajbhiye +91-9082337572
Roll No.: 240101073 r.gajbhiye@iitg.ac.in
B.Tech. in Computer Science and Engineering rgajbhiyee@gmail.com
Indian Institute Of Technology, Guwahati github.com/noobcoder7810
linkedin.com/in/Raj-GajbhiyeRaj Gajbhiye +91-9082337572
Roll No.: 240101073 r.gajbhiye@iitg.ac.in
B.Tech. in Computer Science and Engineering rgajbhiyee@gmail.com
Indian Institute Of Technology, Guwahati github.com/noobcoder7810
linkedin.com/in/Raj-Gajbhiye
Education
Degree/Certificate Institute/Board CGPA/Percentage Year
B.Tech. Major Indian Institute of Technology, Guwahati 7.85 (Current) 2025-Present
Senior Secondary CBSE Board 91.6% 2024
Secondary CBSE Board 95.2% 2022
Experience
• Brain Reasearch Consultant June 2025 - Present
World Quant LLC Remote
– Developed quantitative trading strategies (alphas) using statistical modelling on 10+ years of US equity data.
– Performed backtesting to compute Sharpe ratio, turnover, return, and stability metrics.
– Generated 14 uncorrelated alphas (pairwise correlation < 0.7), demonstrating robustness and diversity.
Projects
• Wealth Maze — Personal Finance Optimization Project June 2025
FEC Recruitment Project
– Created tailored financial plans using budgeting, asset allocation, and risk profiles.
– Designed investment strategies with SIP projections and goal-based planning.
– Delivered a structured presentation explaining persona choices and optimization insights.
• Weather Website June 2025
SWC Hackstack Github
– Built a responsive web app that fetches real-time weather data using a public API.
– Implemented city-based search and dynamic display of temperature, humidity, and conditions.
– Developed with HTML, CSS, JavaScript and integrated with OpenWeatherMap API.
• EventPal – Full-Stack Event Discovery & Management Web App June 2025
SWC Hackstack Github
– Built a responsive React web application for discovering, creating, and managing events.
– Implemented features like event listing, filtering, bookmarking, and calendar view.
– Added form validation, routing, and persistent storage for smooth user experience.
Technical Skills
• Programming: C, C++, Python*
• Web Technology: HTML, CSS, Javascript, ReactJS
• Data Analysis: Matplotlib, Numpy, Pandas * Elementary proficiency
Key courses taken
• Mathematics: Probability & Random Processes, Discrete Mathematics, Linear Algebra & Number Theory
• Computer Science: Data structures and Algorithms, System Software (Lab), Digital Design
Achievements
• Codeforces, Maximum rating: 1083 | Solved 150+ problems | 25+ contests | Handle: raj__7810
• Codechef, Maximum rating: 1306 | Solved 40+ problems | Handle: raj_7810
• Associate at Finance & Economics Club IITG (Quant),
Extra-Curricular Activities
• Manthan (Inter Hostel Cultural Competetion), Participated and secured rank 1 in Sketch video Mar 2025
• Manthan (Inter Hostel Cultural Competetion), Participated in Mime Mar 2025
"""

jd_text = """
Looking for a software engineering intern with Python,
data structures, algorithms, SQL, and Linux experience.
"""

resume_clean = preprocess_text(resume_text)
jd_clean = preprocess_text(jd_text)

matched, missing = compare_skills(resume_clean, jd_clean)

print("Matched Skills:", matched)
print("Missing Skills:", missing)
