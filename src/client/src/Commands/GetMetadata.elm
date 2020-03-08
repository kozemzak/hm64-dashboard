module Commands.GetMetadata exposing (getMetadata, handleMetadata)

import Commands.GetAllJson exposing (getAllJson)
import Http
import Json.Decode exposing (decodeString, maybe)
import Types.Metadata exposing (metadataDecoder)
import Types.Model exposing (Model)
import Types.Msg exposing (Msg(..))
import Types.Page exposing (PageState(..))


{-| Sends a request to get the values of metadata about the game.

    The metadata is useful for gathering information about the server schema.
    As an example, the metadata contains a list of all NPCs in the game. As the
    server adds more NPCs, it can update the metadata enpoint with their names,
    and this frontend will automatically add that NPC to the schema and to the
    page that displays a table of all NPCs.

-}
getMetadata : Cmd Msg
getMetadata =
    Http.get
        { url = "http://localhost:3000/meta"
        , expect = Http.expectString ReceivedMetadata
        }


{-| Handles the result of the request for metadata

    Ensures that the http request succeeded, and that the result of the request can be parsed.
    On success, we send out a `Cmd` to fetch all data from the server.

-}
handleMetadata : Model -> Result Http.Error String -> ( Model, Cmd Msg )
handleMetadata model result =
    case result of
        Ok jsonString ->
            case decodeString (maybe metadataDecoder) jsonString of
                Ok metadata ->
                    ( { model | meta = metadata }, getAllJson )

                Err _ ->
                    ( { model | state = Failure "Could not parse metadata" }, Cmd.none )

        Err _ ->
            ( { model | state = Failure "Http Request for metadata failed" }, Cmd.none )
