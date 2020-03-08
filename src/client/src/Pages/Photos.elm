module Pages.Photos exposing (photosView)

import Element exposing (..)
import Element.Font as Font


photosView : Element msg
photosView =
    column
        [ centerY
        , centerX
        , spacing 40
        , padding 120
        ]
        [ el [ width fill, Font.center, Font.size 40 ] (text "PHOTOS")
        , row [ spacing 30, centerX ]
            [ text "Picture"
            , text "Picture name"
            , text "You have it?"
            ]
        ]
