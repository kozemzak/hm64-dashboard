module Types.Model exposing (Model, initialModel)

import Types.Page exposing (Page(..), PageState(..))


type alias Model =
    { currentPage : Page
    , state : PageState
    , debugString : String
    }


initialModel : Model
initialModel =
    Model Home Loading "{}"
