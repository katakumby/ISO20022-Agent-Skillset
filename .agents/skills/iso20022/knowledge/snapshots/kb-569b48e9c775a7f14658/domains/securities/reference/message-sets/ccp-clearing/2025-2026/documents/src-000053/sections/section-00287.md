---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "CCP Clearing"
source_ids: ["src-000053"]
source_editions: ["March 2026; Standards MX November 2026 release"]
message_ids: []
heading_path: ["12 Message Items Types", "12.1 MessageComponents", "12.1.2 Account Identification", "12.1.2.1 AccountIdentification26", "12.1.2.1.1 Proprietary <Prtry>"]
file_pages: [376]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 12.1.2.1.1 Proprietary <Prtry>

Source: [src-000053](../../../../../../../../../evidence/omitted/4e6ea171978d4b0a5cc40b11.md). Locator: one-based file pages 376 to 376.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 376

```text
12.1.2.1.1  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Proprietary <Prtry> contains the following SimpleIdentificationInformation4 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 376
12.1.2.1.1.1  Identification <Id>
Presence: [1..1]
Definition: Name or number assigned by an entity to enable recognition of that entity, for example,
account identifier.
Datatype: Max35Text on page 493
12.1.2.2  AccountIdentification4Choice
Definition: Specifies the unique identification of an account as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet   'C8 376
Or}   Other <Othr> [1..1] ± 377
12.1.2.2.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by:   'C8 IBAN  '
Datatype: IBAN2007Identifier on page 489
Constraints
• IBAN
(Rule)
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
Error handling:
– Error severity: Fatal
– Error Code: D00003
Message Definition Report - Part 2
Central CounterParty (CCP) Securities Clearing - November 2026 for
Standards MX
Message Items Types
March 2026 376
```

