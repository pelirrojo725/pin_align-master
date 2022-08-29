########################## Base Parameters ##########################

DEFAULT_PIXELS_PER_MM = 40
PIN_X1_OFFSET = 20

X_POS = True
Y_POS = True
Z_POS = False

X_CENTER = 300
Y_CENTER = 548

########################## pin,body,base ##########################
# slice(offset, offset)
# offset = Y + height
DEFAULT_ROI_Y1 = 418
DEFAULT_ROI_Y2 = 678

DEFAULT_HEIGHT = 260

# Pin tip
# offset = X + width
PIN_TIP_X1 = 200
PIN_TIP_X2 = 398

PIN_TIP = slice(PIN_TIP_X1, PIN_TIP_X2)

# Pin body
PIN_BODY_X1 = 398
PIN_BODY_X2 = 596

PIN_BODY = slice(PIN_BODY_X1, PIN_BODY_X2)

# Pin base
PIN_BASE_X1 = 596
PIN_BASE_X2 = 796

PIN_BASE = slice(PIN_BASE_X1, PIN_BASE_X2)

########################## Tilt check  parameters ##########################
# Setting the width = -10 the width of the image
TILT_CHECK_X1 = 746
TILT_CHECK_X2 = 796

TILT_CHECK_ROI_WIDTH = slice(TILT_CHECK_X1, TILT_CHECK_X2)

# Top crop
TILT_CHECK_TOP_Y1 = 433
TILT_CHECK_TOP_Y2 = 498

TILT_CHECK_TOP = slice(TILT_CHECK_TOP_Y1, TILT_CHECK_TOP_Y2)

# Bottom crop
TILT_CHECK_BOTTOM_Y1 = 598
TILT_CHECK_BOTTOM_Y2 = 663

TILT_CHECK_BOTTOM = slice(TILT_CHECK_BOTTOM_Y1, TILT_CHECK_BOTTOM_Y2)

########################## Pin check parameters ##########################

# Top crop
PIN_CHECK_TOP_Y1 = 418
PIN_CHECK_TOP_Y2 = 498

PIN_CHECK_TOP = slice(PIN_CHECK_TOP_Y1, PIN_CHECK_TOP_Y2)

# Bottom crop
PIN_CHECK_BOTTOM_Y1 = 598
PIN_CHECK_BOTTOM_Y2 = 678

PIN_CHECK_BOTTOM = slice(PIN_CHECK_BOTTOM_Y1, PIN_CHECK_BOTTOM_Y2)

DEFAULT_WIDTH = 596

########################## X,Y,Z check parameters ##########################
MIN_X = -2
MAX_X = 2

MIN_Y = -2
MAX_Y = 2

MIN_Z = -2
MAX_Z = 2

########################## Small & Big Box parameters ##########################
BOX_X_IN = 300
BOX_Y_IN = 548

SMALL_BOX_X1 = BOX_X_IN + (MIN_Z * DEFAULT_PIXELS_PER_MM)
SMALL_BOX_X2 = BOX_X_IN + (MAX_Z * DEFAULT_PIXELS_PER_MM)

SMALL_BOX_WIDTH = slice(SMALL_BOX_X1, SMALL_BOX_X2)

SMALL_BOX_Y1 = BOX_Y_IN + (MIN_Y * DEFAULT_PIXELS_PER_MM)
SMALL_BOX_Y2 = BOX_Y_IN + (MAX_Y * DEFAULT_PIXELS_PER_MM)

SMALL_BOX_HEIGHT = slice(SMALL_BOX_Y1, SMALL_BOX_Y2)

BIG_BOX_X1 = 200
BIG_BOX_X2 = 796

BIG_BOX_WIDTH = slice(BIG_BOX_X1, BIG_BOX_X2)

BIG_BOX_Y1 = 418
BIG_BOX_Y2 = 678

BIG_BOX_HEIGHT = slice(BIG_BOX_Y1, BIG_BOX_Y2)
#################################################### EOF ####################################################
