---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.4 Message Building Blocks", "5.4.2 RequestDetails <ReqDtls>", "5.4.2.3 AccountApplicationIdentification <AcctApplId>"]
file_pages: [82]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.4.2.3 AccountApplicationIdentification <AcctApplId>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 82 to 82.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 82

```text
CodeName Name Definition
ACCO AccountOpening Refers to an account opening instruction
message.
GACC GetAccountDetails Refers to a get account details message.
ACST AccountStatus Refers to the account status.
5.4.2.3  AccountApplicationIdentification <AcctApplId>
Presence: [0..1]
Definition: Unique and unambiguous identifier of the account opening or account modification
instruction at application level.
Datatype: "Max35Text" on page 5403
5.4.2.4  ExistingAccountIdentification <ExstgAcctId>
Presence: [0..1]
Definition: Account to which the account opening is related.
ExistingAccountIdentification <ExstgAcctId> contains the following elements (see "Account23" on
page 4325 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 4325
   RelatedAccountDetails <RltdAcctDtls> [0..1] ± 4325
5.4.2.5  InvestmentAccount <InvstmtAcct>
Presence: [0..1]
Definition: Account information for which the status of an account management instruction is requested.
InvestmentAccount <InvstmtAcct> contains the following InvestmentAccount77 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AccountIdentification <AcctId> [1..1] Text 83
   AccountName <AcctNm> [0..1] Text 83
   AccountDesignation <AcctDsgnt> [0..1] Text 83
   OwnerIdentification <OwnrId> [0..1]  83
{Or     IndividualOwnerIdentification <IndvOwnrId> [1..1]  83
{Or       IdentificationNumber <IdNb> [1..1] ± 84
Or}       PersonName <PrsnNm> [1..1] ± 84
Or}     OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± 84
   AccountServicer <AcctSvcr> [0..1] ± 84
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 82 May 2026
```

