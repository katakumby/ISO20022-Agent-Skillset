---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.16 Direct Debit", "66.1.16.1 DirectDebitMandate7", "66.1.16.1.1 DebtorAccount <DbtrAcct>"]
file_pages: [4477]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.16.1.1 DebtorAccount <DbtrAcct>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4477 to 4477.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4477

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   DebtorAccount <DbtrAcct> [1..1] ± 4477
   Debtor <Dbtr> [0..1] ± 4477
   DebtorTaxIdentificationNumber <DbtrTaxIdNb> [0..1] Text 4477
   DebtorNationalRegistrationNumber <DbtrNtlRegnNb> [0..1] Text 4478
   Creditor <Cdtr> [0..1] ± 4478
   DebtorAgent <DbtrAgt> [1..1] ± 4478
   DebtorAgentBranch <DbtrAgtBrnch> [0..1] ± 4478
   CreditorAgent <CdtrAgt> [0..1] ± 4479
   CreditorAgentBranch <CdtrAgtBrnch> [0..1] ± 4479
   RegistrationIdentification <RegnId> [0..1] Text 4479
   MandateIdentification <MndtId> [0..1] Text 4480
66.1.16.1.1  DebtorAccount <DbtrAcct>
Presence: [1..1]
Definition: Unambiguous identification of the account of the debtor to which a debit entry will be made
as a result of the transaction.
DebtorAccount <DbtrAcct> contains the following elements (see "AccountIdentificationAndName5" on
page 4329 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4330
   Name <Nm> [0..1] Text 4330
66.1.16.1.2  Debtor <Dbtr>
Presence: [0..1]
Definition: Party that owes the cash to the creditor/final party. The debtor is also the debit account
owner.
Debtor <Dbtr> contains one of the following elements (see "PartyIdentification125Choice" on
page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.16.1.3  DebtorTaxIdentificationNumber <DbtrTaxIdNb>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4477 May 2026
```

