---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types", "16.1 MessageComponents", "16.1.1 Account Identification", "16.1.1.1 CashAccountIdentification9Choice", "16.1.1.1.3 Proprietary <Prtry>"]
file_pages: [830]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16.1.1.1.3 Proprietary <Prtry>

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 830 to 830.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 830

```text
16.1.1.1.3  Proprietary <Prtry>
Presence: [1..1]
Definition: Unique identifier for an account. It is assigned by the account servicer using a proprietary
identification scheme.
Datatype: "Max34Text" on page 1250
16.1.1.2  AccountIdentification10
Definition: Provides account identification information.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   IdentificationCode <IdCd> [1..1] CodeSet 830
16.1.1.2.1  IdentificationCode <IdCd>
Presence: [1..1]
Definition: Standard code to specify that announcement applies to all safekeeping accounts that own
underlying financial instrument.
Datatype: "SafekeepingAccountIdentification1Code" on page 1241
CodeName Name Definition
GENR General Announcement applies to all
safekeeping accounts that own
underlying financial instrument. (Used for
general or preliminary announcements.).
16.1.1.3  CashAccountIdentification5Choice
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 830
Or}   Proprietary <Prtry> [1..1] Text 831
16.1.1.3.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C16 "IBAN"
Datatype: "IBAN2007Identifier" on page 1245
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 830 February 2026
```

