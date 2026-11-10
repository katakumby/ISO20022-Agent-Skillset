---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["48 reda.028.001.01 CollateralDataStatusAdviceV01", "48.4 Message Building Blocks", "48.4.3 StatusReasonAndFinancialInstrument <StsRsnAndFinInstrm>", "48.4.3.2 Reason <Rsn>", "48.4.3.2.3 AdditionalInformation <AddtlInf>"]
file_pages: [2201]
content_origin: "source-text-extraction"
mentioned_message_ids: ["reda.028.001.01"]
---

# 48.4.3.2.3 AdditionalInformation <AddtlInf>

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2201 to 2201.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2201

```text
Impacted by: C1 "DescriptionPresenceRule", C2 "DescriptionUsageRule", C3 "ISINGuideline", C4
"ISINPresenceRule", C5 "OtherIdentificationPresenceRule"
FinancialInstrument <FinInstrm> contains the following elements (see "SecurityIdentification19" on
page 2951 for details)
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
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
On Condition
    /ISIN is absent
Following Must be True
    /OtherIdentification[*] Must be present
 Or    /Description Must be present
• OtherIdentificationPresenceRule
If OtherIdentification is not present then either ISIN or Description must be present.
On Condition
    /OtherIdentification[*] is absent
Following Must be True
    /ISIN Must be present
 Or    /Description Must be present
48.4.3.2.3  AdditionalInformation <AddtlInf>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
reda.028.001.01 CollateralDataStatusAdviceV01
Target2-Securities 2201 August 2026
```

