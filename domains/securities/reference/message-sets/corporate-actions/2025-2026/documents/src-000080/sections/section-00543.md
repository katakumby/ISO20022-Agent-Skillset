---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["11 seev.039.001.13 CorporateActionCancellationAdviceV13", "11.4 Message Building Blocks", "11.4.2 CorporateActionGeneralInformation <CorpActnGnlInf>", "11.4.2.5 MandatoryVoluntaryEventType <MndtryVlntryEvtTp>"]
file_pages: [709]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.039.001.13"]
---

# 11.4.2.5 MandatoryVoluntaryEventType <MndtryVlntryEvtTp>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 709 to 709.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 709

```text
If Code is present, the code REDM (Final Maturity) must only be used if the redemption is decided by
the issuer and not by the securities holders.
11.4.2.5  MandatoryVoluntaryEventType <MndtryVlntryEvtTp>
Presence: [1..1]
Definition: Specifies whether the event is mandatory, mandatory with options or voluntary.
MandatoryVoluntaryEventType <MndtryVlntryEvtTp> contains one of the following elements (see
"CorporateActionMandatoryVoluntary3Choice" on page 975 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 975
Or}   Proprietary <Prtry> [1..1] ± 975
11.4.2.6  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identification of the security concerned by the corporate action.
Impacted by: C3 "DescriptionPresenceRule", C4 "DescriptionUsageRule", C6 "ISINGuideline", C7
"ISINPresenceRule", C9 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 869 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 870
   OtherIdentification <OthrId> [0..*]  870
     Identification <Id> [1..1] Text 870
     Suffix <Sfx> [0..1] Text 870
     Type <Tp> [1..1] ± 871
   Description <Desc> [0..1] Text 871
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
Approved by the Securities SEG on 27 January 2026 seev.039.001.13
CorporateActionCancellationAdviceV13
Corporate Actions - Maintenance 2025 - 2026 709 February 2026
```

