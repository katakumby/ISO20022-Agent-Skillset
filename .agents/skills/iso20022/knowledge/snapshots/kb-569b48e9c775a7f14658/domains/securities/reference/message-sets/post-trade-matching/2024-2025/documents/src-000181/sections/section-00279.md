---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.19 Miscellaneous", "7.1.19.43 Order23", "7.1.19.43.4 SecondaryClientOrderIdentification <ScndryClntOrdrId>"]
file_pages: [339]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.19.43.4 SecondaryClientOrderIdentification <ScndryClntOrdrId>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 339 to 339.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 339

```text
7.1.19.43.4  SecondaryClientOrderIdentification <ScndryClntOrdrId>
Presence: [0..*]
Definition: Assigned by the party that originates the order. Can be used to provide the
ClientOrderIdentification used by an exchange or executing system.
Datatype: "Max35Text" on page 669
7.1.19.43.5  ListIdentification <ListId>
Presence: [0..*]
Definition: Unique identifier for a list, as assigned by the trading party. The identifier must be unique
within a single trading day.
Datatype: "Max35Text" on page 669
7.1.19.43.6  FinancialInstrumentIdentification <FinInstrmId>
Presence: [1..1]
Definition: Unique and unambiguous identifier of a financial instrument, assigned under a formal or
proprietary identification scheme.
Impacted by: C13 "DescriptionPresenceRule", C14 "DescriptionUsageRule", C19 "ISINGuideline", C20
"ISINPresenceRule", C26 "OtherIdentificationPresenceRule"
FinancialInstrumentIdentification <FinInstrmId> contains the following elements (see
"SecurityIdentification19" on page 270 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   ISIN <ISIN> [0..1] IdentifierSet 271
   OtherIdentification <OthrId> [0..*]  271
     Identification <Id> [1..1] Text 271
     Suffix <Sfx> [0..1] Text 271
     Type <Tp> [1..1] ± 271
   Description <Desc> [0..1] Text 271
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
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 339 February 2025
```

