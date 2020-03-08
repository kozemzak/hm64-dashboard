module Types.Msg exposing (Msg(..))

import Http
import Time
import Types.Page exposing (Page)


type Msg
    = ChangePage Page
    | ReceivedAllJson (Result Http.Error String)
    | Tick Time.Posix
