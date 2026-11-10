---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.47 Tax", "66.1.47.1 TaxReporting3", "66.1.47.1.5 CashAccountDetails <CshAcctDtls>", "66.1.47.1.5.3 AccountOwner <AcctOwnr>"]
file_pages: [5217]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.47.1.5.3 AccountOwner <AcctOwnr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5217 to 5217.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5217

```text
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Identification <Id> contains the following elements (see "AccountIdentificationAndName5" on
page 4329 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4330
   Name <Nm> [0..1] Text 4330
66.1.47.1.5.3  AccountOwner <AcctOwnr>
Presence: [0..1]
Definition: Party that legally owns the account.
AccountOwner <AcctOwnr> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
66.1.47.1.5.4  AccountServicer <AcctSvcr>
Presence: [0..1]
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains one of the following elements (see
"FinancialInstitutionIdentification11Choice" on page 4480 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   NameAndAddress <NmAndAdr> [1..1] ± 4480
Or   BICFI <BICFI> [1..1] IdentifierSet C5 4480
Or   ClearingSystemMemberIdentification <ClrSysMmbId> [1..1] ± 4481
Or}   ProprietaryIdentification <PrtryId> [1..1]  4481
     Identification <Id> [1..1] Text 4482
66.1.47.1.5.5  AccountServicerBranch <AcctSvcrBrnch>
Presence: [0..1]
Definition: Information identifying a specific branch of a financial institution.
Usage: this component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5217 May 2026
```

