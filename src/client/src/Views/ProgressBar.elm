module Views.ProgressBar exposing (progressBar)

import Element exposing (..)
import Element.Font as Font
import Svg
import Svg.Attributes
import Views.Colors exposing (..)


{-| A circular progress bar with a label underneath

    progressBar "Some label" 78 100 250

    This would create a circle with an outline over 78 percent of it,
    with the text "78 / 100" inside it, with the label "Some label"
    underneath it. The circle would be 250px wide.

-}
progressBar : String -> Int -> Int -> Int -> Element msg
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
