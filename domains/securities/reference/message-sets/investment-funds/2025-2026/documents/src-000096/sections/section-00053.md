---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["5 acmt.005.001.06 RequestForAccountManagementStatusReportV06", "5.4 Message Building Blocks", "5.4.2 RequestDetails <ReqDtls>", "5.4.2.5 InvestmentAccount <InvstmtAcct>", "5.4.2.5.4 OwnerIdentification <OwnrId>", "5.4.2.5.4.1 IndividualOwnerIdentification <IndvOwnrId>", "5.4.2.5.4.1.1 IdentificationNumber <IdNb>"]
file_pages: [84, 85]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.005.001.06"]
---

# 5.4.2.5.4.1.1 IdentificationNumber <IdNb>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 84 to 85.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 84

```text
5.4.2.5.4.1.1  IdentificationNumber <IdNb>
Presence: [1..1]
Definition: Identification of a party, such as a tax or social security identifier.
IdentificationNumber <IdNb> contains the following elements (see "GenericIdentification81" on
page 4543 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4544
   IdentificationType <IdTp> [1..1]  4544
{Or     Code <Cd> [1..1] CodeSet 4544
Or}     Proprietary <Prtry> [1..1] ± 4545
5.4.2.5.4.1.2  PersonName <PrsnNm>
Presence: [1..1]
Definition: Human entity, as distinguished from a corporate entity (which is sometimes referred to as an
'artificial person').
PersonName <PrsnNm> contains the following elements (see "IndividualPerson30" on page 5074 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   GivenName <GvnNm> [0..1] Text 5075
   MiddleName <MddlNm> [0..1] Text 5075
   Name <Nm> [1..1] Text 5075
   Gender <Gndr> [0..1] CodeSet 5075
   BirthDate <BirthDt> [0..1] Date 5075
5.4.2.5.4.2  OrganisationOwnerIdentification <OrgOwnrId>
Presence: [1..1]
Definition: Identification of an organisation.
OrganisationOwnerIdentification <OrgOwnrId> contains the following elements (see
"PartyIdentification139" on page 5043 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Party <Pty> [1..1] ± 5043
   LEI <LEI> [0..1] IdentifierSet 5043
5.4.2.5.5  AccountServicer <AcctSvcr>
Presence: [0..1]
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 84 May 2026
```

## File page 85

```text
Definition: Party that manages the account on behalf of the account owner, that is manages the
registration and booking of entries on the account, calculates balances on the account and provides
information about the account.
AccountServicer <AcctSvcr> contains one of the following elements (see
"PartyIdentification125Choice" on page 4909 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   AnyBIC <AnyBIC> [1..1] IdentifierSet C4 4909
Or   ProprietaryIdentification <PrtryId> [1..1] ± 4909
Or}   NameAndAddress <NmAndAdr> [1..1] ± 4910
Approved by the Securities SEG on 27 January 2026 acmt.005.001.06
RequestForAccountManagementStatusReportV06
Investment Funds - Maintenance 2025 - 2026 85 May 2026
```

