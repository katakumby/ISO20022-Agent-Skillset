---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.51 ExposureType18Choice", "7.1.19.51.2 Proprietary <Prtry>"]
file_pages: [376]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.51.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 376 to 376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 376

```text
CodeName Name Definition
TRCP TreasuryCrossProduct Combination of treasury related
exposure types.
BFWD BondForward Any securities traded out beyond 3 days
which include treasury notes, Japanese
Governement Bonds (JGBs) and Gilts.
RVPO ReverseRepurchaseAgreement In support of a reverse repurchase
agreement transaction.
TBAS ToBeAnnounced To be announced (TBA) related
collateral.
7.1.19.51.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Collateral movement exposure type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.19.52  NumberCount1Choice
Definition: Choice of number count type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   CurrentInstructionNumber <CurInstrNb> [1..1] Text 376
Or}   TotalNumber <TtlNb> [1..1]  C17,
C10
377
     CurrentInstructionNumber <CurInstrNb> [1..1] Text 377
     TotalOfLinkedInstructions <TtlOfLkdInstrs> [1..1] Text 377
Constraints
• CurrentInstructionNumberRule
If the Sender wants to indicate that this instruction is linked to one or more settlement instruction,
then the CurrentInstructionNumber must be specified.
7.1.19.52.1  CurrentInstructionNumber <CurInstrNb>
Presence: [1..1]
Definition: Sequential number of the instruction in a range of linked settlement instructions.
Datatype: "Exact3NumericText" on page 667
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 376 February 2025
```

