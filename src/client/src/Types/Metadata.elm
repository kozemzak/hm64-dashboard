module Types.Metadata exposing (Metadata, initialMetadata, metadataDecoder)

import Json.Decode as Decode exposing (Decoder, list, string)
import Json.Decode.Pipeline exposing (required)


type alias Metadata =
    { npcNames : List String
    , girlNames : List String
    , rivalNames : List String
    }


initialMetadata : Metadata
initialMetadata =
    { npcNames = []
    , girlNames = []
    , rivalNames = []
    }


metadataDecoder : Decoder Metadata
metadataDecoder =
    Decode.succeed Metadata
        |> required "npcs" (list string)
        |> required "girls" (list string)
        |> required "rivals" (list string)
