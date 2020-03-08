module Types.Model exposing (Model, initialModel)

import Types.Metadata exposing (Metadata, initialMetadata)
import Types.Page exposing (Page(..), PageState(..))


type alias Model =
    { currentPage : Page
    , state : PageState
    , debugString : String
    , meta : Maybe Metadata
    }


initialModel : Model
initialModel =
    { currentPage = Home
    , state = Loading
    , debugString = "{}"
    , meta = Nothing
    }
