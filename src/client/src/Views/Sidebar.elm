module Views.Sidebar exposing (sidebar)

import Element exposing (..)
import Element.Font
import Element.Input
import Types.Msg exposing (Msg(..))
import Types.Page exposing (Page(..))


sidebar : Element Msg
sidebar =
    column
        [ spacing 40
        , centerY
        , centerX
        , Element.Font.center
        ]
        [ Element.Input.button [ width fill ] { onPress = Just (ChangePage Home), label = text "Home" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Affections), label = text "Affections" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Recipes), label = text "Recipes" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Photos), label = text "Photos" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Debug), label = text "Debug" }
        ]
