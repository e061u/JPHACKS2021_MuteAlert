set MEETINGID=<meeting_id>
set PASSWORD=<hashing_pass>
start zoommtg:"//zoom.us/join?action=join&confno=%MEETINGID%&pwd=%PASSWORD%"
python <script-path>
timeout /t <wait-time>