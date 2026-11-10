---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Corporate Actions"
source_ids: ["src-000080"]
source_editions: ["February 2026"]
message_ids: []
heading_path: ["16 Message Items Types"]
file_pages: [829]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 16 Message Items Types

Source: [src-000080](../../../../../../../../../evidence/omitted/dfb597659e5318b4c0abe01e.md). Locator: one-based file pages 829 to 829.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 829

```text
16 Message Items Types
16.1 MessageComponents
16.1.1 Account Identification
16.1.1.1  CashAccountIdentification9Choice
Definition: Unique identifier of an account, as assigned by the account servicer.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IBAN <IBAN> [1..1] IdentifierSet C16 829
Or   BlockChainCashWallet <BlckChainCshWllt> [1..1] ± 829
Or}   Proprietary <Prtry> [1..1] Text 830
16.1.1.1.1  IBAN <IBAN>
Presence: [1..1]
Definition: International Bank Account Number (IBAN) - identifier used internationally by financial
institutions to uniquely identify the account of a customer. Further specifications of the format and
content of the IBAN can be found in the standard ISO 13616 "Banking and related financial services -
International Bank Account Number (IBAN)" version 1997-10-01, or later revisions.
Impacted by: C16 "IBAN"
Datatype: "IBAN2007Identifier" on page 1245
Constraints
• IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
16.1.1.1.2  BlockChainCashWallet <BlckChainCshWllt>
Presence: [1..1]
Definition: Block Chain Wallet where digital currencies are maintained. This is the equivalent of cash
account for digital currencies.
BlockChainCashWallet <BlckChainCshWllt> contains the following elements (see
"BlockChainAddressWallet3" on page 925 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 925
   Type <Tp> [0..1] ± 926
   Name <Nm> [0..1] Text 926
Approved by the Securities SEG on 27 January 2026 Message Items Types
Corporate Actions - Maintenance 2025 - 2026 829 February 2026
```

