---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.33 Postal Address", "66.1.33.1 DeliveryParameters3", "66.1.33.1.2 IssuedCertificateNumber <IssdCertNb>"]
file_pages: [5097]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.33.1.2 IssuedCertificateNumber <IssdCertNb>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5097 to 5097.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5097

```text
Address <Adr> contains the following elements (see "NameAndAddress4" on page 5100 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [0..1] Text 5100
   Address <Adr> [1..1] ± 5100
66.1.33.1.2  IssuedCertificateNumber <IssdCertNb>
Presence: [0..1]
Definition: Certificate representing a security that is delivered.
Datatype: "Max35Text" on page 5403
66.1.33.2  LongPostalAddress1Choice
Definition: Information that locates and identifies a specific address, as defined by postal services.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Unstructured <Ustrd> [1..1] Text 5097
Or}   Structured <Strd> [1..1] ± C14 5097
66.1.33.2.1  Unstructured <Ustrd>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in free format text.
Datatype: "Max140Text" on page 5402
66.1.33.2.2  Structured <Strd>
Presence: [1..1]
Definition: Information that locates and identifies a specific address, as defined by postal services, that
is presented in a formal structure.
Impacted by: C14 "StreetNameAndOrPostOfficeBoxRule"
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5097 May 2026
```

