#/bin/bash

###########################################################

DEFAULT_PIXELS_PER_MM="40"
PIN_X1_OFFSET=$((20))

export X_POS=1
export Y_POS=1
export Z_POS


X_CENTER=$((300))

Y_CENTER=$((548))
DEFAULT_HEIGHT=$((260))
DEFAULT_WIDTH=$((596))
#########################################################

BIG_BOX_X1=$((202))
BIG_BOX_X2=$((798))

BIG_BOX_Y1=$((423))
BIG_BOX_Y2=$((673))

PIN_ALIGN_ROI_WIDTH=$(((${BIG_BOX_X2}-${BIG_BOX_X1}) / 3))
PIN_ALIGN_ROI_HEIGHT=$((${BIG_BOX_Y2}-${BIG_BOX_Y1}))

########################## pin,body,base ##########################

DEFAULT_ROI_Y1=$((423))

PIN_TIP_X1=$((202))

PIN_TIP="${PIN_ALIGN_ROI_WIDTH}x${PIN_ALIGN_ROI_HEIGHT}+${PIN_TIP_X1}+${DEFAULT_ROI_Y1}"

PIN_BODY_X1=$((400))

PIN_BODY="${PIN_ALIGN_ROI_WIDTH}x${PIN_ALIGN_ROI_HEIGHT}+${PIN_BODY_X1}+${DEFAULT_ROI_Y1}"

PIN_BASE_X1=$((598))

PIN_BASE="${PIN_ALIGN_ROI_WIDTH}x${PIN_ALIGN_ROI_HEIGHT}+${PIN_BASE_X1}+${DEFAULT_ROI_Y1}"

########################## Tilt check  parameters ##########################

TILT_CHECK_X1=$((748))
TILT_CHECK_X2=$((798))

TILT_CHECK_ROI_WIDTH=$((${TILT_CHECK_X2}-${TILT_CHECK_X1}))

# Tilt check top
TILT_CHECK_TOP_Y1=$((438))
TILT_CHECK_TOP_Y2=$((498))

TILT_CHECK_TOP_HEIGHT=$((${TILT_CHECK_TOP_Y2}-${TILT_CHECK_TOP_Y1}))
#TILT_CHECK_TOP_HEIGHT=((1))

TILT_CHECK_TOP="${TILT_CHECK_ROI_WIDTH}x${TILT_CHECK_TOP_HEIGHT}+$((${TILT_CHECK_X1} - ${PIN_BASE_X1}))+$((${TILT_CHECK_TOP_Y1} - ${DEFAULT_ROI_Y1}))"

# Tilt check bottom
TILT_CHECK_BOTTOM_Y1=$((598))
TILT_CHECK_BOTTOM_Y2=$((658))

TILT_CHECK_BOTTOM_HEIGHT=$((${TILT_CHECK_BOTTOM_Y2}-${TILT_CHECK_BOTTOM_Y1}))
#TILT_CHECK_BOTTOM_HEIGHT=((1))

TILT_CHECK_BOTTOM="${TILT_CHECK_ROI_WIDTH}x${TILT_CHECK_TOP_HEIGHT}+$((${TILT_CHECK_X1} - ${PIN_BASE_X1}))+$((${TILT_CHECK_BOTTOM_Y1} - ${DEFAULT_ROI_Y1}))"

########################## Pin check parameters ##########################

PIN_CHECK_ROI_WIDTH=${PIN_ALIGN_ROI_WIDTH}

PIN_CHECK_X1=${PIN_BODY_X1}

PIN_CHECK_TOP_Y1=$((423))
PIN_CHECK_TOP_Y2=$((498))

#PIN_CHECK_TOP_HEIGHT=$((${PIN_CHECK_TOP_Y2}-${PIN_CHECK_TOP_Y1}))
PIN_CHECK_TOP_HEIGHT=$((1))

PIN_CHECK_TOP="${PIN_CHECK_ROI_WIDTH}x${PIN_CHECK_TOP_HEIGHT}+0+0"

PIN_CHECK_BOTTOM_Y1=$((598))
PIN_CHECK_BOTTOM_Y2=$((673))

#PIN_CHECK_BOTTOM_HEIGHT=$((${PIN_CHECK_BOTTOM_Y2}-${PIN_CHECK_BOTTOM_Y1}))
PIN_CHECK_BOTTOM_HEIGHT=$((1))

PIN_CHECK_BOTTOM="${PIN_CHECK_ROI_WIDTH}x${PIN_CHECK_TOP_HEIGHT}+0+$((${PIN_CHECK_BOTTOM_Y1}-${PIN_CHECK_TOP_Y1}))"

########################## X,Y,Z check parameters ##########################
MIN_X=$((-2))
MAX_X=$((2))

MIN_Y=$((-2))
MAX_Y=$((2))

MIN_Z=$((-2))
MAX_Z=$((2))

##############################################################
#  *** UNCOMMENT THE FOLLOWING LINE TO ENABLE DEBUG MODE ***
# export PIN_ALIGN_DEBUG="yes"
# ##############################################################

if [ "xx${PIN_ALIGN_PIXELS_PER_MM}" == "xx" ]; then
    PIN_ALIGN_PIXELS_PER_MM=${DEFAULT_PIXELS_PER_MM}
fi
echo "PIN_ALIGN_PIXELS_PER_MM = ${PIN_ALIGN_PIXELS_PER_MM}"
#################################################### EOF ####################################################
