---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.8 Charge", "66.1.8.1 Fees2", "66.1.8.1.2 IndividualFee <IndvFee>", "66.1.8.1.2.6 RecipientIdentification <RcptId>"]
file_pages: [4441]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.8.1.2.6 RecipientIdentification <RcptId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4441 to 4441.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4441

```text
66.1.8.1.2.6  RecipientIdentification <RcptId>
Presence: [0..1]
Definition: Party entitled to the amount of money resulting from the fee.
RecipientIdentification <RcptId> contains the following elements (see "PartyIdentification139" on
page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
66.1.8.2  CostsAndCharges2
Definition: Costs and charges associated with the distribution or selling of a financial instrument. These
may be one-off or recurring charges. These may be intended (ex ante) or actual (ex post).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ExAnteReferenceDate <ExAnteRefDt> [0..1] Date 4442
   IndividualCostOrCharge <IndvCostOrChrg> [1..*]  C14,
C15,
C31,
C32
4442
     CostType <CostTp> [1..1]  4443
{Or       Code <Cd> [1..1] CodeSet 4443
Or}       Proprietary <Prtry> [1..1] ± 4448
     ExAnteOrExPost <ExAnteOrExPst> [1..1] CodeSet 4448
     Amount <Amt> [0..1] Amount C1 4449
     Sign <Sgn> [0..1] Indicator 4449
     Rate <Rate> [0..1] Rate 4449
     ReferencePeriod <RefPrd> [0..1]  4449
       StartDate <StartDt> [1..1] Date 4450
       EndDate <EndDt> [1..1] Date 4450
     AdditionalInformation <AddtlInf> [0..1] ± 4450
   AdditionalInformation <AddtlInf> [0..1] ± 4450
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4441 May 2026
```

