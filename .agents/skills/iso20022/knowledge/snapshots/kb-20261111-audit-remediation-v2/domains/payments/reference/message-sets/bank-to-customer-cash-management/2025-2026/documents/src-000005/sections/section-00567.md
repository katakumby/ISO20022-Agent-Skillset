---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Bank-to-Customer Cash Management"
source_ids: ["src-000005"]
source_editions: ["March 2026"]
message_ids: []
heading_path: ["6 Message Items Types", "6.1 MessageComponents", "6.1.1 Account", "6.1.1.4 GenericAccountIdentification1", "6.1.1.4.2 SchemeName <SchmeNm>", "6.1.1.4.2.1 Code <Cd>"]
file_pages: [800]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 6.1.1.4.2.1 Code <Cd>

Source: [src-000005](../../../../../../../../../evidence/omitted/4704d0f065c82a397d84d52d.md). Locator: one-based file pages 800 to 800.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 800

```text
SchemeName <SchmeNm> contains one of the following AccountSchemeName1Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 800
Or}   Proprietary <Prtry> [1..1] Text 800
6.1.1.4.2.1  Code <Cd>
Presence: [1..1]
Definition: Name of the identification scheme, in a coded form as published in an external list.
Datatype: "ExternalAccountIdentification1Code" on page 892
6.1.1.4.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Name of the identification scheme, in a free text form.
Datatype: "Max35Text" on page 916
6.1.1.4.3  Issuer <Issr>
Presence: [0..1]
Definition: Entity that assigns the identification.
Datatype: "Max35Text" on page 916
6.1.2 Account Identification
6.1.2.1  SecuritiesAccount19
Definition: Account to or from which a securities entry is made.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 800
   Type <Tp> [0..1] ± 800
   Name <Nm> [0..1] Text 801
6.1.2.1.1  Identification <Id>
Presence: [1..1]
Definition: Unambiguous identification for the account between the account owner and the account
servicer.
Datatype: "Max35Text" on page 916
6.1.2.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the type of securities account.
Approved by the Payments SEG on 12 January 2026 Message Items Types
Bank-to-Customer Cash Management - Maintenance 2025 -
2026
800 March 2026
```

