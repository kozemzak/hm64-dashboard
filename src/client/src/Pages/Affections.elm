module Pages.Affections exposing (affectionsView)

import Element exposing (..)
import Element.Font as Font
import Types.GameState exposing (GameState)


affectionsView : GameState -> Element msg
affectionsView state =
    column
        [ centerY
        , centerX
        , spacing 40
        , padding 120
        ]
        [ el [ width fill, Font.center, centerY, Font.size 40 ] (text "GIRL AFFECTIONS")
        , girlTable state
        ]


girlTable : GameState -> Element msg
girlTable state =
    table
        [ centerY
        , centerX
        , spacing 40
        , padding 120
        ]
        { data = state.girls
        , columns =
            [ { header = el [ Font.center, centerY ] <| text "Name"
              , width = fill
              , view = \npc -> el [ Font.center, centerY, centerY ] <| text npc.name
              }
            , { header = el [ Font.center, centerY ] <| text "Heart Color"
              , width = fill
              , view = \npc -> el [ Font.center, centerY ] <| text npc.heartColor
              }
            , { header = el [ Font.center, centerY ] <| text "Affection"
              , width = fill
              , view = \npc -> el [ Font.center, centerY ] <| text <| String.fromInt <| npc.affection
              }
            , { header = el [ Font.center, centerY ] <| text "Convo"
              , width = fill
              , view =
                    \npc ->
                        el [ Font.center, centerY ] <|
                            text <|
                                if npc.hasHadConversation then
                                    "Yes"

                                else
                                    "No"
              }
            , { header = el [ Font.center, centerY ] <| text "Gift"
              , width = fill
              , view =
                    \npc ->
                        el [ Font.center, centerY ] <|
                            text <|
                                if npc.hasGivenGift then
                                    "Yes"

                                else
                                    "No"
              }
            , { header = el [ Font.center, centerY ] <| text "Location"
              , width = fill
              , view = \npc -> el [ Font.center, centerY ] <| text npc.location
              }
            , { header = el [ Font.center, centerY ] <| text "Location Byte"
              , width = fill
              , view = \npc -> el [ Font.center, centerY ] <| text <| String.fromInt <| npc.locationByte
              }
            ]
        }
