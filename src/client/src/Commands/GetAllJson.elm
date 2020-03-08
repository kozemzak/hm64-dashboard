module Commands.GetAllJson exposing (getAllJson, handleAllData)

import Http
import Json.Decode exposing (decodeString)
import Types.GameState exposing (gameStateDecoder)
import Types.Model exposing (Model)
import Types.Msg exposing (Msg(..))
import Types.Page exposing (PageState(..))


{-| Sends a request to get the values of all Features in the game state.
-}
getAllJson : Cmd Msg
getAllJson =
    Http.get
        { url = "http://localhost:3000"
        , expect = Http.expectString ReceivedAllJson
        }


{-| Handles the result of the request for all data.

    Ensures that the http request succeeded, and that the result of the request can be parsed.

-}
handleAllData : Model -> Result Http.Error String -> ( Model, Cmd Msg )
handleAllData model result =
    case ( result, model.meta ) of
        ( Ok jsonString, Just meta ) ->
            case decodeString (gameStateDecoder meta) jsonString of
                Ok gameState ->
                    ( { model | state = Success gameState jsonString }, getAllJson )

                Err _ ->
                    ( { model | state = Failure "Could not parse json" }, Cmd.none )

        ( Ok jsonString, Nothing ) ->
            ( model, Cmd.none )

        ( Err _, _ ) ->
            ( { model | state = Failure "Http Request for all data failed" }, Cmd.none )
