module Main exposing (main, update, view)

import Browser
import Commands.GetAllJson exposing (handleAllData)
import Commands.GetMetadata exposing (getMetadata, handleMetadata)
import Json.Decode exposing (decodeString, list, string)
import Subscriptions.DataPoller exposing (handleTick, pollData)
import Types.Model exposing (Model, initialModel)
import Types.Msg exposing (Msg(..))
import Views.Layout exposing (mainLayout)


main =
    Browser.document
        { init = init
        , update = update
        , view = view
        , subscriptions = \_ -> pollData
        }


init : () -> ( Model, Cmd Msg )
init _ =
    ( initialModel, getMetadata )


update : Msg -> Model -> ( Model, Cmd Msg )
update msg model =
    case msg of
        ChangePage newPage ->
            ( { model | currentPage = newPage }, Cmd.none )

        ReceivedAllJson result ->
            handleAllData model result

        ReceivedMetadata result ->
            handleMetadata model result

        Tick _ ->
            ( model, handleTick model.meta )


view model =
    { title = "Harvest Moon Dash"
    , body = [ mainLayout model ]
    }
