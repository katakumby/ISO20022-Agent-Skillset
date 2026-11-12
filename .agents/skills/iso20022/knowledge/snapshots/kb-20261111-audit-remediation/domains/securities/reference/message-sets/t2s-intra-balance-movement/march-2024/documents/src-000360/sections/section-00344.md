---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S IntraBalanceMovement"
source_ids: ["src-000360"]
source_editions: ["march-2024"]
message_ids: []
heading_path: ["17 Message Items Types", "17.1 MessageComponents", "17.1.12 Identification Information", "17.1.12.3 GenericIdentification36", "17.1.12.3.3 SchemeName <SchmeNm>"]
file_pages: [410]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 17.1.12.3.3 SchemeName <SchmeNm>

Source: [src-000360](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_IntraBalanceMovement_MessageSet/ISO20022_MDRPart2_Target2Securities_IntraBalanceMovement_2023_2024_v1.pdf`. Locator: one-based file pages 410 to 410.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 410

```text
Datatype: "Max35Text" on page 497
17.1.12.3.3  SchemeName <SchmeNm>
Presence: [0..1]
Definition: Short textual description of the scheme.
Datatype: "Max35Text" on page 497
17.1.13 Miscellaneous
17.1.13.1  Number3Choice
Definition: Choice of 3 and 5 exact numeric number.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Short <Shrt> [1..1] Text 410
Or}   Long <Lng> [1..1] Text 410
17.1.13.1.1  Short <Shrt>
Presence: [1..1]
Definition: Number of maximum 3 numeric text.
Datatype: "Exact3NumericText" on page 495
17.1.13.1.2  Long <Lng>
Presence: [1..1]
Definition: Number of maximum 5 numeric text. Is only to be used in a delta statement.
Datatype: "Exact5NumericText" on page 496
17.1.13.2  AdditionalParameters16
Definition: Specifies additional parameters to the message or transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PartialSettlement <PrtlSttlm> [0..1] CodeSet 411
   PreviousPartialConfirmationIdentification
<PrvsPrtlConfId>
[0..1] Text 411
   AccountOwnerTransactionIdentification <AcctOwnrTxId> [0..1] Text 411
   AccountServicerTransactionIdentification <AcctSvcrTxId> [0..1] Text 411
   PoolIdentification <PoolId> [0..1] Text 411
   CorporateActionEventIdentification <CorpActnEvtId> [0..1] Text 411
   MarketInfrastructureTransactionIdentification
<MktInfrstrctrTxId>
[0..1] Text 411
   ProcessorTransactionIdentification <PrcrTxId> [0..1] Text 412
Approved by the Securities and the Payments SEGs under the leadership of
the Securities SEG on 15 February 2024
Message Items Types
Target2-Securities - Intra-balance Movement - Maintenance
2023 - 2024
410 March 2024
```

