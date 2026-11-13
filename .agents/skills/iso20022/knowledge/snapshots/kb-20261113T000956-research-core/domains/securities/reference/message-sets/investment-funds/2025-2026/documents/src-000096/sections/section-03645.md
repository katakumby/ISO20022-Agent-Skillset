---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.29 Organisation Identification", "66.1.29.3 PartyIdentification1Choice", "66.1.29.3.3 NameAndAddress <NmAndAdr>", "66.1.29.3.3.1 Name <Nm>"]
file_pages: [4895]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.29.3.3.1 Name <Nm>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4895 to 4895.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4895

```text
66.1.29.3.3.1  Name <Nm>
Presence: [1..1]
Definition: Name by which a party is known and which is usually used to identify that party.
Datatype: "Max35Text" on page 5403
66.1.29.3.3.2  Address <Adr>
Presence: [0..1]
Definition: Information that locates and identifies a specific address, as defined by postal services.
Address <Adr> contains one of the following elements (see "LongPostalAddress1Choice" on
page 5097 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 5097
Or}   Structured <Strd> [1..1] ± C14 5097
66.1.29.4  PartyIdentification3
Definition: Unique and unambiguous way to identify an organisation.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   BICOrBEI <BICOrBEI> [1..1] IdentifierSet C5 4895
66.1.29.4.1  BICOrBEI <BICOrBEI>
Presence: [1..1]
Definition: Code allocated to a financial or non-financial institution by the ISO 9362 Registration
Authority, as described in ISO 9362 "Banking - Banking telecommunication messages - Business
identifier code (BIC)".
Impacted by: C5 "AnyBIC"
Datatype: "AnyBICIdentifier" on page 5389
Constraints
• AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered by the ISO 9362 Registration Authority in the BIC directory, and
consists of eight (8) or eleven (11) contiguous characters.
66.1.29.5  Organisation39
Definition: Organised structure that is set up for a particular purpose, for example, a business,
government body, department, charity, or financial institution.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4895 May 2026
```

