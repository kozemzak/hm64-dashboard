module Decoders.GameState exposing (gameStateDecoder)

import Json.Decode as Decode exposing (Decoder, float, int, string)
import Json.Decode.Pipeline exposing (required)
import Types.GameState exposing (GameState)


gameStateDecoder : Decoder GameState
gameStateDecoder =
    Decode.succeed GameState
        |> required "gold" int
        |> required "hammer_uses" int
        |> required "player_stamina" int
        |> required "player_stamina_max" int
        |> required "player_name" string
        |> required "farm_name" string
        |> required "dog_affection" int
