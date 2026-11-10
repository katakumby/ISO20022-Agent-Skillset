---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.30 Party Identification", "66.1.30.8 MoneyLaunderingCheck1Choice", "66.1.30.8.1 Code <Cd>"]
file_pages: [4923]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.30.8.1 Code <Cd>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4923 to 4923.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4923

```text
66.1.30.8.1  Code <Cd>
Presence: [1..1]
Definition: Money laundering status expressed as a code.
Datatype: "MoneyLaunderingCheck1Code" on page 5330
CodeName Name Definition
PASS Passed Money laundering identification
procedures have been carried out by the
intermediary.
NOTC NotChecked Money laundering identification
procedures have not been carried out.
EXEM ExemptBelowLimit Money laundering identification
procedures have not been carried out
because the transaction is below the
prescribed limit.
CLMO ClientMoneyTypeExempt Money laundering identification
procedures have not been carried out
because of the transaction type, for
example, switch, or because the
transaction is being funded from an
existing investor account held by the
intermediary.
AUTH AuthorisedCredit Money laundering identification
procedures have not been carried out
because the investor is an authorised
credit or financial institution.
POEP PostalOrElectronicPaymentExempt Limited money laundering identification
procedures have been carried out
because it is a one time only transaction
and the payment is being made by
postal, telephone or electronic transfers
from an existing account with an
authorised credit or financial institution.
66.1.30.8.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Money laundering status expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.30.9  ModificationScope43
Definition: Scope of the modification to be applied on an identified set of information.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4923 May 2026
```

