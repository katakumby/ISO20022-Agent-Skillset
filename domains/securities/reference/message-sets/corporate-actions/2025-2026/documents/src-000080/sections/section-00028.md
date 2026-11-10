---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["2 head.001.001.02 BusinessApplicationHeaderV02", "3.4 Message Building Blocks", "3.4.6 EventsLinkage <EvtsLkg>", "3.4.7.7 UnderlyingSecurity <UndrlygScty>", "3.4.7.7.1 FinancialInstrumentIdentification <FinInstrmId>"]
file_pages: [68]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.031.001.16"]
---

# 3.4.7.7.1 FinancialInstrumentIdentification <FinInstrmId>

Source: [src-000080](../../../../../../../../../raw-input/corporate_actions/ISO20022_MDRPart2_CorporateActions_2025_2026_v1.pdf). Locator: one-based file pages 68 to 68.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 68

```text
Constraints
• MaturityDateRule
Maturity date may only provide generic information about the final maturity of the underlying
instrument.
• PreviousNextFactorRule
In case of partial redemption by pool factor, PreviousFactor provides the factor applicable before
redemption and NextFactor provides the factor applicable after redemption.
3.4.7.7.1  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Identifies the financial instrument.
Impacted by: C23 "DescriptionPresenceRule", C24 "DescriptionUsageRule", C61 "ISINGuideline", C62
"ISINPresenceRule", C91 "OtherIdentificationPresenceRule"
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
• ISINGuideline
When an ISIN code exists, it is strongly recommended that the ISIN be used.
• ISINPresenceRule
If ISIN is not present then either Description or at least one occurrence of OtherIdentification must be
present.
Approved by the Securities SEG on 27 January 2026 seev.031.001.16 CorporateActionNotificationV16
Corporate Actions - Maintenance 2025 - 2026 68 February 2026
```

