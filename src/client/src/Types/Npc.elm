module Types.Npc exposing (Npc, npcsDecoder)

import Json.Decode as Decode exposing (Decoder, bool, int, string)
import Json.Decode.Pipeline exposing (hardcoded, optional, required)


type alias Npc =
    { name : String
    , affection : Int
    , hasHadConversation : Bool
    , hasGivenGift : Bool
    , heartColor : String
    , location : String
    , locationByte : Int
    }


npcsDecoder : List String -> Decoder (List Npc)
npcsDecoder names =
    List.foldr (Decode.map2 (::)) (Decode.succeed []) <| List.map npcDecoder names


npcDecoder : String -> Decoder Npc
npcDecoder name =
    Decode.succeed Npc
        |> hardcoded name
        |> optional (name ++ "_affection") int 0
        |> optional (name ++ "_conversation") bool False
        |> optional (name ++ "_gift") bool False
        |> optional (name ++ "_heart_color") string ""
        |> optional (name ++ "_location") string ""
        |> optional (name ++ "_location_byte") int 0
