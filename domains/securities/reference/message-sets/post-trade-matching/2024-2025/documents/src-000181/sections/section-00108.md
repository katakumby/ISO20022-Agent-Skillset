---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["4 setr.029.001.02 SecuritiesTradeConfirmationCancellationV02", "4.2 Structure"]
file_pages: [141]
content_origin: "source-text-extraction"
mentioned_message_ids: ["setr.029.001.02"]
---

# 4.2 Structure

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 141 to 141.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 141

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <SctiesTradConfCxl> [1..1]  
   Identification <Id> [1..1]  142
     TransactionIdentification <TxId> [1..1] Text 142
   References <Refs> [0..*] ± 142
   OtherBusinessParties <OthrBizPties> [0..1]  C6, C8 143
     Investor <Invstr> [0..*] ± C5 143
     StockExchange <StockXchg> [0..1] ± 144
     TradeRegulator <TradRgltr> [0..1] ± 145
     TripartyAgent <TrptyAgt> [0..1] ± 145
     QualifiedForeignIntermediary <QlfdFrgnIntrmy> [0..1] ± 145
   SupplementaryData <SplmtryData> [0..*] ± C10 146
4.3 Constraints
C1 AdditonalDetailsGuideline
Unless bilaterally agreed between the Sender and Receiver, DeclarationlDetails,
RegistrationDetails and PartyContactDetails must not contain information that can be provided
in a structured field.
C2 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C3 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C4 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C5 IdentificationUsageRule
The presence of Identification and/or CountryOfResidence is mandatory.
C6 InvestorUsageRule
When investor is used with a country code, the country code specifies the nationality of the
investor, for the settlement of certain securities (i.e. airlines, defence manufacturers) under the
EU legislation.
Approved by the Securities SEG on 13 February 2025 setr.029.001.02
SecuritiesTradeConfirmationCancellationV02
Post Trade Matching - Maintenance 2024 - 2025 141 February 2025
```

