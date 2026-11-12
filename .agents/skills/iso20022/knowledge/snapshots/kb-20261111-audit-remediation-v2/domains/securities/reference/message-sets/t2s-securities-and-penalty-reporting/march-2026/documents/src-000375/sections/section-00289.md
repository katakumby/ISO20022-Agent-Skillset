---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.18 Miscellaneous", "7.1.18.8 NettingEligibility4Choice"]
file_pages: [366]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.18.8 NettingEligibility4Choice

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 366 to 366.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 366

```text
7.1.18.8  NettingEligibility4Choice
Definition: Choice of format for the netting eligibility information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Indicator <Ind> [1..1] Indicator 366
Or}   Proprietary <Prtry> [1..1] ± 366
7.1.18.8.1  Indicator <Ind>
Presence: [1..1]
Definition: Specifies whether the settlement transaction is eligible for netting.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 553):
• Meaning When True: Yes
• Meaning When False: No
7.1.18.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Netting eligibility expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification30" on page 352 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 352
   Issuer <Issr> [1..1] Text 352
   SchemeName <SchmeNm> [0..1] Text 353
7.1.18.9  ClassificationType1Choice
Definition: Choice of format for the classification.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   ClassificationFinancialInstrument <ClssfctnFinInstrm> [1..1] IdentifierSet 366
Or}   AlternateClassification <AltrnClssfctn> [1..1] ± 366
7.1.18.9.1  ClassificationFinancialInstrument <ClssfctnFinInstrm>
Presence: [1..1]
Definition: ISO 10962 Classification of Financial Instrument (CFI).
Datatype: "CFIOct2015Identifier" on page 551
7.1.18.9.2  AlternateClassification <AltrnClssfctn>
Presence: [1..1]
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 366 March 2026
```

