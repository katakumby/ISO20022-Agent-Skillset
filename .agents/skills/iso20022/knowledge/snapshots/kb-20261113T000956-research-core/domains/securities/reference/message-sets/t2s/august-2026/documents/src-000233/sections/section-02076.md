---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types"]
file_pages: [2828]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82 Message Items Types

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2828 to 2828.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2828

```text
82 Message Items Types
82.1 MessageComponents
82.1.1 Account
82.1.1.1  CashAccount38
Definition: Provides the details to identify an account.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 2828
   Type <Tp> [0..1] ± 2828
   Currency <Ccy> [0..1] CodeSet C1 2828
   Name <Nm> [0..1] Text 2829
   Proxy <Prxy> [0..1] ± 2829
82.1.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains one of the following elements (see "AccountIdentification4Choice" on
page 2836 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2837
Or}   Other <Othr> [1..1] ± 2837
82.1.1.1.2  Type <Tp>
Presence: [0..1]
Definition: Specifies the nature, or use of the account.
Type <Tp> contains one of the following elements (see "CashAccountType2Choice" on page 2830 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 2830
Or}   Proprietary <Prtry> [1..1] Text 2831
82.1.1.1.3  Currency <Ccy>
Presence: [0..1]
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2828 August 2026
```

