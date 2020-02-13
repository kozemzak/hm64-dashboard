module Main exposing (Msg(..), main, update, view)

import Basics
import Browser
import Element exposing (..)
import Element.Background as Background
import Element.Border as Border
import Element.Font as Font
import Element.Input
import Html exposing (Html)
import Html.Attributes
import Http
import Json.Decode as Decode exposing (Decoder, decodeString, float, int, string)
import Json.Decode.Pipeline exposing (required)
import Json.Print exposing (prettyString)
import Loaders
import Svg
import Svg.Attributes
import Time



-----------
-- TYPES --
-----------


type alias Model =
    { currentPage : Page
    , state : PageState
    , debugString : String
    }


type PageState
    = Loading
    | Failure String
    | Success GameState String


type alias GameState =
    { gold : Int
    , hammerUses : Int
    , stamina : Int
    , maxStamina : Int
    , playerName : String
    , farmName : String
    }


type Msg
    = ChangePage Page
    | ReceivedAllJson (Result Http.Error String)
    | Tick Time.Posix


type Page
    = Home
    | Recipes
    | Photos
    | Debug



------------------
-- JSON Decoder --
------------------


gameStateDecoder : Decoder GameState
gameStateDecoder =
    Decode.succeed GameState
        |> required "gold" int
        |> required "hammer_uses" int
        |> required "player_stamina" int
        |> required "player_stamina_max" int
        |> required "player_name" string
        |> required "farm_name" string



---------
-- App --
---------


main =
    Browser.document
        { init = init
        , update = update
        , view = view
        , subscriptions = subscriptions
        }


init : () -> ( Model, Cmd Msg )
init _ =
    ( Model Home Loading "{}"
    , sendRequest
    )


subscriptions : Model -> Sub Msg
subscriptions model =
    Time.every 1000 Tick



------------
-- Update --
------------


sendRequest : Cmd Msg
sendRequest =
    Http.get
        { url = "http://localhost:3000"
        , expect = Http.expectString ReceivedAllJson
        }


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
                    ( { model | state = Failure "Http request failed" }, Cmd.none )

        ReceivedAllJson (Err err) ->
            ( { model | state = Failure "Http request failed" }, Cmd.none )

        Tick _ ->
            ( model, sendRequest )



----------
-- View --
----------


lightColor : Color
lightColor =
    rgb255 240 240 240


darkColor : Color
darkColor =
    rgb255 20 20 20


view model =
    { title = "Harvest Moon Dash"
    , body = [ body model ]
    }


body : Model -> Html Msg
body model =
    layout
        [ Font.family
            [ Font.external
                { url = "https://fonts.googleapis.com/css?family=Roboto+Mono&display=swap"
                , name = "Roboto Mono"
                }
            , Font.sansSerif
            ]
        ]
    <|
        row [ width fill, height fill, htmlAttribute (Html.Attributes.style "height" "1vh") ]
            [ el
                [ width (fillPortion 1)
                , height fill
                , Background.color lightColor
                , Font.color darkColor
                ]
                sidebar
            , el
                [ width <| fillPortion 5
                , height fill
                , scrollbarY
                , Background.color darkColor
                , Font.color lightColor
                , padding 20
                ]
                (mainView model)
            ]


sidebar : Element Msg
sidebar =
    column
        [ spacing 40
        , centerY
        , centerX
        , Font.center
        ]
        [ Element.Input.button [ width fill ] { onPress = Just (ChangePage Home), label = text "Home" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Recipes), label = text "Recipes" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Photos), label = text "Photos" }
        , Element.Input.button [ width fill ] { onPress = Just (ChangePage Debug), label = text "Debug" }
        ]


mainView : Model -> Element Msg
mainView model =
    case model.state of
        Loading ->
            el [ centerX, centerY ] <| html <| Loaders.grid 40 "#fff"

        Failure msg ->
            el [ centerX, centerY ] (text <| "Failure: " ++ msg)

        Success gameState debugString ->
            pageView model.currentPage gameState debugString


pageView : Page -> GameState -> String -> Element Msg
pageView page state debugString =
    case page of
        Home ->
            homeView state

        Recipes ->
            recipeView

        Photos ->
            photosView

        Debug ->
            el [ centerX, centerY ] <| text <| Result.withDefault "{}" <| prettyString { columns = 120, indent = 4 } debugString


