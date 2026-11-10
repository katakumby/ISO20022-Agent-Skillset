---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.27 Settlement Details", "7.1.27.1 SettlementDetails213", "7.1.27.1.1 SettlementTransactionType <SttlmTxTp>", "7.1.27.1.1.2 Proprietary <Prtry>"]
file_pages: [574]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.27.1.1.2 Proprietary <Prtry>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 574 to 574.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 574

```text
CodeName Name Definition
SYND SyndicateUnderwriters Relates to the issue of financial
instruments through a syndicate of
underwriters and a lead manager.
TBAC TBAClosing Relates to a To Be Announced (TBA)
closing trade.
TRAD Trade Relates to the settlement of a trade.
TRPO TripartyRepo Relates to a triparty repurchase
agreement.
TRVO TripartyReverseRepo Relates to a triparty reverse repurchase
agreement.
TURN Turnaround Relates to a turnaround: the same
security is bought and sold to settle the
same day, to or from different brokers.
GUAR GuaranteedClose Trade which is guaranteed to be
finalized.
OFIT OfferingIssuingTrade Offering issue trade.
7.1.27.1.1.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 276 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 276
   Issuer <Issr> [1..1] Text 276
   SchemeName <SchmeNm> [0..1] Text 276
7.1.27.1.2  HoldIndicator <HldInd>
Presence: [0..1]
Definition: Specifies whether the transaction is on hold/blocked/frozen.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 665):
• Meaning When True: Yes
• Meaning When False: No
7.1.27.1.3  Priority <Prty>
Presence: [0..1]
Definition: Specifies whether the transaction is to be executed with a high priority.
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 574 February 2025
```

