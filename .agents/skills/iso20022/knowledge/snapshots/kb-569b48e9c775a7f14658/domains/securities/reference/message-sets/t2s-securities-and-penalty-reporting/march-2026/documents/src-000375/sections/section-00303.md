---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.24 SettlementOrCorporateActionEvent26Choice"]
file_pages: [382]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.24 SettlementOrCorporateActionEvent26Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 382 to 382.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 382

```text
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.24  SettlementOrCorporateActionEvent26Choice
Definition: Choice between transaction type, corporate action event and settlement transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 382
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 382
7.1.18.24.1  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType48Choice" on page 376 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 376
Or}   Proprietary <Prtry> [1..1] ± 379
7.1.18.24.2  CorporateActionEventType <CorpActnEvtTp>
Presence: [1..1]
Definition: Specifies the type of corporate event.
Impacted by: C13 "EventTypeRule"
CorporateActionEventType <CorpActnEvtTp> contains one of the following elements (see
"CorporateActionEventType73Choice" on page 403 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 404
Or}   Proprietary <Prtry> [1..1] ± 410
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 382 March 2026
```

