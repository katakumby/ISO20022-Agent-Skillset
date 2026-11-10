---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.24 Investment Account", "66.1.24.10 InvestmentAccount76", "66.1.24.10.8 AccountServicer <AcctSvcr>"]
file_pages: [4640, 4641]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.24.10.8 AccountServicer <AcctSvcr>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4640 to 4641.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4640

```text
Intermediary <Intrmy> contains the following elements (see "Intermediary47" on page 4966 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] ± 4966
   LegalEntityIdentifier <LglNttyIdr> [0..1] IdentifierSet 4966
   Account <Acct> [0..1]  4966
     Identification <Id> [0..1] Text 4967
     AccountServicer <AcctSvcr> [1..1] ± 4967
66.1.24.10.8  AccountServicer <AcctSvcr>
Presence: [0..1]
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
66.1.24.11  OwnershipType2Choice
Definition: Choice of formats for the specification of the ownership type.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4640
Or}   Proprietary <Prtry> [1..1] ± 4642
66.1.24.11.1  Code <Cd>
Presence: [1..1]
Definition: Ownership type expressed as a code.
Datatype: "AccountOwnershipType4Code" on page 5272
CodeName Name Definition
UNCO Unincorporated Account owner is an unincorporated
partnership or is of sole proprietorship.
LIPA LimitedPartnership Account owner is a limited partnership or
is of sole proprietorship.
ENTR Entrepreneurial Entrepreneurial account.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4640 May 2026
```

## File page 4641

```text
CodeName Name Definition
CORP Corporation Account owner is a corporate.
CUST CustodialAccount Minor's account, registered in the minor's
name. Since the minor cannot legally
own property, the custodian of the
account maintains control of the account.
EURE EUResidualEntity Account owner is an entity located in the
European Union which can be
considered neither as a legal entity (for
example, company, corporate), nor as
an individual person, nor as a UCITS
(Undertakings for Collective Investment
of Transferable Securities) fund.
PART FormalPartnership Account owner is a contractual business
organisation in which two or more
individuals agree to pool their funds to
manage and operate a business.
TRUS FormalTrust Account owner is an organisation which
is engaged as a trustee for individuals or
businesses in the administration of
services such as stock transfer,
registration, trust funds.
GOVO GovernmentOrganisation Account owner is a government
organisation.
JOIT JointAccount Two or more individuals of legal age own
shares of the same account.
COMO JointAccountInCommon Two or more individuals of legal age own
shares of the same account. Upon the
death of one of the account owners, the
respective percentage of the ownership
is transferred to the deceased's estate.
JOIN JointAccountWithSurvivorshipRights Two or more individuals own shares of
the same account. Upon the death of
one of the account owners, the entire
account ownership is passed onto the
surviving owners.
LLCO LimitedLiabilityCompany Account is for a limited liability company.
NOMI Nominee Account owner is a person or firm into
whose name securities or other
properties are transferred in order to
facilitate transactions whilst leaving the
customer as the actual owner.
NFPO NonProfitOrganisation Account owner is an association that is
given tax-free status due to the nature of
their activities such as charity
organisation.
ONIS OtherNonIndividual Account owner is another type of non
individual organisation.
RGIC RegisteredInvestmentCompany Account is for a registered investment
company.
SIGL SingleOwnerAccount Account has only one individual owner.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4641 May 2026
```

