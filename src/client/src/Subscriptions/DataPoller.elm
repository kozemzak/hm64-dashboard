module Subscriptions.DataPoller exposing (handleTick, pollData)

import Commands.GetAllJson exposing (getAllJson)
import Time
import Types.Metadata exposing (Metadata)
import Types.Msg exposing (Msg(..))


{-| Subscribe to a clock, creating a `Tick` message every second
-}
pollData : Sub Msg
pollData =
    Time.every 1000 Tick


{-| Handle the `Tick` message.

    If we already have the metadata from our server, we can
    request the full set of features. If we don't have the metadata,
    we won't know how to handle the features, so we do nothing.

-}
handleTick : Maybe Metadata -> Cmd Msg
handleTick meta =
    case meta of
        Just metadata ->
            getAllJson

        Nothing ->
            Cmd.none
