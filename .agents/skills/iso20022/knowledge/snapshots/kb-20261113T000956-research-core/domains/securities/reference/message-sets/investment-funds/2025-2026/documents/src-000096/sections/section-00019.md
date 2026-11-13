---
template: false
document_kind: "source-section"
review_status: "needs-review"
domain: "securities"
message_set: "Investment Funds"
source_ids: ["src-000096"]
source_editions: ["May 2026"]
message_ids: []
heading_path: ["3 acmt.002.001.08 AccountDetailsConfirmationV08", "3.2 Structure"]
file_pages: [40, 41, 42]
content_origin: "source-text-extraction"
mentioned_message_ids: ["acmt.002.001.08"]
---

# 3.2 Structure

Source: [src-000096](../../../../../../../../../evidence/omitted/fffd4ab68b421d059524ec38.md). Locator: one-based file pages 40 to 42.

PDF text evidence. Columns and vector figures require comparison with rendered pages. Printed page labels are retained in the extracted text; file page numbers below are authoritative file locators.

## File page 40

```text
3.2 Structure
Or MessageElement/BuildingBlock<XML Tag> Mult. Type Constr.
No.
Page
Message root <Document> <AcctDtlsConf> [1..1]  C22,
C33
   MessageIdentification <MsgId> [1..1] ± 43
   OrderReference <OrdrRef> [0..1] ± 43
   RelatedReference <RltdRef> [0..1] ± 44
   ConfirmationDetails <ConfDtls> [1..1]  44
     ConfirmationType <ConfTp> [1..1] ± 44
     AccountApplicationIdentification <AcctApplId> [0..1] Text 45
     ClientReference <ClntRef> [0..1] Text 45
     CounterpartyReference <CtrPtyRef> [0..1] ± 45
     ExistingAccountIdentification <ExstgAcctId> [0..*] ± 45
   InvestmentAccount <InvstmtAcct> [0..1] ± C21,
C31,
C17
46
   AccountParties <AcctPties> [0..1] ± 48
   Intermediaries <Intrmies> [0..*] ± 49
   Placement <Plcmnt> [0..1] ± C30 50
   NewIssueAllocation <NewIsseAllcn> [0..1] ± 50
   SavingsInvestmentPlan <SvgsInvstmtPlan> [0..50] ± C3 51
   WithdrawalInvestmentPlan <WdrwlInvstmtPlan> [0..10] ± C3 52
   CashSettlement <CshSttlm> [0..8] ± 53
   ServiceLevelAgreement <SvcLvlAgrmt> [0..30] ± 54
   AdditionalInformation <AddtlInf> [0..*] ± 55
   MarketPracticeVersion <MktPrctcVrsn> [0..1] ± 55
   Extension <Xtnsn> [0..*] ± C16 56
3.3 Constraints
C1 ActiveCurrency
The currency code must be a valid active currency code, not yet withdrawn on the day the
message containing the currency is exchanged. Valid active currency codes are registered with
the ISO 4217 Maintenance Agency, consist of three (3) contiguous letters, and are not yet
withdrawn on the day the message containing the Currency is exchanged.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 40 May 2026
```

## File page 41

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
C6 ClosedStatus1Rule
If Closed is present then Enabled is not allowed.
C7 ClosedStatus2Rule
If Closed is present then Disabled is not allowed.
C8 ClosedStatus3Rule
If Closed is present then Pending is not allowed.
C9 ClosedStatus4Rule
If Closed is present then PendingOpening is not allowed.
C10 ClosedStatus5Rule
If Closed is present then Proforma is not allowed.
C11 ClosedStatus6Rule
If Closed is present then ClosurePending is not allowed.
C12 Country
The code is checked against the list of country names obtained from the United Nations (ISO
3166, Alpha-2 code).
C13 CurrencyAmount
The number of fractional digits (or minor unit of currency) must comply with ISO 4217.
Note: The decimal separator is a dot.
C14 EnabledDisabledStatus1Rule
If Enabled is present, then Disabled is not allowed.
C15 EnabledDisabledStatus2Rule
If Disabled is present, then Enabled is not allowed.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 41 May 2026
```

## File page 42

```text
C16 ExtensionRule
This component may not be used without the explicit approval of the Registration Authority and
without strict usage rules published by the Registration Authority.
C17 FinancialInstrumentDetailsGuideline
FinancialInstrumentDetails may be present if a single investment fund is associated to the
investment account. If several investment funds are associated to the investment account, the
FundFamilyName only should be specified.
C18 HoldingCertificateNumberRule
If BlockHolding is CERT (Certificate) then HoldingCertificateNumber is mandatory.
C19 IBAN
A valid IBAN consists of all three of the following components: Country Code, check digits and
BBAN.
C20 IdentificationGuideline
It is recommended that ISIN is used in Identification.
When an ISIN code exists, it is strongly recommended that the ISIN be used.
C21 IncomePreferenceReinvestment1Rule
If IncomePreference is CASH (Cash), then ReinvestmentDetails is not allowed.
C22 InvestmentAccountRule
If ConfirmationDetails/ConfirmationType/Code is ACCO (AccountOpening), then
InvestmentAccount must be present.
This constraint is defined at the MessageDefinition level.
C23 MailingIndicatorRule
If RegistrationAddressIndicator is "true" or "1" (Yes), then MailingIndicator must be "true" or "1".
C24 OrganisationElementRule
One of the elements (Name, ShortName, Identification, LegalEntityIdentifier, Purpose,
RegistrationCountry, RegistrationDate, PostalAddress, TypeOfOrganisation, PlaceOfListing)
must be present.
C25 OwnershipBeneficiaryRateRule
Either Rate or Fraction must be present. Both may be present.
C26 PartialHoldingUnits1Rule
If BlockHolding is NPRH (NonPartialHolding) then PartialHoldingUnits must not be present.
C27 PartialHoldingUnits2Rule
If BlockHolding is PRTH (PartialHolding) then PartialHoldingUnits is mandatory.
C28 PartialHoldingUnits3Rule
If BlockHolding is CERT (Certificate) then PartialHoldingUnits must not be present.
Approved by the Securities SEG on 27 January 2026 acmt.002.001.08 AccountDetailsConfirmationV08
Investment Funds - Maintenance 2025 - 2026 42 May 2026
```

