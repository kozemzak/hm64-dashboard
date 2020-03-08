module Views.PageView exposing (pageView)

import Element exposing (..)
import Json.Print exposing (prettyString)
import Pages.Affections exposing (affectionsView)
import Pages.Home exposing (homeView)
import Pages.Photos exposing (photosView)
import Pages.Recipes exposing (recipeView)
import Types.GameState exposing (GameState)
import Types.Page exposing (Page(..))


pageView : Page -> GameState -> String -> Element msg
pageView page state debugString =
    case page of
        Home ->
            homeView state

        Affections ->
            affectionsView state

        Recipes ->
            recipeView

        Photos ->
            photosView

        Debug ->
            el [ centerX, centerY ] <| text <| Result.withDefault "{}" <| prettyString { columns = 120, indent = 4 } debugString
