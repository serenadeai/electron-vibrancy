{
    "targets": [
        {
            "target_name": "Vibrancy",
            "sources": [
                "src/Init.cc",
                "src/Vibrancy.h",
                "src/Vibrancy_empty.h",
            ],
            'conditions':[
                ['OS!="win"', {
                    "sources!": [
                        "src/Common.h",
                        "src/Vibrancy.cc",
                        "src/VibrancyHelper.h",
                        "src/vibrancy_win.cc",
                    ]
                }],
            ],
            "variables":{
                "CURRENT_DIR":"<!(echo %~dp0)"
            },
            "include_dirs": [
                "<!(node -e \"require('nan')\")"
            ]
        }
    ]
}
