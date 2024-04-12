dependencies
ffmpeg

# output may loook like this  on x86 systems
--enable-sdl2 --enable-libaribb24 --enable-libaribcaption --enable-libdav1d --enable-libdavs2 --enable-libuavs3d --enable-libxevd --enable-libzvbi --enable-librav1e --enable-libsvtav1 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxeve --enable-libxvid --enable-libaom --enable-libjxl --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-frei0r --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-liblensfun --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-libshaderc --enable-vulkan --enable-libplacebo --enable-opencl --enable-libcdio --enable-libgme --enable-libmodplug --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libshine --enable-libtheora --enable-libtwolame --enable-libvo-amrwbenc --enable-libcodec2 --enable-libilbc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-ladspa --enable-libbs2b --enable-libflite --enable-libmysofa --enable-librubberband --enable-libsoxr --enable-chromaprint
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001cc90627480] st: 1 edit list: 1 Missing key frame while searching for timestamp: 0
[mov,mp4,m4a,3gp,3g2,mj2 @ 000001cc90627480] st: 1 edit list 1 Cannot find an index entry before timestamp: 0.
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'input_video.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    creation_time   : 2019-05-04T22:50:40.000000Z
  Duration: 00:03:59.70, start: 0.000000, bitrate: 4315 kb/s
  Stream #0:0[0x1](und): Video: h264 (High) (avc1 / 0x31637661), yuv420p(tv, bt709, progressive), 1920x1080 [SAR 1:1 DAR 16:9], 4184 kb/s, 25 fps, 25 tbr, 12800 tbn (default)
      Metadata:
        creation_time   : 2019-05-04T22:50:40.000000Z
        handler_name    : ISO Media file produced by Google Inc. Created on: 05/04/2019.
        vendor_id       : [0][0][0][0]
  Stream #0:1[0x2](eng): Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 127 kb/s (default)
      Metadata:
        creation_time   : 2019-05-04T22:44:16.000000Z
        handler_name    : ISO Media file produced by Google Inc. Created on: 05/04/2019.
        vendor_id       : [0][0][0][0]
Stream mapping:
  Stream #0:1 -> #0:0 (aac (native) -> aac (native))
Press [q] to stop, [?] for help
Output #0, adts, to 'audio_input_video.mp4.aac':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2avc1mp41
    encoder         : Lavf61.1.100
  Stream #0:0(eng): Audio: aac (LC), 44100 Hz, stereo, fltp, 128 kb/s (default)
      Metadata:
        creation_time   : 2019-05-04T22:44:16.000000Z
        handler_name    : ISO Media file produced by Google Inc. Created on: 05/04/2019.
        vendor_id       : [0][0][0][0]
        encoder         : Lavc61.3.100 aac
