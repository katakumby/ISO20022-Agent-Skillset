---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.8 Financial Institution Identification", "16.1.8.5 ClearingSystemMemberIdentification2", "16.1.8.5.2 MemberIdentification <MmbId>"]
file_pages: [869]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.8.5.2 MemberIdentification <MmbId>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 869 to 869.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 869

```text
ClearingSystemIdentification <ClrSysId> contains one of the following elements (see
"ClearingSystemIdentification2Choice" on page 1155 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 1155
Or}   Proprietary <Prtry> [1..1] Text 1155
16.1.8.5.2  MemberIdentification <MmbId>
Presence: [1..1]
Definition: Identification of a member of a clearing system.
Datatype: "Max35Text" on page 1251
16.1.9 Financial Instrument
16.1.9.1  SecurityIdentification19
Definition: Identification of a security.
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
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 869 February 2026
```

