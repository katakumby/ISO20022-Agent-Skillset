---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.28 Status", "7.1.28.14 InstructionProcessingReason4Choice", "7.1.28.14.1 Reason <Rsn>", "7.1.28.14.1.1 Code <Cd>", "7.1.28.14.1.1.2 Proprietary <Prtry>"]
file_pages: [602]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.28.14.1.1.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../raw-input/post_trade_matching/ISO20022_MDRPart2_PostTradeMatching_2024_2025_v1.pdf). Locator: one-based file pages 602 to 602.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 602

```text
CodeName Name Definition
PHYS PhysicalSettlementImpossible Physical settlement is impossible for the
instructed financial instrument.
PLCE PlaceOfTrade Unrecognised or invalid place of trade.
CTRA ClosingTransactionAmount Unrecognised or invalid closing
transaction amount.
REPO RepurchaseRate Unrecognised or invalid repurchase rate.
REPP PremiumAmount Unrecognised or invalid premium
amount.
RERT RepurchaseRateType Unrecognised or invalid repurchase rate
type.
RSPR SpreadRate Unrecognised or invalid spread rate.
RTGS ImpossibleToUseTheRTGSSystemInstructed Impossible to use the RTGS system
instructed (NRTG or YRTG).
SAFE SafekeepingAccount Unrecognised or invalid message
sender's safekeeping account.
SETR SettlementTransaction Unrecognised or invalid settlement
transaction type.
SETS SettlementSystemMethod Unrecognised or invalid settlement
system/method instructed.
TERM ClosingDateTime Unrecognised or invalid closing date/
time.
TXST TaxStatus Unrecognised or invalid tax status of the
securities instructed.
ULNK Unknown Message was not recognised. Unknown
linked reference.
VASU VariableRateSupport Unrecognised or invalid variable rate
support (repurchase agreement).
7.1.28.14.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Specifies the reason why the instruction/request has a repair or rejection status.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.28.14.1.2  AdditionalReasonInformation <AddtlRsnInf>
Presence: [0..1]
Definition: Provides additional information about the reason in narrative form.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 602 February 2025
```

