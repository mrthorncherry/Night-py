mmal.MMAL_PARAM_IMAGEFX_COLOURPOINT = 0
clp = mmal.MMAL_PARAM_IMAGEFX_COLOURPOINT
camera.image_effect = clp
mp.u = 32768
mp.v = 65536

print(mp.u)

camera.outputs[0].commit()
count=0
lastbuttonstate=0;
presscount=1;
camera.outputs[0].framesize=(1080,720)

p = render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]
p.set = mmal.MMAL_DISPLAY_SET_FULLSCREEN | mmal.MMAL_DISPLAY_SET_DEST_RECT
p.fullscreen = False
while True:
        buttonstate=GPIO.input(3)
        input_state=GPIO.input(3)
        if buttonstate != lastbuttonstate:
                presscount=presscount+1
                if presscount%2==0:

                        camera.outputs[0].framerate=25
                        p.dest_rect = mmal.MMAL_RECT_T(0,35,400,480)
                        mp = camera.control.params[mmal.MMAL_PARAMETER_COLOUR_EFFECT]


                        render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p


                        p.dest_rect = mmal.MMAL_RECT_T(400,35,400,480)
                        render_r.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p
                        splitter.connect(camera.outputs[0])
                        render_l.connect(splitter.outputs[0])
                        render_r.connect(splitter.outputs[1])
while True:
        buttonstate=GPIO.input(3)
        input_state=GPIO.input(3)
        if buttonstate != lastbuttonstate:
                presscount=presscount+1
                if presscount%2==0:

                        camera.outputs[0].framerate=25
                        p.dest_rect = mmal.MMAL_RECT_T(0,35,400,480)
                        mp = camera.control.params[mmal.MMAL_PARAMETER_COLOUR_EFFECT]


                        render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p


                        p.dest_rect = mmal.MMAL_RECT_T(400,35,400,480)
                        render_r.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p
                        splitter.connect(camera.outputs[0])
                        render_l.connect(splitter.outputs[0])
                        render_r.connect(splitter.outputs[1])
                else:
while True:
        buttonstate=GPIO.input(3)
        input_state=GPIO.input(3)
        if buttonstate != lastbuttonstate:
                presscount=presscount+1
                if presscount%2==0:

                        camera.outputs[0].framerate=25
                        p.dest_rect = mmal.MMAL_RECT_T(0,35,400,480)
                        mp = camera.control.params[mmal.MMAL_PARAMETER_COLOUR_EFFECT]


                        render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p


                        p.dest_rect = mmal.MMAL_RECT_T(400,35,400,480)
                        render_r.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p
                        splitter.connect(camera.outputs[0])
                        render_l.connect(splitter.outputs[0])
                        render_r.connect(splitter.outputs[1])
                else:
                        camera.outputs[0].framerate=70
                        p.dest_rect = mmal.MMAL_RECT_T(0,35,400,480)
                        render_l.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p
                        p.dest_rect = mmal.MMAL_RECT_T(400,35,400,480)
                        render_r.inputs[0].params[mmal.MMAL_PARAMETER_DISPLAYREGION]=p
                        splitter.connect(camera.outputs[0])
                        render_l.connect(splitter.outputs[0])
                        render_r.connect(splitter.outputs[1])

        lastbuttonstate=buttonstate
pause()



