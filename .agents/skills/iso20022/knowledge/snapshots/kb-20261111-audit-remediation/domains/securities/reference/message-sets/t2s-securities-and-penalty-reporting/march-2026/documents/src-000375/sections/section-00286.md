---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.3 ClassificationType32Choice"]
file_pages: [363]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.3 ClassificationType32Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 363 to 363.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 363

```text
7.1.18.3  ClassificationType32Choice
Definition: Choice of format for the classification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 363
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 363
7.1.18.3.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: ISO 10962 Classification of Financial Instrument (CFI).
Datatype: "CFIOct2015Identifier" on page 551
7.1.18.3.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Definition: Proprietary classification of financial instrument.
AlternateClassification <AltrnClssfctn> contains the following elements (see
"GenericIdentification36" on page 350 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 350
   Issuer <Issr> [1..1] Text 350
   SchemeName <SchmeNm> [0..1] Text 351
7.1.18.4  Pagination1
Definition: Number used to sequence pages when it is not possible for data to be conveyed in a single
message and the data has to be split across several pages (messages).
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   PageNumber <PgNb> [1..1] Text 363
   LastPageIndicator <LastPgInd> [1..1] Indicator 363
7.1.18.4.1  PageNumber <PgNb>
Presence: [1..1]
Definition: Page number.
Datatype: "Max5NumericText" on page 558
7.1.18.4.2  LastPageIndicator <LastPgInd>
Presence: [1..1]
Definition: Indicates the last page.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 363 March 2026
```

