module Views.Layout exposing (mainLayout)

import Element exposing (..)
import Element.Background as Background
import Element.Font as Font
import Html exposing (Html)
import Html.Attributes
import Types.Model exposing (Model)
import Types.Msg exposing (Msg)
import Views.Colors exposing (..)
import Views.Main exposing (mainView)
import Views.Sidebar exposing (sidebar)


mainLayout : Model -> Html Msg
mainLayout model =
    layout
        [ Font.family
            [ Font.external
                { url = "https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap"
                , name = "Roboto Mono"
                }
            , Font.sansSerif
            ]
        ]
    <|
        row [ width fill, height fill, htmlAttribute (Html.Attributes.style "height" "1vh") ]
            [ el
                [ width (fillPortion 1)
                , height fill
                , Background.color lightColor
                , Font.color darkColor
                ]
                sidebar
            , el
                [ width <| fillPortion 5
                , height fill
                , scrollbarY
                , scrollbarX
                , Background.color darkColor
                , Font.color lightColor
                , padding 20
                ]
                (mainView model)
            ]
