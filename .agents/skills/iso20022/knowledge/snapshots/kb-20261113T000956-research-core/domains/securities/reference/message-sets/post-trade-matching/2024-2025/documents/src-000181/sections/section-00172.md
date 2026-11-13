---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Post-Trade Matching"
source_ids: ["src-000181"]
source_editions: ["February 2025"]
message_ids: []
heading_path: ["7 Message Items Types", "7.1 MessageComponents", "7.1.1 Account Identification", "7.1.1.3 SecuritiesAccount35", "7.1.1.3.2 Type <Tp>"]
file_pages: [224]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 7.1.1.3.2 Type <Tp>

Source: [src-000181](../../../../../../../../../evidence/omitted/128c587d5e2143c7e981d2b6.md). Locator: one-based file pages 224 to 224.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 224

```text
7.1.1.3.2  Type <Tp>
Presence: [0..1]
Definition: Choice between a code and a data source scheme to identify the type of account.
Type <Tp> contains one of the following elements (see "PurposeCode9Choice" on page 308 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 308
Or}   Proprietary <Prtry> [1..1] ± 309
7.1.1.3.3  Name <Nm>
Presence: [0..1]
Definition: .
Datatype: "Max70Text" on page 670
7.1.1.4  AccountIdentification55Choice
Definition: Unique identifier of an account as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C5 224
Or   BBAN <BBAN> [1..1] IdentifierSet 224
Or   UPIC <UPIC> [1..1] IdentifierSet 225
Or}   ProprietaryAccount <PrtryAcct> [1..1] ± 225
7.1.1.4.1  IBAN <IBAN>
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
7.1.1.4.2  BBAN <BBAN>
Presence: [1..1]
Approved by the Securities SEG on 13 February 2025 Message Items Types
Post Trade Matching - Maintenance 2024 - 2025 224 February 2025
```

