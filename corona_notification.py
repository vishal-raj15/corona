# from gi.repository import Notify

# # One time initialization of libnotify
# Notify.init("My Program Name")

# # Create the notification object
# summary = "Wake up!"
# body = "Meeting at 3PM!"
# notification = Notify.Notification.new(
#     summary,
#     body, # Optional
# )

# # Actually show on screen
# notification.show()







# from gi.repository import Notify
# Notify.init("My Program Name")

# # Create the notification object and show once
# notification = Notify.Notification.new("Hi")
# notification.show()

# # Let's throw in a sleep before we show again
# import time
# time.sleep(5)

# # Change application name
# notification.set_app_name("New App Name")

# # Change summary and body
# notification.update("Ding!", "Cupcakes are done.")

# # Show again
# notification.show()




from gi.repository import Notify, GdkPixbuf

Notify.init("Test App")
notification = Notify.Notification.new("Alert!")

# Use GdkPixbuf to create the proper image type
image = GdkPixbuf.Pixbuf.new_from_file("/home/vishal/Downloads/344856.jpg")

# Use the GdkPixbuf image
notification.set_icon_from_pixbuf(image)
notification.set_image_from_pixbuf(image)

notification.show()




# This one is required, but should already be installed
#sudo apt-get install python-gobject

# Installing this will install the
# notify-send program. Check that out
# for sending notifications in the shell
#sudo apt-get install libnotify-bin

# The development headers if you
# want to do any development in C/C++
#sudo apt-get install libnotify-dev