---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.5 Balance", "82.1.5.16 Balance30", "82.1.5.16.2 BalanceForAccount <BalForAcct>", "82.1.5.16.2.1 BalanceDate <BalDt>"]
file_pages: [2870]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.5.16.2.1 BalanceDate <BalDt>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2870 to 2870.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2870

```text
• FinancialInstrumentAttributesRule
If InvestmentFundsFinancialInstrumentAttributes is present, then FinancialInstrumentAttributes is not
allowed.
82.1.5.16.2.1  BalanceDate <BalDt>
Presence: [1..1]
Definition: Specifies the date of the balance position.
BalanceDate <BalDt> contains one of the following elements (see "DateAndDateTime1Choice" on
page 2912 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Date <Dt> [1..1] Date 2913
Or}   DateTime <DtTm> [1..1] DateTime 2913
82.1.5.16.2.2  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Financial instruments representing a sum of rights of the investor vis-a-vis the issuer.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C5 "ISINGuideline", C6
"ISINPresenceRule", C7 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 2951 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 2952
   OtherIdentification <OthrId> [0..*]  2952
     Identification <Id> [1..1] Text 2952
     Suffix <Sfx> [0..1] Text 2952
     Type <Tp> [1..1] ± 2952
   Description <Desc> [0..1] Text 2953
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
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2870 August 2026
```

