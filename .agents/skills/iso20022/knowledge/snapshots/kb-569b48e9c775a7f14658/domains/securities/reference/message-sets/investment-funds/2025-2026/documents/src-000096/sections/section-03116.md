---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.2 Account Identification", "66.1.2.11 CashAccountIdentification8Choice", "66.1.2.11.2 IBAN <IBAN>"]
file_pages: [4340]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.2.11.2 IBAN <IBAN>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4340 to 4340.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4340

```text
Definition: Unique identification of an account, as assigned by the account servicer, using an
identification scheme.
Other <Othr> contains the following elements (see "GenericAccountIdentification1" on page 4326 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4326
   SchemeName <SchmeNm> [0..1]  4326
{Or     Code <Cd> [1..1] CodeSet 4326
Or}     Proprietary <Prtry> [1..1] Text 4326
   Issuer <Issr> [0..1] Text 4326
66.1.2.11.2  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C19 "IBAN"
Datatype: "IBAN2007Identifier" on page 5394
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
66.1.3 Address
66.1.3.1  CommunicationAddress6
Definition: Communication device number or electronic address used for communication.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4340 May 2026
```

