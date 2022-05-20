########################## Base Parameters ##########################

DEFAULT_PIXELS_PER_MM = 20
PIN_X1_OFFSET = 15

X_POS = True
Y_POS = True
Z_POS = False

X_CENTER = 471
Y_CENTER = 433

########################## pin,body,base ##########################
# slice(offset, offset)
# offset = Y + height
DEFAULT_ROI_Y1 = 308
DEFAULT_ROI_Y2 = 558

DEFAULT_HEIGHT = 250

# Pin tip
# offset = X + width
PIN_TIP_X1 = 416
PIN_TIP_X2 = 555

PIN_TIP = slice(PIN_TIP_X1, PIN_TIP_X2)

# Pin body
PIN_BODY_X1 = 555
PIN_BODY_X2 = 694

PIN_BODY = slice(PIN_BODY_X1, PIN_BODY_X2)

# Pin base
PIN_BASE_X1 = 694
PIN_BASE_X2 = 835

PIN_BASE = slice(PIN_BASE_X1, PIN_BASE_X2)

########################## Tilt check  parameters ##########################
# Setting the width = -10 the width of the image
TILT_CHECK_X1 = 785
TILT_CHECK_X2 = 835

TILT_CHECK_ROI_WIDTH = slice(TILT_CHECK_X1, TILT_CHECK_X2)

# Top crop
TILT_CHECK_TOP_Y1 = 323
TILT_CHECK_TOP_Y2 = 383

TILT_CHECK_TOP = slice(TILT_CHECK_TOP_Y1, TILT_CHECK_TOP_Y2)

# Bottom crop
TILT_CHECK_BOTTOM_Y1 = 483
TILT_CHECK_BOTTOM_Y2 = 543

TILT_CHECK_BOTTOM = slice(TILT_CHECK_BOTTOM_Y1, TILT_CHECK_BOTTOM_Y2)

########################## Pin check parameters ##########################

# Top crop
PIN_CHECK_TOP_Y1 = 308
PIN_CHECK_TOP_Y2 = 383

PIN_CHECK_TOP = slice(PIN_CHECK_TOP_Y1, PIN_CHECK_TOP_Y2)

# Bottom crop
PIN_CHECK_BOTTOM_Y1 = 483
PIN_CHECK_BOTTOM_Y2 = 558

PIN_CHECK_BOTTOM = slice(PIN_CHECK_BOTTOM_Y1, PIN_CHECK_BOTTOM_Y2)

DEFAULT_WIDTH = 419

########################## X,Y,Z check parameters ##########################
MIN_X = -2
MAX_X = 2

MIN_Y = -2
MAX_Y = 2

MIN_Z = -2
MAX_Z = 2

########################## Small & Big Box parameters ##########################
BOX_X_IN = 471
BOX_Y_IN = 433

SMALL_BOX_X1 = BOX_X_IN + (MIN_Z * DEFAULT_PIXELS_PER_MM)
SMALL_BOX_X2 = BOX_X_IN + (MAX_Z * DEFAULT_PIXELS_PER_MM)

SMALL_BOX_WIDTH = slice(SMALL_BOX_X1, SMALL_BOX_X2)

SMALL_BOX_Y1 = BOX_Y_IN + (MIN_Y * DEFAULT_PIXELS_PER_MM)
SMALL_BOX_Y2 = BOX_Y_IN + (MAX_Y * DEFAULT_PIXELS_PER_MM)

SMALL_BOX_HEIGHT = slice(SMALL_BOX_Y1, SMALL_BOX_Y2)

BIG_BOX_X1 = 416
BIG_BOX_X2 = 835

BIG_BOX_WIDTH = slice(BIG_BOX_X1, BIG_BOX_X2)

BIG_BOX_Y1 = 308
BIG_BOX_Y2 = 558

BIG_BOX_HEIGHT = slice(BIG_BOX_Y1, BIG_BOX_Y2)
#################################################### EOF ####################################################
