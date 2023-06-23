Causal-Study-of-the-Effects-of-Personal-Relative-Income-Information-v0

Test version of the online survey

The oTree codes are built on oTree 3.0.9 and can be compiled with oTree<5. See requirements.txt for other environment requirements of the codes.

The reason why we did not develop the online survey with oTree5 (oTree light) is because we need multilinguistic pages (Finnish and Swedish), and oTree5 does not support Django translation package.

The codes are developed in English (Python scripts and HTML).

# How to set up and try the survey?
Step 1: Download the zip file and extract it and open the project (extracted folder) in an integrated development environment, i.e., PyCharm. 
	You may also try it on a server if the server has set up oTree in the back end.
Step 2: Open the link (local server if you try on local computer or server URL if you host it on a server).
Step 3: Set up the rooms. 
	The name “stat2” is for incentivized survey (our main sample) and “stat3” is for non-incentivized survey.
Step 4: Click the room link and start the survey as a participant. 
	At the beginning, you need to input a username and password (which the participants did for security and privacy concerns). 
	Each username (participant) in the codes has simulated unreal personal information (i.e., income ranks, education, occupation, etc.). 
	This is to preserve the private information of the participants in our study. 
	
	Below you may find the usernames and their corresponding passwords, treatments, and whether they are usernames for the incentivized version or not. 
	Note that the incentivized (non-incentivized) username and password should be used in the link for room “stat2” (“stat3”).

	username,password,treatment,incentive
	1111,aaa,Occupation,0
	1112,jjj,National,0
	1113,kkk,Education,0
	1114,lll,Education,1
	1115,mmm,Age,0
	1116,nnn,Control,0
	2222,bbb,Occupation,1
	3333,ccc,Age,1
	4444,ddd,Choice,0
	5555,eee,Choice,1
	6666,fff,Municipality,0
	7777,ggg,Municipality,1
	8888,hhh,Control,1
	9999,iii,National,1
