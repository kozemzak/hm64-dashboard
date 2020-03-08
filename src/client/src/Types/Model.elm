module Types.Model exposing (Model, initialModel)

import Types.Page exposing (Page(..), PageState(..))


type alias Model =
    { currentPage : Page
    , state : PageState
    , debugString : String
    , girlNames : List String
    }


initialModel : Model
initialModel =
    { currentPage = Home
    , state = Loading
    , debugString = "{}"
    , girlNames = []
    }
