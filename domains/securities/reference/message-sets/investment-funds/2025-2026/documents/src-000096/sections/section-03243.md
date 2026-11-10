---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.16 Direct Debit", "66.1.16.1 DirectDebitMandate7", "66.1.16.1.8 CreditorAgent <CdtrAgt>"]
file_pages: [4479]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.16.1.8 CreditorAgent <CdtrAgt>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 4479 to 4479.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4479

```text
DebtorAgentBranch <DbtrAgtBrnch> contains the following elements (see "BranchData4" on
page 4482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
66.1.16.1.8  CreditorAgent <CdtrAgt>
Presence: [0..1]
Definition: Financial institution that receives the payment transaction on behalf of the creditor, or other
nominated party, and credits the account.
CreditorAgent <CdtrAgt> contains one of the following elements (see
"FinancialInstitutionIdentification11Choice" on page 4480 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 4480
Or   BICFI <BICFI> [1..1] IdentifierSet C5 4480
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4481
Or}   ProprietaryIdentification <PrtryId> [1..1]  4481
     Identification <Id> [1..1] Text 4482
66.1.16.1.9  CreditorAgentBranch <CdtrAgtBrnch>
Presence: [0..1]
Definition: Information identifying a specific branch of a financial institution.
Usage: this component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
CreditorAgentBranch <CdtrAgtBrnch> contains the following elements (see "BranchData4" on
page 4482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
66.1.16.1.10  RegistrationIdentification <RegnId>
Presence: [0..1]
Definition: Reference assigned to a creditor by its financial institution, or relevant authority, authorising
the creditor to take part in a direct debit scheme.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4479 May 2026
```