[out#0/adts @ 000001cc9064a480] video:0KiB audio:4108KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 1.718076%
size=    4178KiB time=00:03:59.69 bitrate= 142.8kbits/s speed=52.3x
[aac @ 000001cc90c6a880] Qavg: 120.000
ffmpeg version 7.0-full_build-www.gyan.dev Copyright (c) 2000-2024 the FFmpeg developers
  built with gcc 13.2.0 (Rev5, Built by MSYS2 project)
  configuration: --enable-gpl --enable-version3 --enable-static --disable-w32threads --disable-autodetect --enable-fontconfig --enable-iconv --enable-gnutls --enable-libxml2 --enable-gmp --enable-bzlib --enable-lzma --enable-libsnappy --enable-zlib --enable-librist --enable-libsrt --enable-libssh --enable-libzmq --enable-avisynth --enable-libbluray --enable-libcaca --enable-sdl2 --enable-libaribb24 --enable-libaribcaption --enable-libdav1d --enable-libdavs2 --enable-libuavs3d --enable-libxevd --enable-libzvbi --enable-librav1e --enable-libsvtav1 --enable-libwebp --enable-libx264 --enable-libx265 --enable-libxavs2 --enable-libxeve --enable-libxvid --enable-libaom --enable-libjxl --enable-libopenjpeg --enable-libvpx --enable-mediafoundation --enable-libass --enable-frei0r --enable-libfreetype --enable-libfribidi --enable-libharfbuzz --enable-liblensfun --enable-libvidstab --enable-libvmaf --enable-libzimg --enable-amf --enable-cuda-llvm --enable-cuvid --enable-dxva2 --enable-d3d11va --enable-d3d12va --enable-ffnvcodec --enable-libvpl --enable-nvdec --enable-nvenc --enable-vaapi --enable-libshaderc --enable-vulkan --enable-libplacebo --enable-opencl --enable-libcdio --enable-libgme --enable-libmodplug --enable-libopenmpt --enable-libopencore-amrwb --enable-libmp3lame --enable-libshine --enable-libtheora --enable-libtwolame --enable-libvo-amrwbenc --enable-libcodec2 --enable-libilbc --enable-libgsm --enable-libopencore-amrnb --enable-libopus --enable-libspeex --enable-libvorbis --enable-ladspa --enable-libbs2b --enable-libflite --enable-libmysofa --enable-librubberband --enable-libsoxr --enable-chromaprint
  libavutil      59.  8.100 / 59.  8.100
  libavcodec     61.  3.100 / 61.  3.100
  libavformat    61.  1.100 / 61.  1.100
  libavdevice    61.  1.100 / 61.  1.100
  libavfilter    10.  1.100 / 10.  1.100
  libswscale      8.  1.100 /  8.  1.100
  libswresample   5.  1.100 /  5.  1.100
  libpostproc    58.  1.100 / 58.  1.100
Input #0, mov,mp4,m4a,3gp,3g2,mj2, from 'resized_input_video.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2mp41
    encoder         : Lavf58.76.100
  Duration: 00:03:59.64, start: 0.000000, bitrate: 16127 kb/s
  Stream #0:0[0x1](und): Video: mpeg4 (Simple Profile) (mp4v / 0x7634706D), yuv420p, 2560x1080 [SAR 1:1 DAR 64:27], 16126 kb/s, 25 fps, 25 tbr, 12800 tbn (default)
      Metadata:
        handler_name    : VideoHandler
        vendor_id       : [0][0][0][0]
[aac @ 0000016582738840] Estimating duration from bitrate, this may be inaccurate
Input #1, aac, from 'audio_input_video.mp4.aac':
  Duration: 00:04:41.40, bitrate: 121 kb/s
  Stream #1:0: Audio: aac (LC), 44100 Hz, stereo, fltp, 121 kb/s
Stream mapping:
  Stream #0:0 -> #0:0 (mpeg4 (native) -> h264 (libx264))
  Stream #1:0 -> #0:1 (aac (native) -> aac (native))
Press [q] to stop, [?] for help
[libx264 @ 0000016582754dc0] using SAR=1/1
[libx264 @ 0000016582754dc0] using cpu capabilities: MMX2 SSE2Fast SSSE3 SSE4.2 AVX FMA3 BMI2 AVX2
[libx264 @ 0000016582754dc0] profile High, level 5.0, 4:2:0, 8-bit
[libx264 @ 0000016582754dc0] 264 - core 164 r3190 7ed753b - H.264/MPEG-4 AVC codec - Copyleft 2003-2024 - http://www.videolan.org/x264.html - options: cabac=1 ref=3 deblock=1:0:0 analyse=0x3:0x113 me=hex subme=7 psy=1 psy_rd=1.00:0.00 mixed_ref=1 me_range=16 chroma_me=1 trellis=1 8x8dct=1 cqm=0 deadzone=21,11 fast_pskip=1 chroma_qp_offset=-2 threads=18 lookahead_threads=3 sliced_threads=0 nr=0 decimate=1 interlaced=0 bluray_compat=0 constrained_intra=0 bframes=3 b_pyramid=2 b_adapt=1 b_bias=0 direct=1 weightb=1 open_gop=0 weightp=2 keyint=250 keyint_min=25 scenecut=40 intra_refresh=0 rc_lookahead=40 rc=crf mbtree=1 crf=23.0 qcomp=0.60 qpmin=0 qpmax=69 qpstep=4 ip_ratio=1.40 aq=1:1.00
Output #0, mp4, to 'final_resized_input_video.mp4':
  Metadata:
    major_brand     : isom
    minor_version   : 512
    compatible_brands: isomiso2mp41
    encoder         : Lavf61.1.100
  Stream #0:0(und): Video: h264 (avc1 / 0x31637661), yuv420p(progressive), 2560x1080 [SAR 1:1 DAR 64:27], q=2-31, 25 fps, 12800 tbn (default)
      Metadata:
        handler_name    : VideoHandler
        vendor_id       : [0][0][0][0]
        encoder         : Lavc61.3.100 libx264
      Side data:
        cpb: bitrate max/min/avg: 0/0/0 buffer size: 0 vbv_delay: N/A
  Stream #0:1: Audio: aac (LC) (mp4a / 0x6134706D), 44100 Hz, stereo, fltp, 128 kb/s
      Metadata:
        encoder         : Lavc61.3.100 aac
[out#0/mp4 @ 00000165826d4580] video:264113KiB audio:3841KiB subtitle:0KiB other streams:0KiB global headers:0KiB muxing overhead: 0.061060%
frame= 5991 fps= 25 q=-1.0 Lsize=  268117KiB time=00:03:59.56 bitrate=9168.5kbits/s speed=1.01x
[libx264 @ 0000016582754dc0] frame I:72    Avg QP:20.11  size: 82695
[libx264 @ 0000016582754dc0] frame P:5226  Avg QP:23.48  size: 46142
[libx264 @ 0000016582754dc0] frame B:693   Avg QP:25.00  size: 33704
[libx264 @ 0000016582754dc0] consecutive B-frames: 79.8% 13.1%  3.8%  3.3%
[libx264 @ 0000016582754dc0] mb I  I16..4: 20.9% 77.4%  1.7%
[libx264 @ 0000016582754dc0] mb P  I16..4:  8.1% 30.1%  0.5%  P16..4: 41.6%  6.0%  1.5%  0.0%  0.0%    skip:12.2%
[libx264 @ 0000016582754dc0] mb B  I16..4:  3.7% 13.9%  0.2%  B16..8: 41.5%  7.2%  0.9%  direct: 2.6%  skip:30.0%  L0:64.3% L1:30.9% BI: 4.9%
[libx264 @ 0000016582754dc0] 8x8 transform intra:77.8% inter:91.2%
[libx264 @ 0000016582754dc0] coded y,uvDC,uvAC intra: 45.4% 67.1% 11.9% inter: 18.9% 29.1% 0.6%
[libx264 @ 0000016582754dc0] i16 v,h,dc,p: 29% 27% 16% 28%
[libx264 @ 0000016582754dc0] i8 v,h,dc,ddl,ddr,vr,hd,vl,hu: 30% 22% 28%  3%  3%  3%  3%  4%  3%
[libx264 @ 0000016582754dc0] i4 v,h,dc,ddl,ddr,vr,hd,vl,hu: 31% 20% 12%  5%  9%  8%  7%  5%  3%
[libx264 @ 0000016582754dc0] i8c dc,h,v,p: 43% 24% 25%  8%
[libx264 @ 0000016582754dc0] Weighted P-Frames: Y:0.2% UV:0.2%
[libx264 @ 0000016582754dc0] ref P L0: 79.9% 10.6%  7.2%  2.4%
[libx264 @ 0000016582754dc0] ref B L0: 90.1%  8.9%  1.0%
[libx264 @ 0000016582754dc0] ref B L1: 99.2%  0.8%
[libx264 @ 0000016582754dc0] kb/s:9028.56
[aac @ 00000165827084c0] Qavg: 537.530
All videos have been processed.
PS C:\Users\ishan\OneDrive\Desktop\fff\Audip> 
