---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["15 reda.004.001.07 FundReferenceDataReportV07", "15.4 Message Building Blocks", "15.4.5 Report <Rpt>", "15.4.5.8 SecurityIdentification <SctyId>", "15.4.5.8.1 Identification <Id>"]
file_pages: [312]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.004.001.07"]
---

# 15.4.5.8.1 Identification <Id>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 312 to 312.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 312

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   NoRetrocessionIndicator <NoRtrcssnInd> [0..1] Indicator 319
   ExPostCostCalculationBasis <ExPstCostClctnBsis> [0..1]  320
{Or     Code <Cd> [1..1] CodeSet 320
Or}     Proprietary <Prtry> [1..1] ± 320
   AdditionalInformation <AddtlInf> [0..*] ± 320
15.4.5.8.1  Identification <Id>
Presence: [1..1]
Definition: Identification of the security, typically by an ISIN.
Impacted by: C12 "DescriptionPresenceRule", C13 "DescriptionUsageRule", C21 "ISINGuideline", C22
"ISINPresenceRule", C27 "OtherIdentificationPresenceRule"
Identification <Id> contains the following SecurityIdentification40 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   OtherIdentification <OthrId> [0..*]  313
     Identification <Id> [1..1] Text 313
     Suffix <Sfx> [0..1] Text 313
     Type <Tp> [1..1] ± 313
   Description <Desc> [0..1] Text 314
   ISIN <ISIN> [0..1] IdentifierSet 314
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
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
Approved by the Securities SEG on 27 January 2026 reda.004.001.07 FundReferenceDataReportV07
Investment Funds - Maintenance 2025 - 2026 312 May 2026
```

