PyGame tutorial



##Drawing on the screen

To draw something on the screen we must first load image from file. Then blit it on display surface and at the end order PyGame to draw everything on the screen.

Blitting is a process of putting one image onto another e.g. we will put our hero on the screen every frame in a bit different positions to create illusion of motion.

display_surf.blit(image_to_paint, (0,0))

For loading images PyGame have pygame.image module. To load a particular image use:

image_surf = pygame.image.load("myimage.bmp").convert()

**If you wan't to make your games os independent use os.path.join("folder_where_your_data_are", "file_name_of_image") to create os specific path to file e.g uder linux it will be "folder_where_your_data_are/file_name_of_image"**

##Multiple images in one file

Imagine that in our game we have 100 types of ground is this mean that we have to create 100 files?
NO!! just put therm together and order PyGame to cut out only those you need at the moment.
use:

image_surf = pygame.image.load("one_big_file.bmp").convert()

and for drawing only  part of it:
display_surf.blit(image_surf, (0,0) , rect_containing_coordinates_to_draw)