module Views.Main exposing (mainView)

import Element exposing (..)
import Loaders
import Types.Model exposing (Model)
import Types.Page exposing (PageState(..))
import Views.PageView exposing (pageView)


mainView : Model -> Element msg
mainView model =
    case model.state of
        Loading ->
            el [ centerX, centerY ] <| html <| Loaders.grid 40 "#fff"

        Failure msg ->
            el [ centerX, centerY ] (text <| "Failure: " ++ msg)

        Success gameState debugString ->
            pageView model.currentPage gameState debugString
