---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.1 PartyIdentification2Choice", "66.1.29.1.2 ProprietaryIdentification <PrtryId>"]
file_pages: [4888]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.1.2 ProprietaryIdentification <PrtryId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4888 to 4888.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4888

```text
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
66.1.29.1.2  ProprietaryIdentification <PrtryId>
Presence: [1..1]
Definition: Unique and unambiguous identifier, as assigned to a financial institution using a proprietary
identification scheme.
ProprietaryIdentification <PrtryId> contains the following elements (see "GenericIdentification1" on
page 4552 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4552
   SchemeName <SchmeNm> [0..1] Text 4552
   Issuer <Issr> [0..1] Text 4552
66.1.29.1.3  NameAndAddress <NmAndAdr>
Presence: [1..1]
Definition: Name and address of a party.
NameAndAddress <NmAndAdr> contains the following elements (see "NameAndAddress5" on
page 5101 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5101
   Address <Adr> [0..1] ± 5101
66.1.29.2  Organisation40
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4888 May 2026
```

