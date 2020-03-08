module Commands.GetAllJson exposing (getAllJson)

import Types.Msg exposing (Msg(..))
import Http

getAllJson : Cmd Msg
getAllJson =
    Http.get
        { url = "http://localhost:3000"
        , expect = Http.expectString ReceivedAllJson
        }