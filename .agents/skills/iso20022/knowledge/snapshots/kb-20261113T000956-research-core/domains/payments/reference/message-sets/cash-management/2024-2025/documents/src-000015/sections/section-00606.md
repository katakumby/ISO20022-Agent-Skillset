---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "payments"
message_set: "Cash Management"
source_ids: ["src-000015"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["37 Message Items Types"]
file_pages: [783]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 37 Message Items Types

Source: [src-000015](../../../../../../../../../evidence/omitted/e79d1231c5475dd8ba11a782.md). Locator: one-based file pages 783 to 783.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 783

```text
37 Message Items Types
37.1 MessageComponents
37.1.1 Account
37.1.1.1  CashAccount40
Definition: Provides the details to identify an account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] ± 783
   Type <Tp> [0..1] ± 783
   Currency <Ccy> [0..1] CodeSet C1 784
   Name <Nm> [0..1] Text 784
   Proxy <Prxy> [0..1] ± 784
Constraints
• IdentificationAndProxyGuideline
If the account identification is not defined through a conventional identification such as an email
address or a mobile number, then the proxy element should be used for the identification of the
account.
• IdentificationOrProxyPresenceRule
Identification must be present or Proxy must be present. Both may be present.
Following Must be True
    /Identification Must be present
 Or    /Proxy Must be present
37.1.1.1.1  Identification <Id>
Presence: [0..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 787 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 787
Or}   Other <Othr> [1..1] ± 788
37.1.1.1.2  Type <Tp>
Presence: [0..1]
Approved by the Payments SEG on 04 February 2025 Message Items Types
Cash Management - Maintenance 2024 - 2025 783 February 2025
```

