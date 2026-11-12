---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.6 PartyIdentification220", "66.1.29.6.1 Identification <Id>", "66.1.29.6.1.2 ProprietaryIdentification <PrtryId>"]
file_pages: [4902]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.6.1.2 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4902 to 4902.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4902

```text
Datatype: "AnyBICDec2014Identifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the ISO
directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
66.1.29.6.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to the party using a proprietary identification
scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.29.6.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of the party.
NameAndAddress <NmAndAdr> contains the following NameAndAddress15 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4902
   PostalAddress <PstlAdr> [0..1] ± C23 4902
66.1.29.6.1.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which the party is known and which is usually used to identify that party.
Datatype: "Max350Text" on page 5403
66.1.29.6.1.3.2  PostalAddress <PstlAdr>
Presence: [0..1]
Definition: Postal address of the party.
Impacted by: C23 "MailingIndicatorRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4902 May 2026
```

