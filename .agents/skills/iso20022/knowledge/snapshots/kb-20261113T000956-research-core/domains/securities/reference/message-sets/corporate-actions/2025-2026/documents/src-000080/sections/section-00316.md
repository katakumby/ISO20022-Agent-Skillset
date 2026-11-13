---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["7 seev.035.001.17 CorporateActionMovementPreliminaryAdviceV17", "7.4 Message Building Blocks", "7.4.13 CorporateActionMovementDetails <CorpActnMvmntDtls>", "7.4.13.16 AppliedOptionIndicator <ApldOptnInd>"]
file_pages: [436]
content_origin: "source-text-extraction"
mentioned_message_ids: ["seev.035.001.17"]
---

# 7.4.13.16 AppliedOptionIndicator <ApldOptnInd>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 436 to 436.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 436

```text
Definition: Indicates whether change of instruction is allowed.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
7.4.13.16  AppliedOptionIndicator <ApldOptnInd>
Presence: [0..1]
Definition: Indicates whether the option, different from the default one, shall be applied by the account
owner.
Datatype: One of the following values must be used (see "YesNoIndicator" on page 1246):
• Meaning When True: Yes
• Meaning When False: No
7.4.13.17  SecurityIdentification <SctyId>
Presence: [0..1]
Definition: Identifies the financial instrument.
Impacted by: C17 "DescriptionPresenceRule", C18 "DescriptionUsageRule", C44 "ISINGuideline", C45
"ISINPresenceRule", C57 "OtherIdentificationPresenceRule"
SecurityIdentification <SctyId> contains the following elements (see "SecurityIdentification19" on
page 869 for details)
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
Approved by the Securities SEG on 27 January 2026 seev.035.001.17
CorporateActionMovementPreliminaryAdviceV17
Corporate Actions - Maintenance 2025 - 2026 436 February 2026
```

