module Pages.Recipes exposing (recipeView)

import Element exposing (..)
import Element.Font as Font


recipeView : Element msg
recipeView =
    column
        [ centerY
        , centerX
        , spacing 40
        , padding 120
        ]
        [ el [ width fill, Font.center, Font.size 40 ] (text "RECIPES")
        , row [ spacing 30, centerX ]
            [ text "Recipe"
            , text "Picture"
            , text "Recipe Name"
            , text "You have it?"
            ]
        ]
