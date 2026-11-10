---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["37 sese.014.001.09 PortfolioTransferCancellationRequestV09", "39.4 Message Building Blocks", "39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>"]
file_pages: [1452, 1453, 1454, 1455, 1456, 1457, 1458]
content_origin: "source-text-extraction"
mentioned_message_ids: ["sese.019.001.09"]
---

# 39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 1452 to 1458.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 1452

```text
PrimaryIndividualInvestor <PmryIndvInvstr> contains the following elements (see
"IndividualPerson8" on page 5079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5079
   GivenName <GvnNm> [1..1] Text 5079
   NamePrefix <NmPrfx> [0..1] CodeSet 5079
   NameSuffix <NmSfx> [0..1] Text 5080
   Gender <Gndr> [0..1] CodeSet 5080
   BirthDate <BirthDt> [0..1] Date 5080
   SocialSecurityNumber <SclSctyNb> [0..1] Text 5080
   IndividualInvestorAddress <IndvInvstrAdr> [1..1] ± 5080
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
39.4.7 SecondaryIndividualInvestor <ScndryIndvInvstr>
Presence: [0..1]
Definition: Information identifying the secondary individual investor, for example, name, address, social
security number and date of birth.
Impacted by: C22 "SocialSecurityNumberGuideline"
SecondaryIndividualInvestor <ScndryIndvInvstr> contains the following elements (see
"IndividualPerson8" on page 5079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5079
   GivenName <GvnNm> [1..1] Text 5079
   NamePrefix <NmPrfx> [0..1] CodeSet 5079
   NameSuffix <NmSfx> [0..1] Text 5080
   Gender <Gndr> [0..1] CodeSet 5080
   BirthDate <BirthDt> [0..1] Date 5080
   SocialSecurityNumber <SclSctyNb> [0..1] Text 5080
   IndividualInvestorAddress <IndvInvstrAdr> [1..1] ± 5080
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1452 May 2026
```

## File page 1453

```text
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
39.4.8 OtherIndividualInvestor <OthrIndvInvstr>
Presence: [0..*]
Definition: Information identifying the other individual investors, for example, name, address, social
security number and date of birth.
Impacted by: C22 "SocialSecurityNumberGuideline"
OtherIndividualInvestor <OthrIndvInvstr> contains the following elements (see "IndividualPerson8"
on page 5079 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 5079
   GivenName <GvnNm> [1..1] Text 5079
   NamePrefix <NmPrfx> [0..1] CodeSet 5079
   NameSuffix <NmSfx> [0..1] Text 5080
   Gender <Gndr> [0..1] CodeSet 5080
   BirthDate <BirthDt> [0..1] Date 5080
   SocialSecurityNumber <SclSctyNb> [0..1] Text 5080
   IndividualInvestorAddress <IndvInvstrAdr> [1..1] ± 5080
Constraints
• SocialSecurityNumberGuideline
The UK Insurance Number must be indicated without spaces.
39.4.9 PrimaryCorporateInvestor <PmryCorpInvstr>
Presence: [0..1]
Definition: Information identifying the primary corporate investor, for example, name and address.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1453 May 2026
```

## File page 1454

```text
PrimaryCorporateInvestor <PmryCorpInvstr> contains the following elements (see "Organisation36"
on page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
39.4.10 SecondaryCorporateInvestor <ScndryCorpInvstr>
Presence: [0..1]
Definition: Information identifying the secondary corporate investor, for example, name and address.
SecondaryCorporateInvestor <ScndryCorpInvstr> contains the following elements (see
"Organisation36" on page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
39.4.11 OtherCorporateInvestor <OthrCorpInvstr>
Presence: [0..*]
Definition: Information identifying the other corporate investors, for example, name and address.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1454 May 2026
```

## File page 1455

```text
OtherCorporateInvestor <OthrCorpInvstr> contains the following elements (see "Organisation36" on
page 4904 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Name <Nm> [1..1] Text 4904
   Identification <Id> [0..1] ± 4904
   Purpose <Purp> [0..1] Text 4904
   TaxationCountry <TaxtnCtry> [0..1] CodeSet C12 4905
   RegistrationCountry <RegnCtry> [0..1] CodeSet C12 4905
   RegistrationDate <RegnDt> [0..1] Date 4905
   TaxIdentificationNumber <TaxIdNb> [0..1] Text 4905
   NationalRegistrationNumber <NtlRegnNb> [0..1] Text 4905
   CorporateInvestorAddress <CorpInvstrAdr> [1..1] ± 4905
39.4.12 TransferorAccount <TrfrAcct>
Presence: [1..1]
Definition: Identification of the account owned by the investor at the old plan manager (account
servicer).
TransferorAccount <TrfrAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
39.4.13 NomineeAccount <NmneeAcct>
Presence: [0..1]
Definition: Account held in the name of a party that is not the name of the beneficial owner of the
shares.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1455 May 2026
```

## File page 1456

