module Commands.GetGirlNames exposing (getGirlNames)

import Types.Msg exposing (Msg(..))
import Http

getGirlNames : Cmd Msg
getGirlNames =
    Http.get
        { url = "http://localhost:3000/girls"
        , expect = Http.expectString ReceivedGirlNames
        }