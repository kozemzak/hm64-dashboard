module Pages.Home exposing (homeView)

import Element exposing (..)
import Element.Font as Font
import Types.GameState exposing (GameState)
import Views.ProgressBar exposing (progressBar)


homeView : GameState -> Element msg
homeView state =
    column [ height fill, centerX, spaceEvenly, padding 120 ]
        [ el [ width fill, Font.center, Font.size 40 ] (text "HOME")
        , row [ spacing 30, centerX ]
            [ text state.playerName
            , text "Player Icon"
            , text state.farmName
            ]
        , row [ spacing 30, centerX ]
            [ text "today weather icon"
            , text "tomorrow weather"
            , text "next day weather"
            , text "day"
            , text "date"
            , text "season"
            , text "year"
            ]
        , row [ spacing 30, centerX ]
            [ progressBar "Stamina" state.stamina state.maxStamina 20
            , progressBar "Stamina" state.stamina state.maxStamina 50
            , progressBar "Stamina" state.stamina state.maxStamina 100
            , progressBar "Stamina" state.stamina state.maxStamina 250
            ]
        ]
