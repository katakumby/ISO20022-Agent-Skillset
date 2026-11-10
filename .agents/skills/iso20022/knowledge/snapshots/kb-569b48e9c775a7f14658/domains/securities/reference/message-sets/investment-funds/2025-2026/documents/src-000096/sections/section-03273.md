---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["66 Message Items Types", "66.1 MessageComponents", "66.1.18 Financial Instrument", "66.1.18.9 GovernanceProcess1Choice", "66.1.18.9.2 Proprietary <Prtry>"]
file_pages: [4509, 4510]
content_origin: "source-text-extraction"
mentioned_message_ids: []
---

# 66.1.18.9.2 Proprietary <Prtry>

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 4509 to 4510.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 4509

```text
CodeName Name Definition
CMIF NotMiFID Product governance procedure is not in
accordance with MiFID II.
AMIF PursuantMiFID Product governance procedure is
pursuant to MiFID II.
66.1.18.9.2  Proprietary <Prtry>
Presence: [1..1]
Definition: Type of governance process expressed as a proprietary code.
Proprietary <Prtry> contains the following elements (see "GenericIdentification47" on page 4539 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [1..1] Text 4540
   Issuer <Issr> [1..1] Text 4540
   SchemeName <SchmeNm> [0..1] Text 4540
66.1.18.10  GeneralInvestment2
Definition: Information about a general investment.
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Type <Tp> [0..1] ± 4509
   OwnershipType <OwnrshTp> [0..1] CodeSet 4509
   CurrentInvestmentAmount <CurInvstmtAmt> [0..1] Amount C1 4511
   EstimatedValue <EstmtdVal> [0..1] ± 4511
   AdditionalInformation <AddtlInf> [0..*] ± 4511
66.1.18.10.1  Type <Tp>
Presence: [0..1]
Definition: Type of investment.
Type <Tp> contains one of the following elements (see "GeneralInvestmentAccountType2Choice" on
page 4507 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
{Or   Code <Cd> [1..1] CodeSet 4507
Or}   Proprietary <Prtry> [1..1] ± 4507
66.1.18.10.2  OwnershipType <OwnrshTp>
Presence: [0..1]
Definition: Specifies whether the account is, for example, in a nominee name or own name.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4509 May 2026
```

## File page 4510

```text
Datatype: "AccountOwnershipType6Code" on page 5273
CodeName Name Definition
BOWN BareOwner A person has bare ownership on the
asset.
CORP Corporation Account owner is a corporate.
CUST CustodialAccount Minor's account, registered in the minor's
name. Since the minor cannot legally
own property, the custodian of the
account maintains control of the account.
ENTR Entrepreneurial Entrepreneurial account.
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
LIPA LimitedPartnership Account owner is a limited partnership or
is of sole proprietorship.
NOMI Nominee Account owner is a person or firm into
whose name securities or other
properties are transferred in order to
facilitate transactions whilst leaving the
customer as the actual owner.
NFPO NonProfitOrganisation Account owner is an association that is
given tax-free status due to the nature of
their activities such as charity
organisation.
Approved by the Securities SEG on 27 January 2026 Message Items Types
Investment Funds - Maintenance 2025 - 2026 4510 May 2026
```

