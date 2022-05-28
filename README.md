# Django_Kidefty
This is the project on Face Recognition for Microsoft Engage

Go to Django_Kidefty/Django/Project and run the server using :
python manage.py runserver

The home page of Kidefty will get render.

Find about kidefty by going on About Us on navbar.

Register on the Kidefty Service by clicking on "Register Now" button on home page.

You can get the list of registered guardians and child by clicking on "Registered Guardians" on home page.

Web Camera button:
Click on "web camera" button on home page to start the face recognition system.
The Web Cam will get started,
show the images of registered guardian,
you can find the registered guardian images inside the folder "Test Images to show for recognition"
Open those images in your phone and bring the image near the webcam of your laptop.
If the person's face is already registered, they will be recognised and their name along with the child's name whom they came to pick will get stored.

click q to stop the web cam.

To get today's record of children who are safely picked by their guardian click on "Today's Record".

To get the contact detail of children for whom no registered guardian came to receive them click on "Send not receive message to" button on home page.
Those contact details can be used to inform the parent's of the these children that no one came to receive them, they can pick them from the fully guarded playhouse under the serive Kidefty.

To provide feedback click on "Feedback" button on home page.

To view the data of new registered guardians and feedback by going in admin portal of kidefty.
Username: admin
Password: admin

NOTE: In case the webcam is not detected try changing the parameter of cv2.vediocapture() function in the "output" function inside Django_Kidefty/Django/project/home/views.py from 0 to 1 or 2.
