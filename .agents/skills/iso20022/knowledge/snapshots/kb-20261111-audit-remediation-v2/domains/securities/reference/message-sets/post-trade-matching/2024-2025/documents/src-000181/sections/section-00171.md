---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.1 Account Identification", "7.1.1.2 CashAccountIdentification5Choice"]
file_pages: [223]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.1.2 CashAccountIdentification5Choice

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 223 to 223.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 223

```text
7.1.1.2  CashAccountIdentification5Choice
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 223
Or}   Proprietary <Prtry> [1..1] Text 223
7.1.1.2.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C5 "IBAN"
Datatype: "IBAN2007Identifier" on page 664
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
7.1.1.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Datatype: "Max34Text" on page 668
7.1.1.3  SecuritiesAccount35
Definition: Number assigned by a government agency to identify foreign nationals.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 223
   Type <Tp> [0..1] ± 224
   Name <Nm> [0..1] Text 224
7.1.1.3.1  Identification <Id>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 669
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 223 February 2025
```

