---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.4 Message Building Blocks", "5.4.2 RequestDetails <ReqDtls>", "5.4.2.5 InvestmentAccount <InvstmtAcct>", "5.4.2.5.1 AccountIdentification <AcctId>"]
file_pages: [83]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.4.2.5.1 AccountIdentification <AcctId>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 83 to 83.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 83

```text
5.4.2.5.1  AccountIdentification <AcctId>
Presence: [1..1]
Definition: Unique and unambiguous identification for the account between the account owner and the
account servicer.
Datatype: "Max35Text" on page 5403
5.4.2.5.2  AccountName <AcctNm>
Presence: [0..1]
Definition: Name of the account. It provides an additional means of identification, and is designated by
the account servicer in agreement with the account owner.
Datatype: "Max35Text" on page 5403
5.4.2.5.3  AccountDesignation <AcctDsgnt>
Presence: [0..1]
Definition: Supplementary registration information applying to a specific block of units for dealing and
reporting purposes. The supplementary registration information may be used when all the units are
registered, for example, to a funds supermarket, but holdings for each investor have to be reconciled
individually.
Datatype: "Max35Text" on page 5403
5.4.2.5.4  OwnerIdentification <OwnrId>
Presence: [0..1]
Definition: Identification of the owner of the account.
OwnerIdentification <OwnrId> contains one of the following OwnerIdentification3Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IndividualOwnerIdentification <IndvOwnrId> [1..1]  83
{Or     IdentificationNumber <IdNb> [1..1] ± 84
Or}     PersonName <PrsnNm> [1..1] ± 84
Or}   OrganisationOwnerIdentification <OrgOwnrId> [1..1] ± 84
5.4.2.5.4.1  IndividualOwnerIdentification <IndvOwnrId>
Presence: [1..1]
Definition: Identification of the individual person.
IndividualOwnerIdentification <IndvOwnrId> contains one of the following
IndividualPersonIdentification2Choice elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   IdentificationNumber <IdNb> [1..1] ± 84
Or}   PersonName <PrsnNm> [1..1] ± 84
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 83 May 2026
```

