---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "T2S SecuritiesAndPenaltyReporting"
source_ids: ["src-000375"]
source_editions: ["march-2026"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.5 Balance", "7.1.5.14 Balance30", "7.1.5.14.2 BalanceForAccount <BalForAcct>", "7.1.5.14.2.1 BalanceDate <BalDt>"]
file_pages: [278]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.5.14.2.1 BalanceDate <BalDt>

Source: [src-000375](../../../../../../../../../evidence/omitted/e6546c5f64c53f963440988a.md) archive member `ISO20022_MDR_Target2Securities_August_2026_v1/Target2-Securities_SecuritiesAndPenaltyReporting_MessageSet/ISO20022_MDRPart2_Target2Securities_SecuritiesAndPenaltyReporting_v1.pdf`. Locator: one-based file pages 278 to 278.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 278

```text
• FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes is not
allowed.
7.1.5.14.2.1  BalanceDate <BalDt>
Presence: [1..1]
Definition: Specifies the date of the balance position.
BalanceDate <BalDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 320 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 320
Or}   DateTime <DtTm> [1..1] DateTime 320
7.1.5.14.2.2  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C4 "DescriptionPresenceRule", C5 "DescriptionUsageRule", C7 "ISINGuideline", C8
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 339 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 340
   OtherIdentification <OthrId> [0..*]  340
     Identification <Id> [1..1] Text 340
     Suffix <Sfx> [0..1] Text 340
     Type <Tp> [1..1] ± 341
   Description <Desc> [0..1] Text 341
Constraints
• DescriptionPresenceRule
If Description is not present then either ISIN or at least one occurrence of OtherIdentification must be
present.
On Condition
    /Description is absent
Following Must be True
    /ISIN Must be present
 Or    /OtherIdentification[*] Must be present
• DescriptionUsageRule
Description must be used alone as the last resort.
Approved by the Securities SEG 19 February 2026. Message Items Types
Target2-Securities - Securities and Penalty Reporting 278 March 2026
```

