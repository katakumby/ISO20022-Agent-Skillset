---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types", "37.1 MessageComponents", "37.1.1 Account", "37.1.1.4 GenericAccountIdentification1", "37.1.1.4.2 SchemeName <SchmeNm>", "37.1.1.4.2.1 Code <Cd>"]
file_pages: [787]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37.1.1.4.2.1 Code <Cd>

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 787 to 787.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 787

```text
SchemeName <SchmeNm> contains one of the following AccountSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 787
Or}   Proprietary <Prtry> [1..1] Text 787
37.1.1.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalAccountIdentification1Code" on page 852
37.1.1.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 889
37.1.1.4.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 889
37.1.2 Account Identification
37.1.2.1  AccountIdentification4Choice
Definition: Specifies the unique identification of an account as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
37.1.2.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C5 "IBAN"
Datatype: "IBAN2007Identifier" on page 885
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 787 February 2025
```

