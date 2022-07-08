REF_IMG=$1
CONTEXT=$2
FRAMERATE=29.97 # Assume NTSC standard framerate
SR=1000  # Hz

frame_no=$(ffmpeg \
-i ${CONTEXT} \
-loop 1 \
-i ${REF_IMG} \
-an \
-filter_complex "blend=difference:shortest=1,blackframe=99:32" \
-f null \
- \
| cut -d 'frame:' -f 1 | cut -d ' ' -f 1)


tt_s=${frame_no}/${FRAMERATE} # in seconds
tt_ms=${tt_s}/1000
ms_resolution=1000/${SR}
 .
