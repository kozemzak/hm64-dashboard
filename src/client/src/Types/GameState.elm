module Types.GameState exposing (GameState, gameStateDecoder)

import Json.Decode as Decode exposing (Decoder, int, string)
import Json.Decode.Pipeline exposing (required, requiredAt)
import Types.Metadata exposing (Metadata)
import Types.Npc exposing (Npc, npcsDecoder)


type alias GameState =
    { gold : Int
    , hammerUses : Int
    , stamina : Int
    , maxStamina : Int
    , playerName : String
    , farmName : String
    , girls : List Npc
    }


gameStateDecoder : Metadata -> Decoder GameState
gameStateDecoder meta =
    Decode.succeed GameState
        |> required "gold" int
        |> required "hammer_uses" int
        |> required "player_stamina" int
        |> required "player_stamina_max" int
        |> required "player_name" string
        |> required "farm_name" string
        |> requiredAt [] (npcsDecoder meta.girlNames)
