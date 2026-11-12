---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.42 Settlement Instruction", "66.1.42.1 CashSettlement4", "66.1.42.1.2 CashAccountDetails <CshAcctDtls>", "66.1.42.1.2.5 AccountServicerBranch <AcctSvcrBrnch>"]
file_pages: [5149]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.42.1.2.5 AccountServicerBranch <AcctSvcrBrnch>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 5149 to 5149.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 5149

```text
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
66.1.42.1.2.5  AccountServicerBranch <AcctSvcrBrnch>
Presence: [0..1]
Definition: Information identifying a specific branch of a financial institution.
Usage: this component should be used in case the identification information in the financial institution
component does not provide identification up to branch level.
AccountServicerBranch <AcctSvcrBrnch> contains the following elements (see "BranchData4" on
page 4482 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4482
   Name <Nm> [0..1] Text 4482
   PostalAddress <PstlAdr> [0..1] ± 4482
66.1.42.1.2.6  AccountOwnerOtherIdentification <AcctOwnrOthrId>
Presence: [0..*]
Definition: Alternative identification, for example, national registration identification number, passport
number, tax identification number. This may be an account number used to further identify the
beneficial owner, for example, a Central Provident Fund (CFP) account as required for Singapore.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 5149 May 2026
```

