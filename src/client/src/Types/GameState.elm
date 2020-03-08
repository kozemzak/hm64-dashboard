module Types.GameState exposing (GameState)


type alias GameState =
    { gold : Int
    , hammerUses : Int
    , stamina : Int
    , maxStamina : Int
    , playerName : String
    , farmName : String
    , dogAffection : Int
    }
