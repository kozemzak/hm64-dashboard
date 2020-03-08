module Main exposing (main, update, view)

import Basics
import Browser
import Html exposing (Html)
import Http
import Json.Decode exposing (decodeString, list, string)
import Time
import Types.GameState exposing (gameStateDecoder)
import Types.Model exposing (Model, initialModel)
import Types.Msg exposing (Msg(..))
import Types.Page exposing (Page(..), PageState(..))
import Views.Layout exposing (mainLayout)
import Commands.GetAllJson exposing (getAllJson)
import Commands.GetGirlNames exposing (getGirlNames)


main =
    Browser.document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }


init : () -> ( Model, Cmd Msg )
init _ =
    ( initialModel, getGirlNames )


subscriptions : Model -> Sub Msg
subscriptions model =
    Time.every 1000 Tick


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ChangePage newPage ->
            ( { model | currentPage = newPage }, Cmd.none )

        ReceivedAllJson (Ok jsonString) ->
            let
                result =
                    decodeString (gameStateDecoder model.girlNames) jsonString
            in
            case result of
                Ok gameState ->
                    ( { model | state = Success gameState jsonString }, Cmd.none )

                Err _ ->
                    ( { model | state = Failure "Parsing json failed" }, Cmd.none )
        
        ReceivedAllJson (Err err) ->
            ( { model | state = Failure "Http request failed" }, Cmd.none )

        ReceivedGirlNames (Ok jsonString) ->
            case (decodeString (list string) jsonString) of
                Ok names ->
                    ( { model | girlNames = names }, getAllJson)
                
                Err _ ->
                    ( { model | state = Failure "Could not parse girl names" }, Cmd.none)

        ReceivedGirlNames (Err err) ->
            ( { model | state = Failure "Http request failed" }, Cmd.none )

        Tick _ ->
            ( model, getAllJson )


view model =
    { title = "Harvest Moon Dash"
    , body = [ mainLayout model ]
    }
