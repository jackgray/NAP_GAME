NARC Lab's Automated Pipeline for Gaze Analysis and Mapping of EyeLink data


Planning steps:
Goal: generate image of gaze heatmap overlaid on input image. A gaze heatmap is a map of gaze direction represented as colored coordinate points for each milisecond of a given trial. 

To do this, a few things must be determined:

The "edf time" or "tracker time" for the start of the trial (tt_1)
tt_2 aka the edf time that the trial ends

Whether or not a movie trial may have more than one shot or scene of interest. 

How to add the image screen fill function added in the proper timepoints (tt) i.e. MSG ${tracker_time} !V IMGLOAD FILL ref_img.jpg

Array of order of images the subject viewed (is it static or dynamic?)


REFERENCE  NOTES
-----------------

7.3.3 Image Commands
The viewer supports a set of commands that display a default image on the overlay mode
of the trial viewer screen. All image commands use the IMGLOAD token, followed by a
sub command.
7.3.3.1 Image Loading – Fill Full Screen
Identifier: FILL
Description:
EyeLink Data Viewer ©2002-2007 SR Research Ltd. 87
This message specifies the image to be used as the background for the spatial overlay
view of a trial within the viewer. The image is sized to fit the dimensions specified in the
DISPLAY_COORDS command message. The image should be represented as a relative
path. The viewer will look for the image in the following order:
1) In the default image directory specified in the general preference settings.
2) In the directory the EyeLink data file is loaded from.
3) In the directory the viewer application is running from.
Format:
!V IMGLOAD FILL <relative_image_path>
Example:
MSG 3388468 !V IMGLOAD FILL Sac_blur.jpg