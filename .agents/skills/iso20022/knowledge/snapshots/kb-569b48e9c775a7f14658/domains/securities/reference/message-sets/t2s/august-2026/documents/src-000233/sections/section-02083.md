---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "TARGET2-Securities"
source_ids: ["src-000233"]
source_editions: ["August 2026"]
message_ids: []
heading_path: ["82 Message Items Types", "82.1 MessageComponents", "82.1.2 Account Identification", "82.1.2.2 CashAccountIdentification5Choice"]
file_pages: [2835]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 82.1.2.2 CashAccountIdentification5Choice

Source: [src-000233](../../../../../../../../../evidence/omitted/a39ca9be35cc4c8c0f58ea36.md). Locator: one-based file pages 2835 to 2835.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 2835

```text
82.1.2.2  CashAccountIdentification5Choice
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C2 2835
Or}   Proprietary <Prtry> [1..1] Text 2835
82.1.2.2.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C2 "IBAN"
Datatype: "IBAN2007Identifier" on page 3321
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
82.1.2.2.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Datatype: "Max34Text" on page 3327
82.1.2.3  SecuritiesAccount2Choice
Definition: Specifies one or a range of securities accounts.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Range <Rg> [1..1]  2835
     From <Fr> [1..1] ± 2836
     To <To> [1..1] ± 2836
Or}   Account <Acct> [1..*] ± 2836
82.1.2.3.1  Range <Rg>
Presence: [1..1]
Definition: Range of identifications of the securities accounts.
Approved by the Securities and Payments SEGs under the leadership of the
Securities SEG and by the Cross-SEG Harmonisation for the Business File
Header (last message set approved on 18 June 2026).
Message Items Types
Target2-Securities 2835 August 2026
```

