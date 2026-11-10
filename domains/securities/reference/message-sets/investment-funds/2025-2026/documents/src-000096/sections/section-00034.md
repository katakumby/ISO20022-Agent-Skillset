---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["4 acmt.003.001.08 AccountModificationInstructionV08", "4.2 Structure"]
file_pages: [59, 60, 61, 62]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.003.001.08"]
---

# 4.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 59 to 62.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 59

```text
4.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctModInstr> [1..1]  C30
   MessageIdentification <MsgId> [1..1] ± 63
   PreviousReference <PrvsRef> [0..1] ± 63
   InstructionDetails <InstrDtls> [0..1]  C18 63
     ModificationReason <ModRsn> [0..1] Text 64
     AccountApplicationIdentification <AcctApplId> [0..1] Text 64
     ClientReference <ClntRef> [0..1] Text 64
     CounterpartyReference <CtrPtyRef> [0..1] ± 64
     ExistingAccountIdentification <ExstgAcctId> [0..*] ± 65
   InvestmentAccountSelection <InvstmtAcctSelctn> [1..1]  65
{Or     AccountIdentification <AcctId> [1..1] Text 65
Or}     OtherAccountSelectionData <OthrAcctSelctnData> [1..1] ± C1 65
   ModifiedInvestmentAccount <ModfdInvstmtAcct> [0..1] ± C2, C17,
C29,
C12
66
   ModifiedAccountParties <ModfdAcctPties> [0..*] ± C5 69
   ModifiedIntermediaries <ModfdIntrmies> [0..*] ± 70
   ModifiedPlacement <ModfdPlcmnt> [0..1] ± 70
   ModifiedIssueAllocation <ModfdIsseAllcn> [0..1] ± 71
   ModifiedSavingsInvestmentPlan <ModfdSvgsInvstmtPlan> [0..50] ± 71
   ModifiedWithdrawalInvestmentPlan <ModfdWdrwlInvstmtPlan> [0..10] ± 72
   ModifiedCashSettlement <ModfdCshSttlm> [0..8] ± 73
   ModifiedServiceLevelAgreement <ModfdSvcLvlAgrmt> [0..30] ± 74
   ModifiedAdditionalInformation <ModfdAddtlInf> [0..*] ± 75
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 75
   Extension <Xtnsn> [0..*] ± C11 75
4.3 Constraints
C1 AccountDataElementRule
One of the elements (Name, Designation, FundType, FundFamilyName, SecurityDetails,
AccountOwner, Intermediary, Account Servicer) must be present.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 59 May 2026
```

## File page 60

```text
C2 AccountElementRule
One of the elements (AccountStatusUpdateInstruction, Name, Designation, Type,
OwnershipType, TaxExemption, StatementFrequency, ReferenceCurrency, Language,
IncomePreference, ReinvestmentDetails, TaxWithholdingMethod, TaxReporting,
LetterIntentDetails, AccumulationRightReference, RequiredSignatoriesNumber,
FundFamilyName, ModifiedFinancialInstrumentDetails, RoundingDetails, Account Servicer,
BlockedStatus, AccountUsageType, ForeignStatusCertification, AccountSignatureDateTime,
TransactionChannelType, InvestmentAccountCategory, Pledging, Collateral, ThirdPartyRights,
PowerOfAttorneyLevelOfControl, AccountingStatus, OpeningDate, ClosingDate,
NegativeIndicator, ProcessingOrder, Liability, ModifiedInvestorProfile, FiscalYear) must be
present.
C3 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
C4 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C5 AddressRule
If ModificationScopeIndication is INSE (InsertNewDataSet), then one of the following must be
present:
PrincipalAccountParty/./Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
CustodianForMinor/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
SecondaryOwner/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Beneficiary/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
PowerOfAttorney/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
LegalGuardian/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
SuccessorOnDeath/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Administrator/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
OtherParty/OtherPartyDetails/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 60 May 2026
```

## File page 61

```text
Granter/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
Settlor/Party/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet)
SeniorManagingOfficial/./ModifiedPostalAddress/ModificationScopeIndication/INSE
(InsertNewDataSet)
Protector/./ModifiedPostalAddress/ModificationScopeIndication/INSE (InsertNewDataSet).
C6 AmountRule
If Quantity/Amount is not present, then GrossAmountIndicator is not allowed.
C7 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C8 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C9 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C10 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C11 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C12 FinancialInstrumentDetailsGuideline
ModifiedFinancialInstrumentDetails/FinancialInstrumentDetails may be present if a single
investment fund is associated to the investment account. If several investment funds are
associated to the investment account, the FundFamilyName only should be specified.
C13 HoldingCertificateNumberRule
If BlockHolding is CERT (Certificate) then HoldingCertificateNumber is mandatory.
C14 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C15 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 61 May 2026
```

## File page 62

```text
C16 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C17 IncomePreferenceReinvestmentRule
If IncomePreference is CASH (Cash), then ReinvestmentDetails is not allowed.
C18 InstructionDetailsElementRule
One of the elements (ModificationReason, AccountApplicationIdentification, ClientReference,
CounterpartyReference, ExistingAccountIdentification) must be present.
C19 MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
C20 OrganisationElementRule
One of the elements (Name, ShortName, Identification, LegalEntityIdentifier, Purpose,
RegistrationCountry, RegistrationDate, ModifiedPostalAddress, TypeOfOrganisation,
PlaceOfListing) must be present.
C21 OrganisationIdentificationRule
Either Identification or Legal Entity Identifier must be present. Both Identification and Legal
Entity Identifier may be present.
C22 OwnershipBeneficiaryRateRule
Either Rate or Fraction must be present. Both may be present.
C23 PartialHoldingUnits1Rule
If BlockHolding is NPRH (NonPartialHolding) then PartialHoldingUnits must not be present.
C24 PartialHoldingUnits2Rule
If BlockHolding is PRTH (PartialHolding) then PartialHoldingUnits is mandatory.
C25 PartialHoldingUnits3Rule
If BlockHolding is CERT (Certificate) then PartialHoldingUnits must not be present.
C26 PoliticallyExposedPersonTypeRule
If PoliticallyExposedPersonType/Code is 'NoPoliticalExposure' (NPEX) then
PoliticallyExposedPersonStatus is not allowed.
C27 ReasonElementRule
Either Code or AdditionalInformation must be present. Both may be present.
C28 ReferredPlacementAgentRule
ReferredPlacementAgent may only be present if Referred is REFR (Referred).
C29 ReinvestmentPercentageRule
Sum of all occurrences of ReinvestmentDetails/ReinvestmentPercentage must not be greater
than 100.
Approved by the Securities SEG on 27 January 2026 acmt.003.001.08 AccountModificationInstructionV08
Investment Funds - Maintenance 2025 - 2026 62 May 2026
```