```text
NomineeAccount <NmneeAcct> contains the following elements (see "InvestmentAccount69" on
page 4331 for details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   Identification <Id> [0..1] Text 4331
   Designation <Dsgnt> [0..1] Text 4331
   AccountName <AcctNm> [0..1] Text 4332
   Servicer <Svcr> [0..1] ± 4332
39.4.14 Transferee <Trfee>
Presence: [1..1]
Definition: Identification of the institution to which the financial instrument is to be transferred. This may
also be known as the new plan manager.
Transferee <Trfee> contains the following elements (see "PartyIdentification132" on page 5029 for
details)
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   AnyBIC <AnyBIC> [0..1] IdentifierSet C4 5029
   ClearingSystemMemberIdentification <ClrSysMmbId> [0..1] ± 5029
   NameAndAddress <NmAndAdr> [0..1] ± 5030
   ProprietaryIdentification <PrtryId> [0..1] ± 5031
   LEI <LEI> [0..1] IdentifierSet 5031
39.4.15 ProductTransfer <PdctTrf>
Presence: [1..*]
Definition: Information about the portfolio and assets.
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1456 May 2026
```

## File page 1457

```text
ProductTransfer <PdctTrf> contains the following PortfolioTransfer17 elements
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
   MasterReference <MstrRef> [0..1] Text 1459
   TransferIdentification <TrfId> [1..1] Text 1459
   Portfolio <Prtfl> [0..1]  1460
{Or     TaxEfficientProduct <TaxEffcntPdct> [1..1] ± 1460
Or     GeneralInvestment <GnlInvstmt> [1..1] ± 1461
Or}     Pension <Pnsn> [1..1]  1461
       Identification <Id> [0..1]  1461
         Identifier <Idr> [1..1] Text 1462
         SubIdentifier <SubIdr> [0..1] Text 1462
         AdditionalInformation <AddtlInf> [0..1] ± 1462
       Type <Tp> [0..1]  1462
{Or         Code <Cd> [1..1] CodeSet 1462
Or}         Proprietary <Prtry> [1..1] ± 1463
       TransferScope <TrfScp> [0..1] ± 1464
       TaxReference <TaxRef> [0..*] ± 1464
       DrawdownTrancheIdentification <DrwdwnTrchId> [0..1] Text 1464
       NonWrapperTransfer <NonWrpprTrf> [0..1] Indicator 1464
       AdditionalInformation <AddtlInf> [0..*] ± 1465
   FinancialInstrumentAssetForTransfer
<FinInstrmAsstForTrf>
[0..*]  1465
     LineIdentification <LineId> [0..1] Text 1468
     Instrument <Instrm> [1..1]  1468
{Or       Security <Scty> [1..1]  C13 1469
         Identification <Id> [1..1]  1470
{Or           ISIN <ISIN> [1..1] IdentifierSet 1471
Or           SEDOL <SEDOL> [1..1] IdentifierSet 1471
Or           CUSIP <CUSIP> [1..1] IdentifierSet 1472
Or           RIC <RIC> [1..1] IdentifierSet 1472
Or           TickerSymbol <TckrSymb> [1..1] IdentifierSet 1472
Or           Bloomberg <Blmbrg> [1..1] IdentifierSet 1472
Or           CTA <CTA> [1..1] IdentifierSet 1472
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1457 May 2026
```

## File page 1458

```text
Or MessageElement<XML Tag> Mult. Type Constr.
No.
Page
Or           QUICK <QUICK> [1..1] IdentifierSet 1472
Or           Wertpapier <Wrtppr> [1..1] IdentifierSet 1472
Or           Dutch <Dtch> [1..1] IdentifierSet 1473
Or           Valoren <Vlrn> [1..1] IdentifierSet 1473
Or           Sicovam <SCVM> [1..1] IdentifierSet 1473
Or           Belgian <Belgn> [1..1] IdentifierSet 1473
Or           Common <Cmon> [1..1] IdentifierSet 1473
Or           DTI <DTI> [1..1] IdentifierSet 1473
Or}           OtherProprietaryIdentification <OthrPrtryId> [1..1]  1473
             Identification <Id> [1..1] Text 1474
             IdentificationSource <IdSrc> [1..1] ± 1474
         Name <Nm> [0..1] Text 1474
         ShortName <ShrtNm> [0..1] Text 1474
         ClassificationType <ClssfctnTp> [0..1] ± 1474
Or       CashAsset <CshAsst> [1..1] ± 1474
Or}       OtherAsset <OthrAsst> [1..1] ± 1475
     ClientReference <ClntRef> [0..1] ± 1475
     CounterpartyReference <CtrPtyRef> [0..1] ± 1475
     TransfereeAccount <TrfeeAcct> [0..1]  1476
       OwnerIdentification <OwnrId> [0..1] ± 1476
       AccountIdentification <AcctId> [0..1] Text 1477
       Designation <Dsgnt> [0..1] Text 1477
       AccountName <AcctNm> [0..1] Text 1477
       Servicer <Svcr> [0..1] ± 1477
       SubAccountDetails <SubAcctDtls> [0..1] ± 1477
       BlockChainAddressOrWallet <BlckChainAdrOrWllt> [0..1] ± 1478
     Transferor <Trfr> [0..1]  1478
       OwnerIdentification <OwnrId> [0..1] ± 1478
       AccountIdentification <AcctId> [0..1] Text 1479
       Designation <Dsgnt> [0..1] Text 1479
       AccountName <AcctNm> [0..1] Text 1479
Approved by the Securities SEG on 27 January 2026 sese.019.001.09
AccountHoldingInformationRequestV09
Investment Funds - Maintenance 2025 - 2026 1458 May 2026
```

