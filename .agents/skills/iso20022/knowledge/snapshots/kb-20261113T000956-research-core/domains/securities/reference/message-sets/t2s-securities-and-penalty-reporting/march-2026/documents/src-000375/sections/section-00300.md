---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.20 SecuritiesTransactionType48Choice", "7.1.18.20.2 Proprietary <Prtry>"]
file_pages: [379]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.20.2 Proprietary <Prtry>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 379 to 379.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 379

```text
CodeName Name Definition
(subscription or switch), but to account
management.
TOUT TransferOut Transaction is a debit to an account on
the shareholders register, and is not
linked to a shift in investment
(redemption or switch), but to account
management.
7.1.18.20.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Securities transaction type expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.21  SettlementOrCorporateActionEvent27Choice
Definition: Choice between transaction type, corporate action event and settlement transaction.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   SecuritiesTransactionType <SctiesTxTp> [1..1] ± 379
Or}   CorporateActionEventType <CorpActnEvtTp> [1..1] ± C13 379
7.1.18.21.1  SecuritiesTransactionType <SctiesTxTp>
Presence: [1..1]
Definition: Identifies the type of securities transaction.
SecuritiesTransactionType <SctiesTxTp> contains one of the following elements (see
"SecuritiesTransactionType44Choice" on page 395 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 395
Or}   Proprietary <Prtry> [1..1] ± 397
7.1.18.21.2  CorporateActionEventType <CorpActnEvtTp>
Presence: [1..1]
Definition: Specifies the type of corporate event.
Impacted by: C13 "EventTypeRule"
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 379 March 2026
```

