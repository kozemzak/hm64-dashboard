module Main exposing (main, update, view)

import Basics
import Browser
import Decoders.GameState exposing (gameStateDecoder)
import Html exposing (Html)
import Http
import Json.Decode exposing (decodeString)
import Time
import Types.Model exposing (Model, initialModel)
import Types.Msg exposing (Msg(..))
import Types.Page exposing (Page(..), PageState(..))
import Views.Layout exposing (mainLayout)


main =
    Browser.document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }


init : () -> ( Model, Cmd Msg )
init _ =
    ( initialModel, sendRequest )


subscriptions : Model -> Sub Msg
subscriptions model =
    Time.every 1000 Tick


sendRequest : Cmd Msg
sendRequest =
    Http.get
        { url = "http://localhost:3000"
        , expect = Http.expectString ReceivedAllJson
        }


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ChangePage newPage ->
            ( { model | currentPage = newPage }, Cmd.none )

        ReceivedAllJson (Ok jsonString) ->
            let
                result =
                    decodeString gameStateDecoder jsonString
            in
            case result of
                Ok gameState ->
                    ( { model | state = Success gameState jsonString }, Cmd.none )

                Err _ ->
                    ( { model | state = Failure "Parsing json failed" }, Cmd.none )

        ReceivedAllJson (Err err) ->
            ( { model | state = Failure "Http request failed" }, Cmd.none )

        Tick _ ->
            ( model, sendRequest )


view model =
    { title = "Harvest Moon Dash"
    , body = [ mainLayout model ]
    }