homeView : GameState -> Element Msg
homeView state =
    column [ height fill, centerX, spaceEvenly, padding 120 ]
        [ el [ width fill, Font.center, Font.size 40 ] (text "HOME")
        , row [ spacing 30, centerX ]
            [ text state.playerName
            , text "Player Icon"
            , text state.farmName
            ]
        , row [ spacing 30, centerX ]
            [ text "today weather icon"
            , text "tomorrow weather"
            , text "next day weather"
            , text "day"
            , text "date"
            , text "season"
            , text "year"
            ]
        , row [ spacing 30, centerX ]
            [ progressBar "Stamina" state.stamina state.maxStamina 20
            , progressBar "Stamina" state.stamina state.maxStamina 50
            , progressBar "Stamina" state.stamina state.maxStamina 100
            , progressBar "Stamina" state.stamina state.maxStamina 250
            ]

        --, row [ spacing 30, centerX ]
        --    [ text "Fatigue"
        --    , text "Alcohol Tolerance"
        --    ]
        ]


recipeView : Element Msg
recipeView =
    column
        [ centerY
        , centerX
        , spacing 40
        , padding 120
        ]
        [ el [ width fill, Font.center, Font.size 40 ] (text "RECIPES")
        , row [ spacing 30, centerX ]
            [ text "Recipe"
            , text "Picture"
            , text "Recipe Name"
            , text "You have it?"
            ]
        ]


photosView : Element Msg
photosView =
    column
        [ centerY
        , centerX
        , spacing 40
        , padding 120
        ]
        [ el [ width fill, Font.center, Font.size 40 ] (text "PHOTOS")
        , row [ spacing 30, centerX ]
            [ text "Picture"
            , text "Picture name"
            , text "You have it?"
            ]
        ]


{-| A circular progress bar with a label underneath

    progressBar "Some label" 78 100 250

    This would create a circle with an outline over 78 percent of it,
    with the text "78 / 100" inside it, with the label "Some label"
    underneath it. The circle would be 250px wide.

-}
progressBar : String -> Int -> Int -> Int -> Element Msg
progressBar label value maxVal pixelWidth =
    let
        rgbColor =
            toRgb lightColor

        svgColor =
            "rgb("
                ++ String.fromFloat (rgbColor.red * 100)
                ++ "%, "
                ++ String.fromFloat (rgbColor.green * 100)
                ++ "%, "
                ++ String.fromFloat (rgbColor.blue * 100)
                ++ "%)"

        fontSize =
            round (edgeSize / 5)

        edgeSize =
            2 * (radius + strokeWidth)

        innerText =
            String.fromInt value ++ "/" ++ String.fromInt maxVal

        strokeWidth =
            Basics.max (radius / 10.0) 2.0

        radius =
            toFloat pixelWidth / 2.0

        circumference =
            radius * 2.0 * Basics.pi

        percentFull =
            toFloat value / toFloat maxVal

        -- The main circle with a border covering (value / maxVal) percent of it
        circle =
            html <|
                Svg.svg
                    [ Svg.Attributes.width <| String.fromFloat edgeSize
                    , Svg.Attributes.height <| String.fromFloat edgeSize
                    ]
                    [ Svg.circle
                        [ Svg.Attributes.r <| String.fromFloat <| radius
                        , Svg.Attributes.cx <| String.fromFloat <| radius + strokeWidth
                        , Svg.Attributes.cy <| String.fromFloat <| radius + strokeWidth
                        , Svg.Attributes.strokeWidth (String.fromFloat strokeWidth)
                        , Svg.Attributes.fill "transparent"
                        , Svg.Attributes.strokeLinecap "round"
                        , Svg.Attributes.stroke svgColor
                        , Svg.Attributes.strokeDasharray <| String.fromFloat circumference ++ " " ++ String.fromFloat circumference
                        , Svg.Attributes.strokeDashoffset <| String.fromFloat <| circumference * (1.0 - percentFull)
                        ]
                        [ Svg.animate
                            [ Svg.Attributes.attributeName "stroke-dashoffset"
                            , Svg.Attributes.dur "1s"
                            ]
                            []
                        ]
                    , Svg.circle
                        [ Svg.Attributes.r <| String.fromFloat <| radius
                        , Svg.Attributes.cx <| String.fromFloat <| radius + strokeWidth
                        , Svg.Attributes.cy <| String.fromFloat <| radius + strokeWidth
                        , Svg.Attributes.strokeWidth "1"
                        , Svg.Attributes.fill "transparent"
                        , Svg.Attributes.stroke svgColor
                        ]
                        []
                    ]

        -- The label that goes inside the circle
        labelEl =
            el
                [ centerX
                , centerY
                , Font.color lightColor
                , Font.size fontSize
                ]
                (text innerText)
    in
    column [ spacing <| Basics.max (fontSize // 4) 5 ]
        [ el [ inFront labelEl ] <| el [ rotate (degrees -90) ] circle
        , el [ Font.size fontSize, centerX ] (text label)
        ]
