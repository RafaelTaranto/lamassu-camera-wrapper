{
    "targets": [
        {
            "target_name": "camera-wrapper",
            "sources": [
                "src/native/camera.cpp",
                "src/native/types.cpp",
                "src/native/thread.cpp",
                "src/native/supyo.cpp",
                "src/native/pico/picort.cpp"
            ],
            "dependencies": [
                "deps/opencv/opencv.gyp:libopencv",
            ],
            "include_dirs": [
                'deps/opencv/include',
                'deps/opencv/modules/core/include',
                'deps/opencv/modules/dynamicuda/include',
                'deps/opencv/modules/features2d/include',
                'deps/opencv/modules/flann/include',
                'deps/opencv/modules/highgui/include',
                'deps/opencv/modules/imgproc/include',
                'deps/opencv/modules/objdetect/include',
                'deps/opencv/modules/video/include',
            ],
            "cflags": [
                "-g", "-std=c++11", "-Wall"
            ],
            "conditions": [
                ['OS=="linux"', {
                    'cflags!': ['-fno-exceptions'],
                    'cflags_cc!': ['-fno-rtti', '-fno-exceptions']
                }],
                ['OS=="mac"', {
                    'xcode_settings': {
                        'MACOSX_DEPLOYMENT_TARGET' : '10.7',
                        'OTHER_CFLAGS': [
                            "-mmacosx-version-min=10.7",
                            "-std=c++11",
                            "-stdlib=libc++"
                        ],
                        'GCC_ENABLE_CPP_EXCEPTIONS': 'YES',
                        'GCC_ENABLE_CPP_RTTI': 'YES'
                    }
                }]
            ]
        }
    ]
}
