create admin.py to register all models

To check the updating of database, reuse python manager.py shell

django database commands:
	Account.objects.all().delete()
	Account.objects.all()
	Account.objects.filter(username=1)


Jquery and js can be used together
JS: 
	<script>
		var b = 1
		function a(b){
			window.alert(b);
		}
	</script>

Care:

many files or functions have postfix 's'
like views, models......
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!


 DROP TABLE wei6_dghp.auth_group;                 
 DROP TABLE wei6_dghp.auth_group_permissions;     
 DROP TABLE wei6_dghp.auth_message;               
 DROP TABLE wei6_dghp.auth_permission;            
 DROP TABLE wei6_dghp.auth_user;                 
 DROP TABLE wei6_dghp.auth_user_groups;           
 DROP TABLE wei6_dghp.auth_user_user_permissions; 
 DROP TABLE wei6_dghp.django_admin_log;           
 DROP TABLE wei6_dghp.django_content_type;        
 DROP TABLE wei6_dghp.django_session;             
 DROP TABLE wei6_dghp.django_site;               
 DROP TABLE wei6_dghp.login_comment;              
 DROP TABLE wei6_dghp.login_post; 
 DROP TABLE wei6_dghp.media;   
                    
 DROP TABLE wei6_dghp.modelView_account;          
 DROP TABLE wei6_dghp.modelView_download; 
 DROP TABLE wei6_dghp.modelView_comment;      
 DROP TABLE wei6_dghp.modelView_media;
 DROP TABLE wei6_dghp.modelView_download;

-strict experimental !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
format transforming
	avconv -i small.ogv  -strict experimental -vcodec libx264  small.mp4
dimension transforming
	1) raw
	avconv -i H264_test1_Talkinghead_mp4_480x360.mp4  -strict experimental -vcodec libx264  -vf scale=320:200 H264.mp4
	2) by ratio
	width=560
	height=320
	avconv -i H264_test1_Talkinghead_mp4_480x360.mp4 -strict experimental -vcodec libx264  -vf "scale=iw*min($width/iw\,$height/ih):ih*min($width/iw\,$height/ih), pad=$width:$height:($width-iw*min($width/iw\,$height/ih))/2:($height-ih*min($width/iw\,$height/ih))/2" H264.mp4
extract all frames
	avconv -i H264.mp4 %05d.png
extract thumbnail
	avconv -i small.mp4 -f image2 -ss 1.342 -vframes 1 frame.png

inputFile = 'small.ogv'
outputFile = 'small.mp4'

command = ['avconv', '-i', inputFile,  '-strict', 'experimental', '-vcodec', 'libx264', outputFile]
subprocess.call(command)

import subprocess
width=560
height=320
command = ['avconv', '-i', 'H264_test1_Talkinghead_mp4_480x360.mp4', '-strict', 'experimental', '-vcodec', 'libx264',  '-vf', "scale=iw*min(560/iw\,320/ih):ih*min(560/iw\,320/ih), pad=560:320:(560-iw*min(560/iw\,320/ih))/2:(320-ih*min(560/iw\,320/ih))/2", 'H264.mp4']
subprocess.call(command)
