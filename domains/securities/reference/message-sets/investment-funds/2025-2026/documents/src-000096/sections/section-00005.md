---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["2 acmt.001.001.08 AccountOpeningInstructionV08", "2.2 Structure"]
file_pages: [22, 23, 24]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.001.001.08"]
---

# 2.2 Structure

Source: [src-000096](../../../../../../../../../raw-input/investment_funds/ISO20022_MDRPart2_Investment-Funds_2025_2026_v2.pdf). Locator: one-based file pages 22 to 24.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 22

```text
2.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctOpngInstr> [1..1]  C14,
C24
   MessageIdentification <MsgId> [1..1] ± 25
   OrderReference <OrdrRef> [0..1] ± 25
   PreviousReference <PrvsRef> [0..1] ± 25
   InstructionDetails <InstrDtls> [1..1]  25
     OpeningType <OpngTp> [1..1] ± 26
     AccountApplicationIdentification <AcctApplId> [0..1] Text 26
     ClientReference <ClntRef> [0..1] Text 26
     CounterpartyReference <CtrPtyRef> [0..1] ± 26
     ExistingAccountIdentification <ExstgAcctId> [0..*] ± 27
   InvestmentAccount <InvstmtAcct> [1..1] ± C13,
C23, C9
27
   AccountParties <AcctPties> [1..1] ± 29
   Intermediaries <Intrmies> [0..*] ± 30
   Placement <Plcmnt> [0..1] ± C22 31
   NewIssueAllocation <NewIsseAllcn> [0..1] ± 31
   SavingsInvestmentPlan <SvgsInvstmtPlan> [0..50] ± C3 32
   WithdrawalInvestmentPlan <WdrwlInvstmtPlan> [0..10] ± C3 33
   CashSettlement <CshSttlm> [0..8] ± 34
   ServiceLevelAgreement <SvcLvlAgrmt> [0..30] ± 35
   AdditionalInformation <AddtlInf> [0..*] ± 36
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 36
   Extension <Xtnsn> [0..*] ± C8 37
2.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 22 May 2026
```

## File page 23

```text
C2 ActiveOrHistoricCurrency
The Currency Code must be registered, or have already been registered. Valid active or historic
currency codes are registered with the ISO 4217 Maintenance Agency, consist of three (3)
contiguous letters, and may be or not be withdrawn on the day the message containing the
Currency is exchanged.
C3 AmountRule
If Quantity/Amount is not present, then GrossAmountIndicator is not allowed.
C4 AnyBIC
Only a valid Business identifier code is allowed. Business identifier codes for financial or non-
financial institutions are registered and published by the ISO 9362 Registration Authority in the
ISO directory of BICs, and consists of eight (8) or eleven (11) contiguous characters.
C5 BICFI
Valid BICs for financial institutions are registered and published by the ISO 9362 Registration
Authority in the ISO directory of BICs, and consist of eight (8) or eleven (11) contiguous
characters.
C6 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C7 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C8 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C9 FinancialInstrumentDetailsGuideline
FinancialInstrumentDetails may be present if a single investment fund is associated to the
investment account. If several investment funds are associated to the investment account, the
FundFamilyName only should be specified.
C10 HoldingCertificateNumberRule
If BlockHolding is CERT (Certificate) then HoldingCertificateNumber is mandatory.
C11 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C12 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C13 IncomePreferenceReinvestment1Rule
If IncomePreference is CASH (Cash), then ReinvestmentDetails is not allowed.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 23 May 2026
```

## File page 24

```text
C14 InvestmentAccountIdentificationRule
If InstructionDetails/OpeningType/Code is SUPA (SupplementaryAccountOpening), then
InvestmentAccount/Identification must be present and must contain the identification of the
main account to which the supplementary account is related.
This constraint is defined at the MessageDefinition level.
C15 MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
C16 OrganisationElementRule
One of the elements (Name, ShortName, Identification, LegalEntityIdentifier, Purpose,
RegistrationCountry, RegistrationDate, PostalAddress, TypeOfOrganisation, PlaceOfListing)
must be present.
C17 OwnershipBeneficiaryRateRule
Either Rate or Fraction must be present. Both may be present.
C18 PartialHoldingUnits1Rule
If BlockHolding is NPRH (NonPartialHolding) then PartialHoldingUnits must not be present.
C19 PartialHoldingUnits2Rule
If BlockHolding is PRTH (PartialHolding) then PartialHoldingUnits is mandatory.
C20 PartialHoldingUnits3Rule
If BlockHolding is CERT (Certificate) then PartialHoldingUnits must not be present.
C21 PoliticallyExposedPersonTypeRule
If PoliticallyExposedPersonType/Code is 'NoPoliticalExposure' (NPEX) then
PoliticallyExposedPersonStatus is not allowed.
C22 ReferredPlacementAgentRule
ReferredPlacementAgent may only be present if Referred is REFR (Referred).
C23 ReinvestmentPercentage1Rule
Sum of all occurrences of ReinvestmentDetails/ReinvestmentPercentage must not be greater
than 100.
C24 UnitRule
If SavingsInvestmentPlan is present, then SavingsInvestmentPlan/Quantity/Unit is not allowed.
On Condition
    /SavingsInvestmentPlan[*] is present
Following Must be True
    /SavingsInvestmentPlan[*]/Quantity/Unit Must be absent
This constraint is defined at the MessageDefinition level.
C25 ValidationByTable
Must be a valid terrestrial language.
C26 ValidationByTable
Must be a valid nationality.
Approved by the Securities SEG on 27 January 2026 acmt.001.001.08 AccountOpeningInstructionV08
Investment Funds - Maintenance 2025 - 2026 24 May 2026
```

